// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk
function Tour(walker, distancer){
  return distancer.map( walker )
}
function Distance(param){
  var array = []
  for (var i = 0; i < param; i++){
      array.push(false)
  }
  return array
}

function Walk(value){
  return true
}

console.log(Tour(Walk, Distance(25)))
