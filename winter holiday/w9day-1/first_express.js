'use strict'
var express = require('express');

var app = express();
app.get('*', function(req, res) { // ossyres endpointra figyel mindig eyyel valasyol
  var date = Date();
  var path = req.url;
  var meth = req.method;
  res.send('Hey! How are you?' + date + path + meth);
});
app.listen(3000);
