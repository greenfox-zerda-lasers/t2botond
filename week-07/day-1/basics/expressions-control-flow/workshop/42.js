'use strict';

// create a function that returns it's input factorial
function fact(num){
  var result = 1
  for (var i = 1; i < num + 1; i++){
    result = result * i
  }
  return result
}

console.log(fact(9));
