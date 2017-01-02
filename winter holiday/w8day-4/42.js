'use strict';

var test = require('tape')

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens
function evenreturner(array){
  var list = [];
  for(var i = 0; i < array.length; i++){
    if(array[i]%2 == 0){
      list.push(array[i]);
    }
  }
  return list;
}
// console.log(evenreturner(numbers))

test('e', function(o){
  var r = evenreturner([3, 7]);
  var res = [];
  o.deepEqual(r, res);
  o.end();
})
