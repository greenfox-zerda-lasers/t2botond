// Add a click event listener to a <button> and console.log its innerHTML
var text

function Outlogger(){

document.addEventListener('click', function(){
text = document.querySelector('button').innerHTML
document.querySelector('input').value = text
})
}

Outlogger()
