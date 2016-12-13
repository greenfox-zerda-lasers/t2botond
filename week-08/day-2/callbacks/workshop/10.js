// Create a circle with 100px diameter (use border radius)
//  - Make it move from left to right edge
//  - use requestAnimationFrame
var requestAnimationFrame = window.requestAnimationFrame ||
                            window.mozRequestAnimationFrame ||
                            window.webkitRequestAnimationFrame ||
                            window.msRequestAnimationFrame;

function animateCircle(){
  circle.x++;

  window.requestAnimationFrame(animateCircle);
}
 animateCircle()
