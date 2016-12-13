// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)
var x
var y

function Locator(){
  setTimeout(function() {
    document.getElementById('x').value = x
    document.getElementById('y').value = y
    // console.log(x, y)
    Locator()
  }, 1500)
}
Locator()
document.addEventListener('mousemove',function(e) {
  x = e.x
  y = e.y})
