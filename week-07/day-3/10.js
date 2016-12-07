'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {

  grades: [],

  addgrade:
    function(mark){
      student.grades.push(mark)

    },
  getaverage:
    function(){
      return  student.grades.reduce(function(acc, item) {
        return acc + item
      }, 0) / student.grades.length
    }
}
student.addgrade(1)
student.addgrade(2)
student.addgrade(3)
student.addgrade(2)
student.addgrade(5)

console.log(student.grades);
console.log(student.getaverage());
