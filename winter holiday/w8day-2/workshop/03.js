var x;
var y;

function logger(){
  setInterval(function(){
    document.querySelector('#x').value = x;
    document.querySelector('#y').value = y;
  },1500)
}

document.addEventListener('mousemove',function(pos){
  x = pos.x;
  y = pos.y;
})

logger();
