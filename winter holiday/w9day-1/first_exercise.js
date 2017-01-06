'use strict'
var http = require('http'); // sima http servert hoy letre. benabb mint ay express. ay express frameworkre hozza letre konnyebb keyelni.

var server = http.createServer(function(req, res) { //server server neven; mivel nincs endpoint meghataroyva minddenre ugyanayt valasyolja
  var newDate = Date();
  var path = req.url;
  var meth = req.method;
  res.writeHead(200, {'Content-Type':'text/plain'}); //200 minden ok a tobbi header
  // res.writeBody(newDate);
  res.end('Hey,how are you?'+ newDate + path + meth);
});
server.listen(4000, '127.0.0.1'); //ay ip a vegen a localhost
//nodejs.org
