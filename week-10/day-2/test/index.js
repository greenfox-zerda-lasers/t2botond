'use strict';

var test = require('tape');
var request = require('supertest');
var app = require('../server');

test('First test!', function (t) {
  t.end();
});

test('Playlists returned', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('404 on lobab', function (t) {
  request(app)
    .get('/lobab')
    .expect(404)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('teapot', function (t) {
  request(app)
    .get('/teapot')
    .expect(418)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

 test('post playlist', function (t) {
request(app)
    .push({
      id : 1,
      title : 'Never Give Up',
      author : 'Ars Sonor',
      file : 'music/Ars_Sonor_-_02_-_Never_Give_Up.mp3',
      length : '1:20',
    })
    .expect(418)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});
