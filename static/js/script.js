$( document ).ready(function() {

  console.log("bllalh");

  $('#talk-to-dude').on('click', function(evt) {
    
    evt.preventDefault();
    alert("talking");

  });
});