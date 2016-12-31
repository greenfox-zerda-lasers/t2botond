// Add an event listener to the window and display the mouse's x, y coordinates

document.addEventListener('mousemove', function(pos){
  document.querySelector('#x').value = pos.x;
  document.querySelector('#y').value = pos.y;
})
