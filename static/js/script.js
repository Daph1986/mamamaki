// ------------- Function to bind character counter parts -------------

function bindCharacterCounter() {
  $('input#japanese_recipe_name').characterCounter();
  $('input#english_recipe_name').characterCounter();
  $('textarea#recipe_introduction').characterCounter();
  $('input#recipe_ingredients').characterCounter();
  $('input#recipe_instruction').characterCounter();
  $('textarea#recipe_additional_notes').characterCounter();
  $('textarea#recipe_remarks').characterCounter();
  $('textarea#message').characterCounter();
}

// ---------------- Media query for image slider hight ----------------

const sreenWidth = window.matchMedia('(min-width: 1025px)');

function sliderHeight() {
  if (sreenWidth.matches) {
    $('.slider').slider({ height: 650, });
  }
  else {
    $('.slider').slider({ height: 450, });
  }
}

// -------------------------- Initialization --------------------------

/*
Initialization for side nav, image sliders, character counter in forms
and fade out function for flashes with jQuery partially
from materialize documentation.
*/

$(document).ready(function () {
  $('.sidenav').sidenav();
  sliderHeight();
  $('.modal').modal();
  bindCharacterCounter();
  setTimeout(function () {
    $('.flashes').fadeOut('slow');
  }, 3000);
});

// ---------------------- Validation for EmailJS ----------------------

document.onload = function () {
  emailjs.init({
    publicKey: "pcWHehpZJoTD7Vm0p",
  });
}();

// ---------------------------- Mail form -----------------------------

function sendMail(mailForm) {
  console.log("Form submitted");

  emailjs.send("service_4cgsgib", "send_contact_mail", {
    "from_name": mailForm.name.value,
    "from_email": mailForm.email.value,
    "message": mailForm.message.value,
  })
  .then(function (response) {
    console.log("Email sent successfully:", response);
    M.toast({ html: 'Thank you, your message has been sent successfully!', displayLength: '3000' });
    window.setTimeout(function () {
      location.reload();
    }, 4000);
  })
  .catch(function (error) {
    console.error("Error sending email:", error);
    M.toast({ html: 'Sorry, something went wrong :-(', displayLength: '3000' });
  });

  return false; // Voorkomt dat het formulier normaal gesubmit wordt
}


// ----------------- Dynamically adding an ingredient -----------------

let ingredient = 1;
let max_ingredients = 20;

$(".add_ingredient").click(function (e) {
  e.preventDefault();
  if (ingredient < max_ingredients) {
    ingredient++;
    $(".list_of_ingredients").append(`
    <div class="input-field col s12">
    <i class="fas fa-cookie-bite prefix"></i>
    <input id="recipe_ingredients${ingredient}" name="recipe_ingredients" type="text" data-length="150" 
      minlength="2" maxlength="150" class="validate" required>
    <label for="recipe_ingredients${ingredient}">Ingredient ${ingredient}.</label>
    <a type="button" class="right btn-small btn-red-ingredient remove_ingredient"><i class="fas fa-minus"></i> Remove ingredient</a></div>`);
  }
});

$("main").on('click', ".remove_ingredient", function () {
  $(this).parent('div').remove();
  ingredient--;
});

// -------------------- Dynamically adding a step ---------------------

let instruction_step = 1;
let max_instruction_steps = 20;

$(".add_instruction_step").click(function (e) {
  e.preventDefault();
  if (instruction_step < max_instruction_steps) {
    instruction_step++;
    $(".list_of_instruction_steps").append(`
    <div class="input-field col s12">
    <i class="fas fa-utensil-spoon prefix"></i>
    <input id="recipe_instruction${instruction_step}" name="recipe_instruction" type="text" data-length="500" 
      minlength="5" maxlength="500" class="validate" required>
    <label for="recipe_instruction${instruction_step}">Instruction step ${instruction_step}.</label>
    <a type="button" class="right btn-small btn-red-ingredient remove_instruction_step"><i class="fas fa-minus"></i> Remove instruction step</a></div>`);
  }
});

$("main").on('click', ".remove_instruction_step", function () {
  $(this).parent('div').remove();
  instruction_step--;
});

// ---------- Collapsible ingredients and instructions lists ----------

let list = document.getElementsByClassName("collapsible-list");
let i;

for (i = 0; i < list.length; i++) {
  list[i].addEventListener("click", function () {
    this.classList.toggle("active");
    let content = this.nextElementSibling;
    if (content.style.maxHeight) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}

// ----------------------- Scroll to top button -----------------------

let topbutton = document.getElementById("goToTopBtn");

window.onscroll = function () { scrollPage(); };

function scrollPage() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topbutton.style.display = "block";
  } else {
    topbutton.style.display = "none";
  }
}

function goToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// ----------------------- Current year copyright -----------------------

var currentYear = new Date().getFullYear();
var yearSpan = document.getElementById('currentYear');
yearSpan.textContent = currentYear;