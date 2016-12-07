'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements
function second(arr, fun){
  arr.forEach(function(element) {fun(element) }); // next to fun(element), fun index, fun array can be calles also
}
var a = [1, 2, 3, 4, 5, 6,'f',3, 2]
second(a, console.log)
