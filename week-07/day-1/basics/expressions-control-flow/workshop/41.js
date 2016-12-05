'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function summary(array){
  var sum = 0
  for(var i = 0; i < array.length; i++){
  sum = sum + array[i]
  }
  return sum
}
console.log(summary(numbers));
