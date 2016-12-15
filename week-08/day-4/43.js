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
test('min', function(k){
  var testvalue = min([99999,545,4321,-44,9.6]);
  var testresult = -44;
  k.equal(testvalue, testresult);
  k.end();
})
test('min', function(k){
  var testvalue = min([-1, -5563, -565]);
  var testresult = -5563;
  k.equal(testvalue, testresult);
  k.end();
})
test('min', function(k){
  var testvalue = min([0.1, 0.001, 0.00001]);
  var testresult = 0.00001;
  k.equal(testvalue, testresult);
  k.end();
})
