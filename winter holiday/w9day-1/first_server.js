var express = require('express');  //express modul beimportalas

var app = express(); //app neven syervert csinal

app.get('/', function (req, res){ //melzik endpointokra figyeljen itt a / jelre reagal
  res.send('Hey! How are you?');
});

app.listen(5000); //port 1 ip cimhez sok port megy ey kivalasztja
 // npm init    (-f forced)    a package.jsonhoz ebben tarolodnak adatok a preojektrol es milyen kulso cuccok kellenek hoyya pl express
 // npm install express --save        ay express telepiteshey a saveval a package.jsonhoy is bekerul
// npm install body-parser
// npm install mysql
// npm install tape
