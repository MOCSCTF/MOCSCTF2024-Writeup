const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.json());

const tasks = {};

function merge(target, source) {
    for (let key in source) {
        if (source.hasOwnProperty(key)) {
            target[key] = source[key];
        }
    }
    return target;
}
app.get('/',(req,res) =>   {
    return 'Welcom my Task System seems it hasn\'t finished';
}
app.post('/addTask', (req, res) => {
    const { id, description } = req.body;
    if (typeof id === 'string' && typeof description === 'string') {
        tasks[id] = { description };
        res.json({ status: 'success', message: 'Task added successfully' });
    } else {
        res.json({ status: 'error', message: 'Invalid task format' });
    }
    console.log("Current tasks:", tasks);
});

app.post('/updateTask', (req, res) => {
    const { id, updates } = req.body;
    if (tasks.hasOwnProperty(id) && typeof updates === 'object') {
        tasks[id] = merge(tasks[id], updates);
        res.json({ status: 'success', message: 'Task updated successfully' });
    } else {
        res.json({ status: 'error', message: 'Invalid task or updates format' });
    }
    console.log("Updated tasks:", tasks);
});

app.post('/readFile', (req, res) => {
    const { id } = req.body;
    const task = tasks[id];
    if (task) {
        const filePath = task.filePath;
        if (filePath) {
            fs.readFile(filePath, 'utf8', (err, data) => {
                if (err) {
                    console.error('Error reading file:', err);
                    res.status(500).send('Error reading file');
                } else {
                    res.send(data);
                }
            });
        } else {
            res.status(400).send('No file path specified for this task');
        }
    } else {
        res.status(400).send('Invalid task ID');
    }
});

app.listen(port, () => {
    console.log(`Task app listening at http://localhost:${port}`);
});
