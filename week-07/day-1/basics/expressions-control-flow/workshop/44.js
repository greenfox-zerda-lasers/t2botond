'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)
function min(list){
  var min = list[0]
  for (var i = 0; i < list.length; i++){
    if (list[i] < min){
      min = list[i]
    }
  }
  return min
}
console.log(min(numbers));
