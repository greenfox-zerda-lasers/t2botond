'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says
function Animal(sound) {
 this.sound = sound;
}

Animal.prototype.says = function(sound) {
 console.log(this.sound);
}

var cat = new Animal('meow');
cat.says();
// console.log(volvo.km); // 80120
