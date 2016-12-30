'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rocket(cons){
  this.cons = cons;
  this.fuel = 0;
}
Rocket.prototype.fill = function(ammount){
  this.fuel += ammount;
}

Rocket.prototype.launch = function(){
  if(this.fuel > this.cons){
    this.fuel -= this.cons;
    console.log('launched');
  }
  else{
    console.log('No fuel');
  }
}

var falcon = new Rocket(5);

falcon.fill(2);
falcon.launch();
falcon.fill(2);
falcon.launch();
falcon.fill(2);
falcon.launch();
falcon.fill(1);
falcon.launch();
