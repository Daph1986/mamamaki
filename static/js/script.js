// ---------------------- Side nav, image sliders and character counter  -----------------------

// From materialize documentation to initialise with jQuery

$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.slider').slider();
  $('input#japanese_recipe_name, input#english_recipe_name, textarea#recipe_introduction, input#recipe_preparation_time, input#recipe_servings, input#recipe_ingredients, textarea#recipe_instruction').characterCounter();
});
