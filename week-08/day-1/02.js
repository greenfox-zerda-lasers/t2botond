'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference
function Rectangle(a, b) {
  this.a = a;
  this.b = b;
}

Rectangle.prototype.getArea = function(a, b) {
 this.area = this.a * this.b;
 console.log(this.area)
}

Rectangle.prototype.getCircumference = function(a, b) {
 this.circumference = 2 * this.a + 2 * this.b;
 console.log(this.circumference)
}


var square = new Rectangle(1, 10);
square.getArea();
square.getCircumference();
// console.log(volvo.km); // 80120
