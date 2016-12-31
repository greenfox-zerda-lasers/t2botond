// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk
function distance(dis){
  var dislist = [];
  for (var i = 0; i < dis; i++){
    dislist.push(false)
  }
  return dislist;
}

function walk(list){
  var newlist = list;
for(var i = 0; i < list.length; i++){
  newlist[i] = true;
}
return newlist;
}

function tour(first, second){
  return first(second);
}

console.log(tour(walk, distance(10)));
