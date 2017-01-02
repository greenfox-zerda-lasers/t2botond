'use sttict';
var test = require('tape')
var numbers = [8, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function min(array){
  var minval = array[0]
  for (var i = 1; i < array.length; i++) {
    console.log('f')
    if(minval > array[i]){
      minval = array[i]
    }
  }
  return minval
}
// console.log(min(numbers));
test('mi', function(f){
  var o = min([1,2,3,4,5]);
  var c = 1;
  f.equal(o, c);
  f.end();
})
