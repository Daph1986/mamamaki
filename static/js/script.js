// ---------------------- Side nav -----------------------

// From materialize documentation to initialise

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init();
});

$(document).ready(function(){
  $('.sidenav').sidenav();
});
       