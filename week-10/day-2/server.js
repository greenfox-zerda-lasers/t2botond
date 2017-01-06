
'use strict';

var express = require('express');
var app = express();
var playlists =
[
{
  id : 1,
  title : 'Never Give Up',
  file : 'music/Ars_Sonor_-_02_-_Never_Give_Up.mp3',
  author : 'Ars Sonor',
  length : '1:20',
},
{
  id : 2,
  title : 'Doctor Talos Answers The Door',
  file : 'music/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3',
  author : 'Doctor Turtle',
  length : '2:10',
},
{
  id : 3,
  title : 'Purple Drift',
  file : 'music/Organoid_-_09_-_Purple_Drift.mp3',
  author : 'Organoid',
  length : '3:30',
}];
;

app.get('/playlists', function (req, res) {
  res.send(playlists);
});

app.get('/teapot', function (req, res) {
  res.sendStatus(418);
});
app.post('/playlist', function(req, res){
  playlist.push(res)
  console.log(playlist);
})
module.exports = app;
