var request = new XMLHttpRequest();

request.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
request.send();
request.onreadystatechange = ready;


function displayrow(text) {
  console.log(text)
}
function ready(){

  if (request.readyState === XMLHttpRequest.DONE){
    var linkdata = JSON.parse(request.response);
    // displayrow(linkdata)
    linkdata.forEach(function(e){

    var line = document.createElement('li')
    var linecontent = document.createElement('div')
    var linetext = document.createElement('p')
    var innercont = document.createElement('div')
    innercont.className = "icons"
    var listrow = document.createElement('div')
    listrow.className = "listrow"
    var img1 = document.createElement('img')
    var img2 = document.createElement('img')

    linetext.innerHTML = e.text

    img1.setAttribute('src','bin.png')
    img1.addEventListener('click', function(e){
      deletetask();
    })

    if(e.completed === false){
      img2.setAttribute('src','unchecked.png')
    }else{
      img2.setAttribute('src','checked.jpg')
    }
    img2.addEventListener('click',function(){
      changetaskstate();
    })

    // createelement img
    innercont.appendChild(img1)
    innercont.appendChild(img2)
    listrow.appendChild(linetext)
    listrow.appendChild(innercont)
    line.appendChild(listrow)
    document.querySelector('ul').appendChild(line)
  })
}
}

function changetaskstate(e){
  console.log("Wanna change state")
}
function deletetask(e){
  console.log("Wanna delete")
}