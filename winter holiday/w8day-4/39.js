'use strict';

var test = require('tape');

var ai = 123;
// create a function that doubles it's input
// double ai with it
function doubler(x) {
  return 2*x
}

// console.log(doubler(ai))
test('doubler', function(kk){
  var fir = doubler(123);
  var res = 246;
  kk.equal(fir, res);
  kk.end();
})
