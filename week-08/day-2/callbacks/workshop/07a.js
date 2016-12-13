// Embed the following file to a HTML document:
//  - https://www.flickr.com/photos/130463184@N04/15584243094 (use the embed feature)
//  - watch the DOMContentLoaded event also and change the background color of the page to red while the image is loading
//  - add an event to the window object that logs "loaded" the image is downloaded and changes back the background color of the page to white
// DOMContentLoaded ha letrejott az osszes elem ezt a dokumentumra
// load ezt meg windora
// document.bodz.stzle.background.
function Backgroundhandler(){
  document.addEventListener('DOMContentLoaded', function(e){
    document.body.style.backgroundColor = "red"
    })
  window.addEventListener('load', function(e){
    document.body.style.backgroundColor = "white"
  })
}
Backgroundhandler()
