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
</details>

<div align="right"><a href="#top">🔝</a></div>

:construction_worker_woman: :construction_worker_man: Manual testing
======

### User stories

<!-- The design goal is to make a clear, accessible, structured site so that visitors can easily design their own business cards. <br>
When landing on the page there is an explanation on how things work: <br>
<img src="../testing/testing_images/explanation.png" alt="Explanation" width="25%" height="25%"> 
<img src="../testing/testing_images/modal.png" alt="Modal" width="25%" height="25%"> <br>
After reading it the user can either request a sample kit or start designing. When the user clicks the sample kit button they will be taken to a form, this form needs to be filled in to get the address to send the sample kit. <br>
<img src="../testing/testing_images/sample_form1.png" alt="Sample form 1" width="25%" height="25%">
<img src="../testing/testing_images/sample_form2.png" alt="Sample form 3" width="25%" height="25%">
<img src="../testing/testing_images/sample_form3.png" alt="Sample form 3" width="25%" height="25%"> <br> 
After everything is filled out an email is sent to, in this case me, with the data needed to send the sample kit through mail. <br>
<img src="../testing/testing_images/sample_form_emailjs_mail.png" alt="Form emailJS mail" width="40%" height="40%"> <br>
When the user feels ready to start designing they can click the start design button, which will take them to the creator.html page. <br>
<img src="../testing/testing_images/creator_page.png" alt="Creator page" width="25%" height="25%"> <br>
As a visitor there were multiple steps you would like to take, in the manual tests it was checked if these were achieved.
- Choose out of three different sizes of business cards.
- Choose a background color. <br>
This can be done in step 1 and 2.<br>
<img src="../testing/testing_images/step1_2.png" alt="Step 1 & 2" width="25%" height="25%"> <br>
- Choose the paper type.
- Choose the quantity. <br>
This can be done in step 3 and 4.<br>
<img src="../testing/testing_images/step3_4.png" alt="Step 3 & 4" width="25%" height="25%"> <br>
- Upload an own photo or logo.
- Edit text content.
- Download the designed card as a low-res jpeg file. <br>
<img src="../testing/testing_images/buttons.png" alt="Buttons" width="25%" height="25%">
<img src="../testing/testing_images/preview.png" alt="Preview" width="25%" height="25%"> <br>
<img src="../testing/testing_images/preview_testing.jpeg" alt="Download preview" width="18%" height="18%"> <br>
The user can click the buttons to achieve this, also the selections made with steps 1 and 2 are visible on this preview.<br>
- Send a request for a quotation for the designed business cards.<br>
<img src="../testing/testing_images/request_form1.png" alt="Request form 1" width="25%" height="25%">
<img src="../testing/testing_images/request_form2.png" alt="Request form 2" width="25%" height="25%"> <br>
<img src="../testing/testing_images/request_form3.png" alt="Request form 3" width="25%" height="25%"> <br>
<img src="../testing/testing_images/quotation_form_emailjs_mail.png" alt="Quotation form emailJS mail" width="40%" height="40%"> <br>
As with the sample kit form after everything is filled out the send button can be clicked and the user will be informed the request is send successfully and will be redirected to the homepage and the email with the values that are needed to make a quotation is send through EmailJS, to in this case me.

It can be concluded that all goals have been achieved. <br>
<br>
The project has been tested on the available DevTools for phone and tablet sizes as well as on multiple responsive sizes and it was made sure that it looks good and works well on all. It was also tested on multiple devices among others an OnePlus Nord, an iMac (Retina 5K, 27-inch, 2017), a MacBook-Air (Retina M1, 13.3-inch, 2020) and a Samsung Galaxy Tab4 (10.1-inch 2014), everything works as it should. -->

<div align="right"><a href="#top">🔝</a></div>

![HTML5](https://img.shields.io/badge/HTML5%20-%23E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=FFFFFF)
======
### HTML

HTML code was tested with a [HTML](https://validator.w3.org/nu/?doc=http%3A%2F%2Fmamamaki.herokuapp.com%2F) validator. <br>
<img src="../testing/testing_images/html_check.png" alt="HTML check" width="55%" height="55%"> <br>
No errors or warnings were found.

<div align="right"><a href="#top">🔝</a></div>

![CSS3](https://img.shields.io/badge/CSS3%20-%231572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=FFFFFF)
======

### CSS

CSS code was tested with a [CSS](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) validator. <br>
<img src="../testing/testing_images/css_check_1.png" alt="CSS check" width="55%" height="55%"> <img src="../testing/testing_images/css_check_2.png" alt="CSS check" width="55%" height="55%"> <br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way.

<div align="right"><a href="#top">🔝</a></div>

![JavaScript](https://img.shields.io/badge/JavaScript%20-%23323330.svg?&style=for-the-badge&logo=JavaScript&logoColor=F7DF1E) JavaScript
======

JavaScript was tested with a [JavaScript](https://jshint.com/) linter. <br>
<img src="../testing/testing_images/js_check_1.png" alt="JS check 1" width="55%" height="55%">
<img src="../testing/testing_images/js_check_2.png" alt="JS check 2" width="55%" height="55%"><br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way.

<div align="right"><a href="#top">🔝</a></div>

![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
======

### Python

Python was tested with a [PEP8](http://pep8online.com/) linter. <br>
<img src="../testing/testing_images/python_check.png" alt="Python check" width="55%" height="55%"><br>
No errors or warnings were found.

<div align="right"><a href="#top">🔝</a></div>

:traffic_light: Lighthouse
======

### Lighthouse

<!-- All pages have passed through Lighthouse in Chrome DevTools, the results for desktop can found here: <br>
<img src="../testing/testing_images/lighthouse_desktop.png" alt="Lighthouse desktop" width="70%" height="70%"><br>
and these are the results for the mobile versions:<br>
<img src="../testing/testing_images/lighthouse_mobile.png" alt="Lighthouse mobile" width="70%" height="70%"><br>
After doing the Lighthouse checks one warning became visible, namely: <br>
<img src="../testing/testing_images/warning_after_lighthouse.png" alt="Lighthouse warning" width="70%" height="70%"><br>
This was not there in previous testing and is likely due to changes to Google's privacy policy, tutor assistance has been contacted and this warning can be ignored.
The results of the Lighthouse tests are satisfactory, so no adjustments are needed at this time. -->

<div align="right"><a href="#top">🔝</a></div>

:bar_chart: GTmetrix
====== 

### GTmetrix

<!-- The site was tested with [GTmetrix](https://gtmetrix.com/). The reports can be found here:<br>  
[Homepage](https://gtmetrix.com/reports/daph1986.github.io/1OKsvoY3/) <br>
[Sample kit form](https://gtmetrix.com/reports/daph1986.github.io/iiv3HDsB/) <br>
[Creator page](https://gtmetrix.com/reports/daph1986.github.io/nJoX5M9e/) -->

<div align="right"><a href="#top">🔝</a></div>

:eyeglasses: Color blindness
======

### Color blindness

<!-- Color blindness was tested on this [site](https://www.toptal.com/designers/colorfilter/) to ensure you would still be able to read the website when you have different types of color blindness. Here you will find screenshots off the homepage tests, but of course all pages were tested. <br>
<img src="../testing/testing_images/protanopia.png" alt="Protanopia" width="25%" height="25%"/>
<img src="../testing/testing_images/deutanopia.png" alt="Deutanopia" width="25%" height="25%"/>
<img src="../testing/testing_images/tritanopia.png" alt="Tritanopia" width="25%" height="25%"/>
<img src="../testing/testing_images/greyscale_achromatopsia.png" alt="Greyscale / Achromatopsia" width="25%" height="25%"/> -->

<div align="right"><a href="#top">🔝</a></div>

:test_tube: Other tests
======

### Other tests

<!-- A lot of different people were asked to check the project to ensure it works on different systems and devices. The website was tested on Samsung Galaxy TabA (10.1-inch 2019), OnePlus 5, Xiaomi Redmi Note 7, Xiaomi Redmi Note 8 Pro, Motorola G9, Motorola G5 and iPhone 12 Pro Max among others. It has been tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. One bug was found and fixed, please see Bugs section for the found text bug.

#### Advices given after testing which were followed

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

<div align="right"><a href="#top">🔝</a></div>
