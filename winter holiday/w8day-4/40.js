'use strict'
var test = require('tape')

var aj = 'kuty'
// write a function that gets a string as an input
// and appends an 'a' character to its end and returns a new string
function aappend(str){
  str += 'a'
  return str
}

// console.log(aappend(aj))

test('syammal', function(p){
  var r = aappend('');
  var res = 'a'
  p.equal(r, res);
  p.end();
})
