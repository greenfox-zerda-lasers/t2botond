console.log(['elso','masodik','harmadik'].indexOf('masodik'));

['elso','masodik','harmadik'].forEach(function(elem) {console.log(elem);})

var fourTimes = [1, 2, 3, 4, 5, 6].map(function(i){return i*4; });
console.log(fourTimes);

// var fTimes = [1, 2, 3, 4, 5, 6].forEach(function(shitpiece) {console.log(shitpiece*4); });

var even = [1, 2, 3, 4, 5 ,6 ,7].filter(function(i){ return i % 2 === 0 ;})
console.log(even);

var isalleven = [2, 4,6,5 ].every(function(i){ return i % 2 === 0;})
console.log(isalleven);

var anyof = [1,2,3].some(function(i){ return i % 2 == 0;})
console.log(anyof);

var apple = 'overrated'.split('r');
console.log(apple);

// var af = [4, 5, 6, 7];
// print all the elements of af, dont use for or while :)
// af.forEach(function(i){console.log(i);})

var numbers = [2.4, 3.5, 1.7, 3.3, 1.2];

// create a function that takes an array of numbers,
// it should return a new array that consists only the numbers that are
// bigger than 2 and all of it's elements should be rounded
var fuckingemptylist = [];

function biggerThanTwo(item){
  return item > 2;
}
fuckingemptylist = numbers.filter(biggerThanTwo)
fuckingemptylist = fuckingemptylist.map(function(i){ return Math.round(i)})
console.log(fuckingemptylist);

// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

var teststring = 'javascript is a piece of shit';
var letter = 'x';

function checker(string, character){
  return string.split('').some(function(i){return i === letter;});
}
console.log(checker(teststring, letter));

var numbers = [2, 5, 12, 29];
console.log('');
// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function primeChecker(numlist){

function ifprime(i){
  for (var p = 2; p < i; p++){
    if (i % p == 0){
      return false;
    }
  }
  return true;
}
return numlist.every(ifprime);
}
console.log(primeChecker(numbers));
