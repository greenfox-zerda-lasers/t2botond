'use strict';

var express = require('express');
var app = express();
var playlists = ['John', 'Betty', 'Hal'];

app.get('/playlists', function (req, res) {
  res.json(playlists);
});

app.get('/teapot', function (req, res) {
  res.sendStatus(418);
});

module.exports = app;
