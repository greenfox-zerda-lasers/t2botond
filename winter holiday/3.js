
'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

function shit(arr, func){
  arr.forEach(function(i) {func(i)});
}
var arr = [1,2,3,4,5,6];
shit(arr, console.log);

console.log('');
function massminus(numberlist, minusfunc){
  numberlist.forEach(function(listitem){minusfunc(listitem)});
}
  var numberlist = [ 3,2,1,0]
  
function minus(x){
  console.log(x-1);
}

massminus(numberlist, minus);
