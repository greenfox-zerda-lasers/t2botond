var student = {
  name: 'Darth Wader',
  age: 42,
  isForceSensitive: true
};

// console.log(student.name);
var itemname = 'age';
// console.log(student[itemname]);
// console.log(Object.keys(student));
var students = [
  {name: 'Rezso', age: 9.5, candies: 6},
  {name: 'Gerzson', age: 10, candies: 1},
  {name: 'Aurel', age: 7, candies: 5},
  {name: 'Zsombor', age: 12, candies: 4},
  {name: 'Olaf', age: 12, candies: 7},
  {name: 'Teodor', age: 3, candies: 2}
];


// create a function that counts the students that
// has more than 4 candies
console.log('');

function counter(list){
  return list.filter(function(listitem){
    if(listitem.candies > 4) {
      return listitem.name
    }
  }).length
}
// console.log(counter(students));

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

var st = 'csak megirtam ezt a fost';

function charsel(string){
 var doe = {};
 string.split('').forEach(function(element){
   if (Object.keys(doe).indexOf(element) >= 0) {
     doe[element] += 1;
   }else{
     doe[element] = 1;
   }
 })
 return doe;
 }
 // console.log(charsel(st));

var car = {
  km: 120000,
  ride: function(km){
    this.km += km;
  }
}
car.ride(200);
// console.log(car.km);
// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades
var student = {
  grades: [],
  addGrade: function(grade){
    this.grades[this.grades.length] = grade
  },
  getAv: function(){
    return  this.grades.reduce(function(accu, item){return accu + item}) / this.grades.length
  }
}
student.addGrade(5);
student.addGrade(2);
student.addGrade(4);
student.addGrade(2);
// console.log(student.getAv());

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

var Stack = {
  elementlist: [],
  sizeof: function(){
    return this.elementlist.length
  },
  push: function(newitem){
    this.elementlist[this.elementlist.length] = newitem
  },
  pop: function(){
    var delitem;
    delitem = this.elementlist[this.elementlist.length];
    this.elementlist.length = this.elementlist.length - 1;
  }
}

Stack.push('g'),
Stack.push('4'),
Stack.push('h'),
Stack.push('gadc333'),
console.log(Stack.elementlist);
console.log(Stack.sizeof());
Stack.pop();
console.log(Stack.elementlist);
console.log(Stack.sizeof());
