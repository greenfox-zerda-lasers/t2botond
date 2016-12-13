// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call
var x
var y

function Locator(){
  setInterval(function() {
    document.getElementById('x').value = x
    document.getElementById('y').value = y
    console.log(x, y)
  }, 1500)
}
Locator()
document.addEventListener('mousemove',function(e) {
  x = e.x
  y = e.y})
