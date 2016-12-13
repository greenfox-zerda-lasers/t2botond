// Embed the following file to a HTML document:
//  - From the previous flickr example extract the .jpg link directly
//  - Create an image tag in the with document.createElement
//  - Add a 'load' event to the image and only show the image to the user when the image is loaded
function Imagehandler(){

  var body = document.querySelector('body')
  var image = document.createElement('img')
  image.setAttribute('src', 'https://c7.staticflickr.com/8/7562/15584243094_b268a32192_h.jpg')
  window.addEventListener('load', function(e){
    body.appendChild(image)
  })
}
Imagehandler()
