
$(document).ready(function() {
  $('#akeno').on('click', function() {
    var colorx = [{"border": "2px black solid"}, {"border": "2px pink solid"}, {"border": "2px grey solid"}, {"border": "2px white solid"}];
    var i = Math.floor(Math.random() * colorx.length)
    $(this).css(colorx[i]);
  });
  
  $('.typed-out').on('animationend webkitAnimationEnd', function() { 
    $(".typed-out1").show();
  });
});