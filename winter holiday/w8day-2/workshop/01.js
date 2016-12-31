// create a function that when called alerts "I'm delayed" after 1 second

function del(){
  setTimeout(function(){
    console.log("I'm delayed.");
  }, 1000)
}

del();
