document.querySelector('.form-icon').addEventListener('change',function(e){
  var fileName = document.getElementById("Icon").files[0].name;
  var nextSibling = e.target.nextElementSibling;
  nextSibling.innerText = fileName;
})

document.querySelector('.form-image').addEventListener('change',function(e){
  var fileName = document.getElementById("Image").files[0].name;
  var nextSibling = e.target.nextElementSibling;
  nextSibling.innerText = fileName;
})