'use strict';
var test = require('tape')
var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array
function shortest(array){
  var item = array[0]
  for(var i = 0; i < array.length; i++){
    if(item.length > array[i].length){
      item = array[i]
    }
  }
  return item
}
// console.log(shortest(names));
test('cold', function(l){
  var p = shortest(['werty','wer','ertyy','r']);
  var v = 'r';
  l.equal(p, v);
  l.end();
})
