// ---------------------- Side nav, image sliders, collapsible and character counter  -----------------------

// From materialize documentation to initialise with jQuery

$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.slider').slider();
  $('.collapsible').collapsible();
  $('input#japanese_recipe_name, input#english_recipe_name, textarea#recipe_introduction, input#recipe_preparation_time, input#recipe_servings, input#recipe_ingredients, textarea#recipe_instruction').characterCounter();
});


var coll = document.getElementsByClassName("collapsibles");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}