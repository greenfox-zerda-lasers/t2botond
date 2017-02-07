function unionStuff(length ){
  length;
  this.array = [];
  i = 0;
  while (length > i){
    this.array.push(i);
    i++;
  }
  this.unite = function (index1, index2){
    this.array[index1] = index2;
    return this.array;
  }
}

var example = new unionStuff(10);
console.log(example.array);
console.log(example.unite(1, 0));
