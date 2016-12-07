'use strict';

var numbers = [2.4, 3.5, 1.7, 3.3, 1.2];

// create a function that takes an array of numbers,
// it should return a new array that consists only the numbers that are
// bigger than 2 and all of it's elements should be rounded

function selector(inputarray){
  //map filter
  var outputarray = [];
  return inputarray.filter(function(element) {
      return element > 2;
  }).map(Math.round)

}
console.log(selector(numbers));
