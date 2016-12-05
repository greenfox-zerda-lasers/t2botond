'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array
function shortest(list){
  var sh = list[0]
  for (var i = 0; i < list.length; i++){
    if (list[i].length < sh.length){
      sh = list[i]
    }
  }
  return sh
}

console.log(shortest(names));
