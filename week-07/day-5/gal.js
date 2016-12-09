

var list=['url(traktor2.jpg)','url(traktor3.jpg)',
'url(traktor4.jpg)','url(traktor5.jpg)','url(traktor6.jpg)']

var [listindex] = 0

var buttonhandler = document.querySelector('#left')
    buttonhandler.addEventListener('click', function(e){
    var picture = document.querySelector('#mainbody')
    picture.style.backgroundImage = list[listindex]
    listindex--;
 })
