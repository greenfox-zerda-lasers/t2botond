// Add an event listener to the window and display the mouse's x, y coordinates
var xposition
var yposition

function Display(){

  window.addEventListener('mousemove', function(e){
    xposition = e.x
    yposition = e.y

  document.getElementById('xdir').value = xposition
  document.getElementById('ydir').value = yposition
  })
}
Display()
