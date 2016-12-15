'use strict';

var test = require('tape');

var ai = 123;
// create a function that doubles it's input
// double ai with it
function doubler(x) {
  return 2*x
}

// console.log(doubler(ai))

  test('double value', function(r){
      var totest = doubler(0);
      var expected = 0;

      r.equal(totest, expected);
      r.end();
    });

  test('double value', function(r){
      var totest = doubler(-1);
      var expected = -2;

      r.equal(totest, expected);
      r.end();
    });

    test('double value', function(r){
        var totest = doubler(90000);
        var expected = 180000;

        r.equal(totest, expected);
        r.end();
      });

    test('double value', function(r){
        var totest = doubler(0.001);
        var expected = 0.002;

        r.equal(totest, expected);
        r.end();
      });
