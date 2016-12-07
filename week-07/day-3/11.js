'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

var Stacks = {

  elements : [],

  push : function(item) {
      Stacks.elements[Stacks.elements.length] = item
    },
  pop : function() {
      Stacks.elements.length = Stacks.elements.length - 1
  },
}
Stacks.push(3);
Stacks.push(5);
Stacks.push(9);
Stacks.push(3);
Stacks.push(5);
Stacks.push(3);
Stacks.push(5);

console.log(Stacks.elements);

Stacks.pop()
Stacks.pop()
Stacks.pop()

console.log(Stacks.elements);
