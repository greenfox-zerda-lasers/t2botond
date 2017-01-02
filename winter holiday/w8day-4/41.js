'use strict';

var test = require('tape')
// create a function that returns it's input factorial

function factorial(value) {
  var result = 1;
  for(var i = 1; i < value + 1; i++){
    result = result * i;
  }
  return result;
}
// console.log(factorial(5))
test('lastfact', function(j){
  var fir = factorial(5);
  var exp = 120;
  j.equal(fir, exp);
  j.end();
})
