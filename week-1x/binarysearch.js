function binarySearch(){
var variables = [1,
                  2,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  11,
                  12,
                  13,
                  14,
                  15,
                  16];

  var i = 12;
  var x = variables[parseInt(variables.length/2)];
  while (i !== x){
    var index = parseInt(variables.indexOf(x));
    if(i<x){
      x--;
    }else if (i>x) {
      x++;
    }
  }
     return console.log(variables.indexOf(x));
}

binarySearch();
