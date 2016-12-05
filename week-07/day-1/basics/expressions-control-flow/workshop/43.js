'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens
function filter(list){
  var even = []
  for (var i = 0; i < list.length; i = i + 1){
    if (i % 2 == 0){
      even[i / 2] = list[i]
    }
  }
  return even
}
console.log(filter(numbers));
