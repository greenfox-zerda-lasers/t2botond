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
test('evenreturner',function(k){
  var valtotest = evenreturner([9, 8, 7, 6, 5, 4, 3, 2, 1]);
  var expected = [8, 6, 4, 2];
  k.deepEqual(valtotest, expected);
  k.end();
});
