'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function lettercounter(text){
//  split, characters to stirng, object.keys, x in object
  var emptyobj = {}
  text.split('').forEach(function(char){
    console.log(char);
    if (Object.keys(emptyobj).indexOf(char) >= 0) {
  //  if (char in emptyobj) {
      emptyobj[char] += 1
    }
    else {
      emptyobj[char] = 1
    }
  })
  return emptyobj

}
var string = "bhrvurbbu NPOKq"
console.log(lettercounter(string));
