const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.send('Team MOCSCTF-A secret chat');
});

app.get('/secret', (req, res) => {
    res.send('My secret is exposed :(');
});

app.post('/secret', (req, res) => {
    const { password } = req.body;
    if (password == "M" + "O" + +"CTF" + "a" ) {
        fs.readFile("./flag.txt", 'utf8', (err, data) => {
            if (err) {
                console.error('Error reading file:', err);
                    res.status(500).send('Error reading file');
            } else {
                    res.json({ status: 'success', message: data});
            }
        });
    } else {
        res.json({ status: 'error', message: 'Wrong Secret!' });
    }
});

app.listen(port, () => {
    console.log(`MOCSCTF-A app listening at http://localhost:${port}`);
});
