:open_file_folder: Table of Contents
======

**<details><summary>Manual testing</summary>**
* [**_User stories_**](#user-stories)
</details>

**<details><summary>Code check</summary>**
* [**_HTML_**](#html)
* [**_CSS_**](#css)
* [**_JavaScript_**](#javascript)
* [**_Python_**](#python)
* [**_Lighthouse_**](#lighthouse)
* [**_GTmetrix_**](#gtmetrix)
* [**_Color blindness_**](#color-blindness)
* [**_Other tests_**](#other-tests)
</details>

**<details><summary>Bugs</summary>**
* [**_Background_**](#background)
* [**_Mobile nav_**](#mobile-nav)
* [**_Flash messages_**](#flash-messages)
* [**_Logo in sidenav_**](#logo-in-sidenav)
* [**_Safari button bug_**](#safari-button-bug)
* [**_Multiple cards in one card bug_**](#multiple-cards-in-one-card-bug)
</details>

<div align="right"><a href="#top">🔝</a></div>

:construction_worker_woman: :construction_worker_man: Manual testing
======

### User stories

The design goal is to make a clear, accessible, structured site so that visitors can easily read the displayed recipes, make an account and add, edit and delete their own recipes. <br>
To test the goals screen records of an OnePlus Nord were made.<br>
NOTE: the grey overlay in some caption on the footer are displayed because the end of the screen was captured, when just looking on the device this is not visible. So this is just the screen records issue of the phone not a site issue!!!<br><br>
On small devices the menu can be accesed through the hamburger menu, on large devices the sidenav is always visible. There is a difference between the menu for an user who is not logged in and an user who is logged in.<br>
<img src="../testing/testing_images/screen_record_navigation_menu.png" alt="Navigation menu logged out user" width="30%" height="30%"> <img src="../testing/testing_images/screen_record_menu_logged_in_user.png" alt="Navigation menu logged in user" width="30%" height="30%">

#### The visitor goals are:
- To be able to see different recipes and search for them using keywords.<br>
When you navigate to `recipes` you will see a search option and a list with recipe cards.<br> 
<img src="../testing/testing_images/extended_screen_record_recipes_page_1.png" alt="Recipes page 1" width="25%" height="25%"> <img src="../testing/testing_images/extended_screen_record_recipes_page_2.png" alt="Recipes page 2" width="25%" height="25%"> <br>
In the example underneath, the `search` keyword used is pork and the results for the search will be displayed, in this case two recipes.<br>
<img src="../testing/testing_images/screen_record_search.png" alt="Search" width="25%" height="25%">
<img src="../testing/testing_images/extended_screen_record_search_result.png" alt="Search result" width="25%" height="25%"> 

<div align="right"><a href="#top">🔝</a></div>

- To create an account and log in on that account.<br>
To register navigate to `Register` in the menu.<br>
<img src="../testing/testing_images/screen_record_register_page_1.png" alt="Register 1" width="25%" height="25%">
<img src="../testing/testing_images/screen_record_register_page_2.png" alt="Register 2" width="25%" height="25%"><br>
Fill in an `Username` and `Password` end hit `Register`. If the is a not yet excisting user it will successfully register the account<br>
<img src="../testing/testing_images/screen_record_successfully_registered_1.png" alt="Registered successfully 1" width="25%" height="25%"> <img src="../testing/testing_images/screen_record_successfully_registered_2.png" alt="Registered successfully 2" width="25%" height="25%"><br>
If the username is already used it will give an error message. When the characters used are not in range of what is required it will also give error messages, however since I used a phone with langues set to Dutch as a primary language this will be displayed in Dutch.<br>
<img src="../testing/testing_images/screen_record_error_username.png" alt="Username unavailable" width="25%" height="25%">
<img src="../testing/testing_images/screen_record_error_username_and_password_1.png" alt="Register error 1" width="25%" height="25%"> <img src="../testing/testing_images/screen_record_error_username_and_password_2.png" alt="Register error 2" width="25%" height="25%"> <img src="../testing/testing_images/screen_record_error_username_and_password_3.png" alt="Register error 3" width="25%" height="25%"><br>
The same will aply when you navigat to `Log in` and try to log in with an excisting account. It will log you in or give an error message if the username and / or password is not correct:<br>
<img src="../testing/testing_images/screen_record_log_in_1.png" alt="Log in 1" width="25%" height="25%"> <img src="../testing/testing_images/screen_record_log_in_2.png" alt="Log in 2" width="25%" height="25%"> <img src="../testing/testing_images/screen_record_log_in_with_wrong_username_and_or_password.png" alt="Log in wrong" width="25%" height="25%"><br>
Alternatively you can navigate to `Register` and `Log in` through the `Home` page:<br>
<img src="../testing/testing_images/screen_record_alternative_registration_option_1.png" alt="Alternative registration option 1" width="25%" height="25%"><br>
Or navigate to `Register` through the `About` page:<br>
<img src="../testing/testing_images/screen_record_alternative_registration_option_2.png" alt="Alternative registration option 2" width="25%" height="25%">

<div align="right"><a href="#top">🔝</a></div>

- To create, read, update and delete my own recipes.<br>
To create a recipe, make sure you are logged in, if not, navigate to `Log in` and log in to your account. If you don't have an account, navigate to `Register` and register an account. Once logged in navigate to `Add recipe`, there you can fill out the form.<br>
<img src="../testing/testing_images/extended_screen_record_add_recipe_1.png" alt="Add recipie 1" width="25%" height="25%"><br>
Fill out the form and hit  `Add recipe`.<br>
<img src="../testing/testing_images/screen_record_add_recipe_2.png" alt="Add recipie 2" width="25%" height="25%"> <img src="../testing/testing_images/screen_record_add_recipe_3.png" alt="Add recipie 3" width="25%" height="25%"><br>
To read the recipe navigate to `Recipes` in the menu, pick a recipe and hit `Go to recipe`, there you'll see the full recipe.<br>
<img src="../testing/testing_images/extended_screen_record_full_recipe_1.png" alt="Full recipie 1" width="25%" height="25%"> <img src="../testing/testing_images/extended_screen_record_full_recipe_2.png" alt="Full recipie 2" width="25%" height="25%"><br>
To edit / update the recipe hit  `Edit recipe`<br>
<img src="../testing/testing_images/screen_record_recipe_options_logged_in_user.png" alt="Recipe options" width="25%" height="25%"><br>
and change what you want to edit in the recipe, then hit  `Save edited recipe`<br>
<img src="../testing/testing_images/extended_screen_record_edit_recipe.png" alt="Edit recipe" width="25%" height="25%"> <img src="../testing/testing_images/screen_record_updated_successfully.png" alt="Recipe updated successfully" width="25%" height="25%"><br>
To delete a recipe hit `Delete recipe`, you will see a message with the question if you are sure you want to delete it.<br>
<img src="../testing/testing_images/screen_record_delete_recipe.png" alt="Delete recipe" width="25%" height="25%"><br>
If you are sure hit `YES,DELETE!` and the recipe will be deleted.<br>
<img src="../testing/testing_images/screen_record_delete_recipe_success.png" alt="Recipe deleted successfully" width="25%" height="25%"><br>

<div align="right"><a href="#top">🔝</a></div>

#### The site owners goals are:

- To share the love for Japanese home cooking and promote it.<br>
The love for Japanese home cooking is explained on the about page, to read it navigate to `About`.
<img src="../testing/testing_images/extended_screen_record_about_page.png" alt="About page" width="25%" height="25%">

<div align="right"><a href="#top">🔝</a></div>

- Share nice Japanese home cooking recipes.<br>
This is shown through the recipes page were all the shared recipes can be found. Navigate to `Recipes` to read them.<br>
<img src="../testing/testing_images/extended_screen_record_recipes_page_1.png" alt="Recipes page 1" width="25%" height="25%"> <img src="../testing/testing_images/extended_screen_record_recipes_page_2.png" alt="Recipes page 2" width="25%" height="25%"> <br><br>

It can be concluded that all goals have been achieved. <br>

The project has been tested on the available DevTools for phone and tablet sizes as well as on multiple responsive sizes and it was made sure that it looks good and works well on all. It was also tested on multiple devices among others an OnePlus Nord, an iMac (Retina 5K, 27-inch, 2017), a MacBook-Air (Retina M1, 13.3-inch, 2020) and a Samsung Galaxy Tab4 (10.1-inch 2014), everything works as it should.

<div align="right"><a href="#top">🔝</a></div>

![HTML5](https://img.shields.io/badge/HTML5%20-%23E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=FFFFFF)
======
### HTML

The HTML code of all pages was tested with a [HTML](https://validator.w3.org/nu/?doc=http%3A%2F%2Fmamamaki.herokuapp.com%2F) validator.<br>
<img src="../testing/testing_images/html_check_homepage.png" alt="HTML check homepage" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_about_page.png" alt="HTML check about page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_recipes_page.png" alt="HTML check recipes page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_personal_recipe_page.png" alt="HTML check personal recipe page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_add_recipe_page.png" alt="HTML check add recipe page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_update_recipe_page.png" alt="HTML check edit recipe page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_log_in_page.png" alt="HTML check log in page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_register_page.png" alt="HTML check register page" width="55%" height="55%"> <br>
No errors or warnings were found. 

<div align="right"><a href="#top">🔝</a></div>

![CSS3](https://img.shields.io/badge/CSS3%20-%231572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=FFFFFF)
======

### CSS

The CSS code was tested with a [CSS](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) validator. <br>
<img src="../testing/testing_images/css_check_1.png" alt="CSS check" width="55%" height="55%"> <img src="../testing/testing_images/css_check_2.png" alt="CSS check" width="55%" height="55%"> <br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way.

<div align="right"><a href="#top">🔝</a></div>

![JavaScript](https://img.shields.io/badge/JavaScript%20-%23323330.svg?&style=for-the-badge&logo=JavaScript&logoColor=F7DF1E)
======

### JavaScript

The JavaScript code was tested with a [JavaScript](https://jshint.com/) linter. <br>
<img src="../testing/testing_images/js_check_1.png" alt="JS check 1" width="45%" height="45%">
<img src="../testing/testing_images/js_check_2.png" alt="JS check 2" width="45%" height="45%"><br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way.

<div align="right"><a href="#top">🔝</a></div>

![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
======

### Python

The Python code was tested with a [PEP8](http://pep8online.com/) linter. <br>
<img src="../testing/testing_images/python_check.png" alt="Python check" width="55%" height="55%"><br>
No errors or warnings were found.

<div align="right"><a href="#top">🔝</a></div>

:traffic_light: Lighthouse
======

### Lighthouse

All pages have passed through Lighthouse in Chrome DevTools, the results for desktop can found here: <br>
<img src="../testing/testing_images/home_desktop.png" alt="Lighthouse desktop home" width="25%" height="25%"> <img src="../testing/testing_images/about_desktop.png" alt="Lighthouse desktop about" width="25%" height="25%"> <img src="../testing/testing_images/recipes_desktop.png" alt="Lighthouse desktop recipes" width="25%" height="25%"> <img src="../testing/testing_images/register_desktop.png" alt="Lighthouse desktop register" width="25%" height="25%"> <img src="../testing/testing_images/log_in_desktop.png" alt="Lighthouse desktop log in" width="25%" height="25%"> <img src="../testing/testing_images/personal_recipe_page_desktop.png" alt="Lighthouse desktop personal recipe page" width="25%" height="25%"> <img src="../testing/testing_images/add_recipe_desktop.png" alt="Lighthouse desktop add recipe" width="25%" height="25%"> <img src="../testing/testing_images/edit_recipe_desktop.png" alt="Lighthouse desktop edit recipe" width="25%" height="25%"><br>
and these are the results for the mobile versions:<br>
<img src="../testing/testing_images/home_mobile.png" alt="Lighthouse mobile home" width="25%" height="25%"> <img src="../testing/testing_images/about_mobile.png" alt="Lighthouse mobile about" width="25%" height="25%"> <img src="../testing/testing_images/recipes_mobile.png" alt="Lighthouse mobile recipes" width="25%" height="25%"> <img src="../testing/testing_images/register_mobile.png" alt="Lighthouse mobile register" width="25%" height="25%"> <img src="../testing/testing_images/login_mobile.png" alt="Lighthouse mobile log in" width="25%" height="25%"> <img src="../testing/testing_images/personal_recipe_page_mobile.png" alt="Lighthouse mobile personal recipe page" width="25%" height="25%"> <img src="../testing/testing_images/add_recipe_mobile.png" alt="Lighthouse mobile add recipe" width="25%" height="25%"> <img src="../testing/testing_images/edit_recipe_mobile.png" alt="Lighthouse mobile edit recipe" width="25%" height="25%"><br>
The results of the Lighthouse tests are satisfactory, so no adjustments are needed at this time. But in the future a way to increase the performance on some pages would be something to do in an update.

<div align="right"><a href="#top">🔝</a></div>

:bar_chart: GTmetrix
====== 

### GTmetrix

The site was tested with [GTmetrix](https://gtmetrix.com/). The reports can be found here:<br>
[Homepage](https://gtmetrix.com/reports/mamamaki.herokuapp.com/s5oaEEkc/) <br>
[About page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/ORtp6cCU/) <br>
[Recipes page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/jJydxJtH/) <br>
[Single recipe page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/bZ5vU616/) <br>
[Register page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/D9zcldQf/) <br>
[Log in page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/w7caPZIA/) <br>
[Personal recipe page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/ilAC1S1D/) <br>
[Add recipe](https://gtmetrix.com/reports/mamamaki.herokuapp.com/N1BFTHGb/) <br>
[Edit recipe](https://gtmetrix.com/reports/mamamaki.herokuapp.com/UMcBCkEe/) <br>


<div align="right"><a href="#top">🔝</a></div>

:eyeglasses: Color blindness
======

### Color blindness

Color blindness was tested on this [site](https://www.toptal.com/designers/colorfilter/) to ensure you would still be able to read the website when you have different types of color blindness. Here you will find the links of the homepage tests, but of course all pages were tested. <br>
[Protanopia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=protan) <br>
[Deutanopia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=deutan) <br>
[Tritanopia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=tritan) <br>
[Greyscale / Achromatopsia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=grey)

<div align="right"><a href="#top">🔝</a></div>

:test_tube: Other tests
======

### Other tests

A lot of different people were asked to check the project to ensure it works on different systems and devices. The website was tested on Samsung Galaxy TabA (10.1-inch 2019), OnePlus 5, Xiaomi Redmi Note 7, Xiaomi Redmi Note 8 Pro, Motorola G9, Motorola G5 and iPhone 12 Pro Max among others. It has been tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. During the testing two bugs were found and fixed, the Safari button bug and the Multiple cards in one card bug, please see the Bugs section and matching issue link for these bugs and their fix.
<br>
The contact form of the home page has also been tested on Google Chrome, Safari, Microsoft Edge and Mozilla Firefox, this works as it should.<br>
<img src="../testing/testing_images/emailjs_test.png" alt="EmaiJS test" width="55%" height="55%">

<!-- #### Advices given after testing which were followed

1. Some spelling and grammar changes have been made after reviews from my husband, brother-in-law and sister-in-law.
2. My husband, Django, did not think the user-friendliness was good enough, because only the logo could be used to return to the homepage. That is why on the page for requesting the sample kit and for designing the business card, 2 buttons have been added at the top to switch between the other pages. Cancel buttons have also been added to the bottom of the forms. This increases user-friendliness. -->

<div align="right"><a href="#top">🔝</a></div>

:bug: Bugs
======

The bugs are listed below, with a link to the issue item where they are further explained. I was able to solve all of them.

### Background
[Full size background bug](https://github.com/Daph1986/mamamaki/issues/26)

### Mobile nav
[Mobile navigation bug](https://github.com/Daph1986/mamamaki/issues/27)

### Flash messages
[Flash messages bug](https://github.com/Daph1986/mamamaki/issues/28)

### Logo in sidenav
[The sidenav logo bug](https://github.com/Daph1986/mamamaki/issues/29)

### Safari button bug
[Safari button bug](https://github.com/Daph1986/mamamaki/issues/30)

### Multiple cards in one card bug
[Multiple cards in one card bug](https://github.com/Daph1986/mamamaki/issues/31)

<div align="right"><a href="#top">🔝</a></div>
