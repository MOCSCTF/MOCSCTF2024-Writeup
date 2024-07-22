#[macro_use] extern crate rocket;

use rocket::form::Form;
use rocket::serde::{Serialize, Deserialize, json::Json};
use rocket::fs::{FileServer, relative};
use std::collections::HashMap;
use std::sync::Mutex;
use uuid::Uuid;

struct AppState {
    balances: Mutex<HashMap<Uuid, u32>>,
    add_attempts: Mutex<HashMap<Uuid, u32>>,
    max_attempts: u32,
}

#[derive(FromForm)]
struct AddBalance {
    user_id: String,
    amount: u32,
}

#[derive(Serialize)]
struct RegisterResponse {
    user_id: String,
}

#[post("/register")]
fn register(state: &rocket::State<AppState>) -> Json<RegisterResponse> {
    let user_id = Uuid::new_v4();
    let mut balances = state.balances.lock().unwrap();
    let mut attempts = state.add_attempts.lock().unwrap();

    balances.insert(user_id, 100);
    attempts.insert(user_id, 0);

    Json(RegisterResponse {
        user_id: user_id.to_string(),
    })
}

#[get("/")]
fn index() -> &'static str {
    "visit /start to access the interface."
}

#[post("/add_balance", data = "<form>")]
fn add_balance(form: Form<AddBalance>, state: &rocket::State<AppState>) -> String {
    let user_id = match Uuid::parse_str(&form.user_id) {
        Ok(id) => id,
        Err(_) => return "Invalid user ID".to_string(),
    };

    let mut balances = state.balances.lock().unwrap();
    let mut attempts = state.add_attempts.lock().unwrap();

    let balance = balances.entry(user_id).or_insert(100);
    let attempt = attempts.entry(user_id).or_insert(0);

    if *attempt >= state.max_attempts {
        return format!("你已达到增加余额的最大次数! 当前余额: {}", *balance);
    }
    *balance = balance.wrapping_add(form.amount); 
    *attempt += 1;
    format!("余额已增加! 当前余额: {}", *balance)
}

#[derive(FromForm)]
struct BuyFlag {
    user_id: String,
}

#[post("/buy_flag", data = "<form>")]
fn buy_flag(form: Form<BuyFlag>, state: &rocket::State<AppState>) -> String {
    let user_id = match Uuid::parse_str(&form.user_id) {
        Ok(id) => id,
        Err(_) => return "Invalid user ID".to_string(),
    };

    let mut balances = state.balances.lock().unwrap();
    let balance = balances.entry(user_id).or_insert(100);

    if *balance == 1 {
        *balance = 0;
        "恭喜，你购买到了flag:MOCSCTF{REDACTED}".to_string()
    } else {
        format!("余额必须为 1 元才能购买 flag! 当前余额: {}", *balance)
    }
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AppState {
            balances: Mutex::new(HashMap::new()),
            add_attempts: Mutex::new(HashMap::new()),
            max_attempts: 3, // 设置最大尝试次数为3次
        })
        .mount("/", routes![index, add_balance, buy_flag, register])
        .mount("/start", FileServer::from(relative!("static")))
}
