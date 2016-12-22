var express = require('express');

var app = express();

app.get('/', function (req, res) {
  res.send('Hey! How are you?');
});

app.listen(5000);
