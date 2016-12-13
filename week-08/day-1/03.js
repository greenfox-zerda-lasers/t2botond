'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rockets(consumption) {
  this.consumption = consumption;
  }

Rockets.prototype.Fill = function(ammount) {
  this.fill = ammount;
}

Rockets.prototype.Launch = function()  {
  if (this.fill > this.consumption) {
    console.log('launched')
  }
  else {
    console.log('not launched');

  }
}
var rocket1 = new Rockets(10);
var rocket2 = new Rockets(10);
var rocket3 = new Rockets(20);

rocket1.Fill(51)
rocket2.Fill(1)
rocket3.Fill(25)

rocket1.Launch()
rocket2.Launch()
rocket3.Launch()
