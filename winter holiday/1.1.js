'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

var number = 1;
function e(number){
    switch (number){
      case 1:
        console.log('one');
        break;
      case 2:
        console.log('two');
        break;
      case 3:
        console.log('three');
        break;
      case 4:
        console.log('four');
        break;
      case 5:
        console.log('five');
        break;
      default:
        console.log('javascript is shit');
    }};
e(number);
e(number+1);
e(number+2);
e(number+3);
e(number+4);
e();
