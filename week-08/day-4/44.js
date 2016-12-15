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
test('shortest', function(f){
  var totest = shortest(['ffrwfer', 'vfev','rr','fttfqergve'])
  var res = 'rr'
  f.equal(totest, res)
  f.end()
})

test('shortest', function(f){
  var totest = shortest(['ffr', 'vfev','rr','fte'])
  var res = 'rr'
  f.equal(totest, res)
  f.end()
})
