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
