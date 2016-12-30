// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function F16(){
  this.ammo = 0;
  this.base_dammage = 30;
  this.all_dammage = 0;
}
function F35(){
  this.ammo = 0;
  this.base_dammage = 50;
  this.all_dammage = 0;
}

F16.prototype.refill = function(qty){
  this.ammo += qty;
  this.all_dammage = this.ammo * this.base_dammage;
  if(this.ammo > 8){
    ret = this.ammo - 8;
    this.ammo = 8;
    this.all_dammage = this.ammo * this.base_dammage;
    return ret;
  }
  else{
    return 0;
  }
}

F35.prototype.refill = function(qty){
  this.ammo += qty;
  this.all_dammage = this.ammo * this.base_dammage;
  if(this.ammo > 12){
    ret = this.ammo - 12;
    this.ammo = 12;
    this.all_dammage = this.ammo * this.base_dammage;
    return ret;
  }
  else{
    return 0;
  }
}

F16.prototype.fight = function(){
  var fightresult = this.ammo * this.base_dammage;
  this.ammo = 0;
  return fightresult
}

F35.prototype.fight = function(){
  var fightresult = this.ammo * this.base_dammage;
  this.ammo = 0;
  return fightresult;
}

function Carrier(ammo){
  this.ammo = ammo;
  this.health = 3000;
  this.aircraftlist = [];
  this.dammage = 0
}

Carrier.prototype.addAircraft = function(plane){
  this.aircraftlist.push(plane);
}

Carrier.prototype.status_report = function(){
  console.log('Aircraft number: ' + this.aircraftlist.length + ' Ammo storage: ' + this.ammo + ' Total dammage: ' + this.dammage + ' Health: ' + this.health);
  console.log('Aircrafts: ');
  this.aircraftlist.forEach(function(plane){
    console.log('Type: ' + plane.constructor.name + ' Ammo: ' + plane.ammo + ' Base dammage: ' + plane.base_dammage + ' All dammage: ' + plane.all_dammage);
  })
}
Carrier.prototype.refill = function(){
  this.aircraftlist.forEach(function(plane){
    carr.ammo = plane.refill(carr.ammo);
  })
}
Carrier.prototype.fight = function(){
  this.aircraftlist.forEach(function(plane){
    carr.dammage += plane.fight();
    carr.health = 3000-carr.dammage;
  })
}

var first = new F16;
var second = new F35;
console.log(first.refill(61));
console.log(first.fight());
console.log(second.refill(62));
console.log(second.fight());
var carr = new Carrier(5);
carr.addAircraft(first);
carr.addAircraft(second);
carr.status_report();
carr.refill();
carr.status_report();
carr.fight();
carr.status_report();
