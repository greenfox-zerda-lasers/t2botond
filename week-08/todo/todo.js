function getToDos() {
    var request = new XMLHttpRequest();

    request.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
    request.send();
    request.onreadystatechange = ready;


    function ready() {

        if (request.readyState === XMLHttpRequest.DONE) {
            var linkdata = JSON.parse(request.response);
            // displayrow(linkdata)
            linkdata.forEach(function(e) {

                var line = document.createElement('li')
                var linecontent = document.createElement('div')
                var linetext = document.createElement('p')
                var innercont = document.createElement('div')
                innercont.className = "icons"
                var listrow = document.createElement('div')
                listrow.className = "listrow"
                var img1 = document.createElement('img')
                var img2 = document.createElement('img')
                img1.setAttribute('id', e.id)
                var deletid = e.id

                linetext.innerHTML = e.text

                img1.setAttribute('src', 'bin.png')
                img1.addEventListener('click', function(e) {
                  var r = confirm("Are you sure to delete this item?")
                  if (r == true){
                    deletetask(deletid);
                    this.parentNode.parentNode.parentNode.remove()
                  }
                })

                if (e.completed === false) {
                    img2.setAttribute('src', 'unchecked.png')
                    img2.dataset.unchecked = 'true'
                } else {
                    img2.setAttribute('src', 'checked.jpg')
                    img2.dataset.unchecked = 'false'
                }
                img2.addEventListener('click', function() {
                    e.completed = !e.completed
                    changetaskstate(e);
                    if (this.dataset.unchecked == "true") {
                        this.dataset.unchecked = "false"
                        this.setAttribute('src', 'checked.jpg')
                    } else {
                        this.dataset.unchecked = "true"
                        this.setAttribute('src','unchecked.png')
                    }
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
}


function changetaskstate(e) {
    console.log(e)
    var request = new XMLHttpRequest();
    request.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + e.id);
    request.setRequestHeader("Content-Type", "application/json")
    request.send(JSON.stringify({
        text: e.text,
        completed: e.completed
    }));
}

function deletetask(e) {
    console.log("Wanna delete")
    var request = new XMLHttpRequest();
    request.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + e);
    request.send();
}

function postDatas() {
    var inputtext = document.querySelector('input').value
        // console.dir(value);
    var request = new XMLHttpRequest();
    request.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
    request.setRequestHeader("Content-Type", "application/json")
    request.send(JSON.stringify({
        text: inputtext
    }));
    document.querySelector('input').value = ''
}
var addbutton = document.querySelector("button")
addbutton.addEventListener('click', postDatas)

getToDos()
