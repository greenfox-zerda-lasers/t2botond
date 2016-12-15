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

test('a - append', function(r){
    var totest = aappend('macsk');
    var expected = 'macska';

    r.equal(totest, expected);
    r.end();
  });

  test('a - append', function(r){
      var totest = aappend("6543");
      var expected = '6543a';

      r.equal(totest, expected);
      r.end();
    });

    test('a - append', function(r){
        var totest = aappend(6543);
        var expected = '6543a';

        r.equal(totest, expected);
        r.end();
      });

test('a - append', function(r){
  var totest = aappend('');
  var expected = 'a';

  r.equal(totest, expected);
  r.end();
});
