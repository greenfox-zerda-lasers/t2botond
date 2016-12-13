'use strict'

 var list = ['url(traktor2.jpg)',
            'url(traktor3.jpg)',
            'url(traktor4.jpg)',
            'url(traktor5.jpg)',
            'url(traktor6.jpg)']

var listindex = 0

var buttonhandler = document.querySelector('#left')
    buttonhandler.addEventListener('click', function(e){
    var picture = document.querySelector('#mainbody')
    listindex--;
    console.log(listindex)
    if (listindex == -1){
      listindex = 4
    }
    picture.style.backgroundImage =  list[listindex]
    console.log(list[listindex]);
 })

 var buttonhandler = document.querySelector('#right')
     buttonhandler.addEventListener('click', function(e){
     var picture = document.querySelector('#mainbody')
     listindex++;
     console.log(listindex)
     if (listindex == 5){
       listindex = 0
     }
     picture.style.backgroundImage =  list[listindex]
     console.log(list[listindex]);
  })
