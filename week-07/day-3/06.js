'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise
function searcher(word, letter){
  return word.indexOf(letter) != -1;
}

var wo = 'Python was better!';
var le = 'w';

console.log(searcher(wo, le));
