// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout
var illegal

function ThreeSecDelay() {
  illegal = setTimeout(function(){
    document.querySelector('input').value = "Time over"
  }, 3000)

}

ThreeSecDelay()
var button = document.querySelector('button');
  button.addEventListener('click', function(){
    clearTimeout(illegal)
  });

// setinterval clearinterval
