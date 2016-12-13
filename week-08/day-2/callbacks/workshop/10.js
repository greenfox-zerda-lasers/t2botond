// Create a circle with 100px diameter (use border radius)
//  - Make it move from left to right edge
//  - use requestAnimationFrame
var c=document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.beginPath();
ctx.arc(100,75,50,0,2*Math.PI);
ctx.stroke();
