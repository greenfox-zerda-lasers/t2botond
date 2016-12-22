'use strict'
var http = require('http');

var server = http.createServer(function(req, res) {
  var newDate = Date();
  var path = req.url;
  var meth = req.method;
  res.writeHead(200, {'Content-Type':'text/plain'});
  // res.writeBody(newDate);
  res.end('Hey,how are you?'+ newDate + path + meth);
});
server.listen(4000, '127.0.0.1');
