'use strict';

var express = require('express');
var bodyParser = require('body-parser');

var app = express();
app.use(bodyParser.json());

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, DELETE, PUT, POST")
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

var list = [{ completed: false, id: 1, text: 'Buy milk' },
{ completed: true, id: 2, text: 'Make dinner' },
{ completed: false, id: 3, text: 'Save the world' }];
var counter = 3;

app.get('/todos/:id', function a(req, res) {
  // res.set('Content-Type', 'application/json');
  // console.log(list);
  res.send(JSON.stringify(list[parseInt(req.params.id) - 1]));
  // res.send('hello')
});
app.get('/todos', function b(req, res) {
  // res.set('Content-Type', 'application/json');
  // console.log(list);
  console.log(req.query);
  if(req.query.completed == 'true'){ //ey viysgalja a queryparametert, hgy igay e?   todos/?completed=true
      var filtered
      filtered = list.filter( function h(item){
        return item.completed //mert boolean ertek nem kell ossyehasonlitani
      })
      console.log(filtered);
      res.send(filtered);
  }
  else {res.send(JSON.stringify(list));
  // res.send('hello')
}});
app.put('/todos/:id', function f(req, res) {
  let changeitem = parseInt(req.params.id);
  let idcounter;
  list.forEach(function g(item, index){
    // console.log(changeitem, item.id);
    if (item.id == changeitem){
      console.log('bbkvrjkjvfre');
      item.completed = req.body.completed;
      item.text = req.body.text;
      idcounter = index;
    }
  })
  if(idcounter == undefined){
    res.status(404).send('no such id')
  }
  res.send(list[idcounter]);
})
app.post('/todos', function c(req, res) {
  counter += 1;
  list.push({ text: req.body.text, id: counter, completed: false });      // your JSON
  res.send({ text: req.body.text, id: counter, completed: false });    // echo the result back
});

app.delete('/todos/:id', function d(req, res) {
   let deleteid = parseInt(req.params.id);
   let deletitem = list.filter(function n(item){
     return item.id === deleteid;
   })
  let filtered = list.filter(function e(item) {
    return item.id !== deleteid;
  });
  list = filtered;
  res.send(deletitem[0]);
});

app.listen(5000);
