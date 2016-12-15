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

test('factorialer', function(p){
  var functtotest = factorial(1);
  var result = 1;

  p.equal(functtotest, result);
  p.end()
});

test('factorialer', function(p){
  var functtotest = factorial(3);
  var result = 6;

  p.equal(functtotest, result);
  p.end()
});

test('factorialer', function(p){
  var functtotest = factorial(5);
  var result = 120;

  p.equal(functtotest, result);
  p.end()
});
