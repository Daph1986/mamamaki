// ---------------------- Side nav, image sliders, collapsible and character counter  -----------------------

// From materialize documentation to initialise with jQuery

$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.slider').slider();
  $('.collapsible').collapsible();
  $('input#japanese_recipe_name, input#english_recipe_name, input#recipe_introduction, input#recipe_preparation_time, input#recipe_servings, input#recipe_ingredients, textarea#recipe_instruction, textarea#recipe_additonal_notes, textarea#recipe_remarks').characterCounter();
});

// ---------------------- Adding an ingredient dynamically  -----------------------

/* 
From https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery 
modified for my own purpose, for adding ingredients and instruction steps
*/

let ingredient = 1;
let max_ingredients = 20;

$(".add_ingredient").click(function (e) {
  e.preventDefault();
  if (ingredient < max_ingredients) {
    ingredient++;
    $(".list_of_ingredients").append(`
    <div class="input-field col s12">
    <i class="fas fa-cookie-bite prefix"></i>
    <input id="recipe_ingredients${ingredient}" name="recipe_ingredients" type="text" data-length="75" 
      minlength="5" maxlength="75" class="validate" required>
    <label for="recipe_ingredients${ingredient}">Ingredient ${ingredient}.</label>
    <a type="button" class="right btn-small btn-red-ingredient remove_ingredient"><i class="fas fa-minus"></i> Remove ingredient</a></div>`);
  }
});


$("main").on('click', ".remove_ingredient", function () {
  $(this).parent('div').remove();
  ingredient--;
});

// ---------------------- Adding a step dynamically  -----------------------

let instruction_step = 1;
let max_instruction_steps = 20;

$(".add_instruction_step").click(function (e) {
  e.preventDefault();
  if (instruction_step < max_instruction_steps) {
    instruction_step++;
    $(".list_of_instruction_steps").append(`
    <div class="input-field col s12">
    <i class="fas fa-utensil-spoon prefix"></i>
    <input id="recipe_instruction${instruction_step}" name="recipe_instruction" type="text" data-length="100" 
      minlength="5" maxlength="100" class="validate" required>
    <label for="recipe_instruction${instruction_step}">Instruction step ${instruction_step}.</label>
    <a type="button" class="right btn-small btn-red-ingredient remove_instruction_step"><i class="fas fa-minus"></i> Remove instruction step</a></div>`);
  }
});


$("main").on('click', ".remove_instruction_step", function () {
  $(this).parent('div').remove();
  instruction_step--;
});