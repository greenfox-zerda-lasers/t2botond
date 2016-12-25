'use strict'

function truth(text){
  console.log(text + ' is shit');
}

var tellTheTruth = truth;

tellTheTruth('javascript');

function add(a, b){
  return a+b;
}
console.log(add(1,2));

function run(func, arg){
  func(arg);
}
function reality(texts){
  console.log(texts + " is shitty!");
}
run(reality, 'Javascript');
