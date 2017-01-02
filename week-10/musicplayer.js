var listitems = document.querySelectorAll('li')

listitems.forEach(function(item){
  item.addEventListener('click',function(){
    var newsource = item.getAttribute('data-src');
    document.querySelector('audio').setAttribute('src',newsource);
  })
})
