'use strict';

var numbers = [2, 5, 11, 31];
//true
//[Finished in 931.127s]
// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function ifprime(arr) {

  function isprime(item){
    for (var i = 2; i < item; i++){
      if (item % i == 0){
        return false;
      }
    }
    return true;
    }
  return arr.every(isprime)
}
console.log(ifprime(numbers));
