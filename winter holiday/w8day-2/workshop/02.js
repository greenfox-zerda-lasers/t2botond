// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout
function dela(){
  wrt = setTimeout(function(){
    document.querySelector('#textf').value = 'javascript, I hate it';
  }, 3100)
}
dela();

document.querySelector('#sht').addEventListener('click', function(){
  clearTimeout(wrt);
})
// setinterval clearinterval
