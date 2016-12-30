'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says
function Animal(noise){
  this.sound = noise;
}

Animal.prototype.say = function(){
  console.log(this.sound);
}

var c = new Animal('huuu');
c.say();
