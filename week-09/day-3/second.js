'use strict';

var express = require('express');
var bodyParser = require('body-parser');

var app = express(); //http syervert l;trehozo modul.
app.use(bodyParser.json());//middleware httpk;r;s test r;sy;t parseolja form'yya
app.use(express.static('./todo'));  //ossyes statikus kerest e todo mappabol szolgalja ki pl fajlok kerese
//cors modul engedelzezi hogy masik domainrol is mehessenek a keresek

//app.use(cors()) cors oldalan ellenorizni


app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, DELETE, PUT, POST")
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});   //cors miatt nem kell

var mysql = require('mysql');
var con = mysql.createConnection({  //csatlakozas mmysql serverhez alapbol elindul...
  host:'localhost',
  user:'root',
  password:'6025',
  database:'todo'
});

con.connect(function(err){  ///callback fuggveny ami parameterkent van adva es kesobb van meghivva. ey csak hibakezeles miatt van
  if(err){
    console.log('Error connecting to todos');
    return;
  }
  console.log('Connection established');
});

// var list = [{ completed: false, id: 1, text: 'Buy milk' },
// { completed: true, id: 2, text: 'Make dinner' },
// { completed: false, id: 3, text: 'Save the world' }];

app.get('/todos', function a(req, res) {
  // res.set('Content-Type', 'application/json');
  // console.log(list);
  if(req.query.completed){  //req query az url bol kerdojel modotti resz /todos?completed= hd fhvfejvbfjvbef
    con.query('SELECT * FROM todos where completed='+ req.query.completed, function(err, rows){
      if(err){
        console.log('Error connecting to todos');
        return;
      }
      console.log(rows)
      res.send(rows);
    })
  }
  else {
  con.query('SELECT * FROM todos', function(err, rows){
    if(err){
      console.log('Error connecting to todos');
      return;
    }
    console.log(rows)
    res.send(rows);
  })
}
  // res.send('hello')
});
app.get('/todos/:id', function b(req, res){
  con.query('SELECT * from todos WHERE id ='+ req.params.id, function c(err, rows){ ///req.body htp keres belso tartalma, most json volt
    if(err){                                                                        ///req.params a kettospont utani parameter
      console.log('Error connecting to todos');
      return;
    }
    res.send(rows[0]);
  });
});

// app.get('/todos', function l(req, res){
//   con.query('SELECT * FROM todos where completed=', function m(err, rows){
//     if(err){
//       console.log('No items in this status');
//       return;
//     }
//     console.log(rows);
//     res.send(rows);
//   })
// })
app.post('/todos',

function d(req, res){
  // con.query('INSERT INTO todos(text, completed) VALUES(\''+ req.body.text+'\',0)',function c(err, rows){
  con.query('INSERT INTO todos(text, completed) VALUES(?,0)', [req.body.text], function c(err, rows){
    if(err){
      console.log('Error connecting to todos');
      return;
    }
})      // your JSON
})
app.put('/todos/:id', function e(req, res){
  con.query('UPDATE todos SET text = "' + req.body.text + '",completed = ' + req.body.completed +' WHERE id ='+ req.params.id,function f(err, rows){
    if(err){
      console.log('putos fut');
      return;
    }
    res.send({id:req.params.id, text:req.body.text, completed: req.body.completed})
  })
})
app.delete('/todos/:id', function g(req, res){
  con.query('SELECT * FROM todos WHERE id ='+ req.params.id, function k(err, rows){
    if(rows.length == 0){
      res.status(404).send();
    }
    else {
      res.send(rows[0]);}
  });
  con.query('DELETE from todos WHERE id ='+req.params.id, function h(err, rows){
  })
})
// app.get('/todos', function b(req, res) {
  // console.log(req.query);
// /  if(req.query.completed == 'true'){ //ey viysgalja a queryparametert, hgy igay e?   todos/?completed=true
//       var filtered
//       filtered = list.filter( function h(item){
//         return item.completed //mert boolean ertek nem kell ossyehasonlitani
//       })
//       console.log(filtered);
//       res.send(filtered);
//   }
//   else {res.send(JSON.stringify(list));
//   // res.send('hello')
// }});
// app.put('/todos/:id', function f(req, res) {
//   let changeitem = parseInt(req.params.id);
//   let idcounter;
//   list.forEach(function g(item, index){
//     // console.log(changeitem, item.id);
//     if (item.id == changeitem){
//       console.log('bbkvrjkjvfre');
//       item.completed = req.body.completed;
//       item.text = req.body.text;
//       idcounter = index;
//     }
//   })
//   if(idcounter == undefined){
//     res.status(404).send('no such id')
//   }
//   res.send(list[idcounter]);
// })
// app.post('/todos', function c(req, res) {
//   counter += 1;
//   list.push({ text: req.body.text, id: counter, completed: false });      // your JSON
//   res.send({ text: req.body.text, id: counter, completed: false });    // echo the result back
// });
//
// app.delete('/todos/:id', function d(req, res) {
//    let deleteid = parseInt(req.params.id);
//    let deletitem = list.filter(function n(item){
//      return item.id === deleteid;
//    })
//   let filtered = list.filter(function e(item) {
//     return item.id !== deleteid;
//   });
//   list = filtered;
//   res.send(deletitem[0]);
// });

app.listen(5000);
