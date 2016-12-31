// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)
var y = 0;
var x = 0;

function loc(){
  setTimeout(function(){
    document.querySelector('#x').value = x;
    document.querySelector('#y').value = y;
    loc();
  }, 1599)
}

document.addEventListener('mousemove',function(po){
  x = po.x;
  y = po.y;
})

loc();
