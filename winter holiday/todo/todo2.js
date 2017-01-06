function getToDos(){
  var ddd = new XMLHttpRequest();
  ddd.open('GET','https://mysterious-dusk-8248.herokuapp.com/todos');
  ddd.send();
  ddd.onreadystatechange = ready;

  function ready(){
    if(ddd.readyState === XMLHttpRequest.DONE){
      var todolist = JSON.parse(ddd.response);
console.log(todolist);
    document.querySelector('button').addEventListener('click', function(){
      add();
    })
        todolist.forEach(function(e){

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
                  // var r = confirm("Are you sure to delete this item?")
                  // if (r == true){
                    deletetask(deletid);
                    this.parentNode.parentNode.parentNode.remove()
                  // }
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
        }}}
        function deletetask(id){
              var pr = new XMLHttpRequest();
              pr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/'+ id);
              pr.send()
        }
        function changetaskstate(item){
          var ke = new XMLHttpRequest();
          ke.open('PUT','https://mysterious-dusk-8248.herokuapp.com/todos/'+ item.id);
          ke.setRequestHeader('Content-Type','application/json');
          ke.send(JSON.stringify({
              completed: item.completed,
              text: item.text
          }))
        }
        function add(){
          var keg = new XMLHttpRequest();
          keg.open('POST','https://mysterious-dusk-8248.herokuapp.com/todos/');
          keg.setRequestHeader('Content-Type','application/json');
          keg.send(JSON.stringify({
              text: document.querySelector('input').value
          }))
        }

getToDos();
