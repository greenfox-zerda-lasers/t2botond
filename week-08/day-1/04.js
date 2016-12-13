// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake
function Aircraft(type) {
  this.type = type;
  this.ammo = 0;
  if (this.type == "F35") {
    this.base_dammage = 50
}
  if (this.type == "F16") {
    this.base_dammage = 30
}
  this.all_dammage = 0
}


Aircraft.prototype.status_report = function() {
  console.log(" Type: " + this.type + "," + " Ammo: " + this.ammo + "," + " Base Damage: " + this.base_dammage + "," + " All Damage: " + this.all_dammage + ",")
}

Aircraft.prototype.fight = function(){
  total_ammount = this.ammo * this.base_dammage
  this.ammot = 0
  return total_ammount
}

Aircraft.prototype.refill = function(ammount){
  if (this.type == "F16") {
    if (this.ammo + ammount > 8 ) {
      this.ammo = 8
      return -(this.ammo - ammount)
    }
    else {
      this.ammo += ammount
  }
}
  if (this.type == "F35") {
    if (this.ammo + ammount > 12 ) {
      this.ammo = 12
      return -(this.ammo - ammount)
    }
    else {
      this.ammo += ammount
    }
  }
  this.all_dammage = this.ammo * this.base_dammage
}

var plane1 = new Aircraft("F16");
var plane2 = new Aircraft("F35");

console.log(plane1.ammo);
console.log(plane2.ammo);
console.log(plane1.refill(83));
console.log(plane2.refill(19));
console.log(plane1.ammo);
console.log(plane2.ammo);
plane1.status_report()
plane2.status_report()
console.log(plane1.fight())
