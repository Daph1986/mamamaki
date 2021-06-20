Table of Contents
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
<br>

<div align="right"><a href="#top">🔝</a></div>

Manual testing
======

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

<br>

<div align="right"><a href="#top">🔝</a></div>

HTML
======

<!-- HTML code was tested with a [HTML](https://validator.w3.org/#validate_by_input) validator, all the pages were checked. <br>
<img src="../testing/testing_images/html_check.png" alt="HTML check" width="55%" height="55%"> <br>
No errors or warnings were found. -->

<br>

<div align="right"><a href="#top">🔝</a></div>

CSS
======

<!-- CSS code was tested with a [CSS](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) validator. <br>
<img src="../testing/testing_images/css_check.png" alt="CSS check" width="55%" height="55%"> <br>
Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way. -->

<br>

<div align="right"><a href="#top">🔝</a></div>

JavaScript
======

<!-- JavaScript was tested with a [JavaScript](https://jshint.com/) linter. <br>
<img src="../testing/testing_images/js_check1.png" alt="JS check 1" width="55%" height="55%">
<img src="../testing/testing_images/js_check2.png" alt="JS check 2" width="55%" height="55%"><br>
<img src="../testing/testing_images/js_check3.png" alt="JS check 3" width="55%" height="55%"><br>
Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way. -->

<br>

<div align="right"><a href="#top">🔝</a></div>

Python
======

<br>

<div align="right"><a href="#top">🔝</a></div>

Lighthouse
======

<!-- All pages have passed through Lighthouse in Chrome DevTools, the results for desktop can found here: <br>
<img src="../testing/testing_images/lighthouse_desktop.png" alt="Lighthouse desktop" width="70%" height="70%"><br>
and these are the results for the mobile versions:<br>
<img src="../testing/testing_images/lighthouse_mobile.png" alt="Lighthouse mobile" width="70%" height="70%"><br>
After doing the Lighthouse checks one warning became visible, namely: <br>
<img src="../testing/testing_images/warning_after_lighthouse.png" alt="Lighthouse warning" width="70%" height="70%"><br>
This was not there in previous testing and is likely due to changes to Google's privacy policy, tutor assistance has been contacted and this warning can be ignored.
The results of the Lighthouse tests are satisfactory, so no adjustments are needed at this time. -->

<br>

<div align="right"><a href="#top">🔝</a></div>

GTmetrix
====== 

<!-- The site was tested with [GTmetrix](https://gtmetrix.com/). The reports can be found here:<br>  
[Homepage](https://gtmetrix.com/reports/daph1986.github.io/1OKsvoY3/) <br>
[Sample kit form](https://gtmetrix.com/reports/daph1986.github.io/iiv3HDsB/) <br>
[Creator page](https://gtmetrix.com/reports/daph1986.github.io/nJoX5M9e/) -->

<br>

<div align="right"><a href="#top">🔝</a></div>

Color blindness
======

<!-- Color blindness was tested on this [site](https://www.toptal.com/designers/colorfilter/) to ensure you would still be able to read the website when you have different types of color blindness. Here you will find screenshots off the homepage tests, but of course all pages were tested. <br>
<img src="../testing/testing_images/protanopia.png" alt="Protanopia" width="25%" height="25%"/>
<img src="../testing/testing_images/deutanopia.png" alt="Deutanopia" width="25%" height="25%"/>
<img src="../testing/testing_images/tritanopia.png" alt="Tritanopia" width="25%" height="25%"/>
<img src="../testing/testing_images/greyscale_achromatopsia.png" alt="Greyscale / Achromatopsia" width="25%" height="25%"/> -->

<br>

<div align="right"><a href="#top">🔝</a></div>

Other tests
======

<!-- A lot of different people were asked to check the project to ensure it works on different systems and devices. The website was tested on Samsung Galaxy TabA (10.1-inch 2019), OnePlus 5, Xiaomi Redmi Note 7, Xiaomi Redmi Note 8 Pro, Motorola G9, Motorola G5 and iPhone 12 Pro Max among others. It has been tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. One bug was found and fixed, please see Bugs section for the found text bug.

#### Advices given after testing which were followed

1. Some spelling and grammar changes have been made after reviews from my husband, brother-in-law and sister-in-law.
2. My husband, Django, did not think the user-friendliness was good enough, because only the logo could be used to return to the homepage. That is why on the page for requesting the sample kit and for designing the business card, 2 buttons have been added at the top to switch between the other pages. Cancel buttons have also been added to the bottom of the forms. This increases user-friendliness. -->

<br>

<div align="right"><a href="#top">🔝</a></div>

Bugs
======

#### Background
For the backgrounds the following CSS was used:<br>
Base background:
```
body {
  background-color: #f1dec2;
  background-image: linear-gradient(135deg, #f1dec2 0%, #f3bea2 30%, #efaa9c 41%, #de5959 75%);
  height: 1000px;
} 
```
```
@media only screen and (max-width : 414px) {
  body {
    height: 736px;
  }
  .register {
    height: 736px;
  }
  .headers{
    margin-top: 50px;
  }
}
```
Register background:
```
.register {
  background-image: url(/static/images/background_login.png);
  height: 1500px;
	width: 100%;
	-webkit-background-size: cover;
	-moz-background-size: cover;
	-o-background-size: cover;
	background-size: cover;
	display:flexbox;
	align-items: center;
	justify-content: center;
	position: relative;
}
```
```
@media only screen and (max-width : 1024px) {
  body {
    height: 1366px;
  }
  header, main, footer {
    padding-left: 0;
  }
  .btn-green {
    font-size: 14px;
  }
  main .fas:before {
    font-size: 16px;
  }
  .register {
    height: 1366px;
  }
} 
```
This was used because otherwise the base background would repeat and the register page background would be cut off.<br>
<img src="../testing/testing_images/gradient_background.png" alt="Mobile nav start" width="50%" height="50%"> <br>
<img src="../testing/testing_images/register_background.png" alt="Mobile nav start" width="50%" height="50%"> <br>
But the fixed height with px bothered me. After some searching I found a way on stack overflow to fix it for the gradient background and figured out how to fix it for the register background myself.
Which resulted in the following CSS:<br>
Base background:
```
html {
  min-height: 100%;
  background-color: #f1dec2;
  background-image: linear-gradient(135deg, #f1dec2 0%, #f3bea2 30%, #efaa9c 41%, #de5959 75%);
  background-repeat:no-repeat;
  font-family: 'Ubuntu', sans-serif;
  color: #212121;
}
```
Register background:<br>
```
.bg-register {
  height: 100vh;
  min-height: 100%;
  background-image: url("/static/images/background_login.png");
  background-repeat: no-repeat;
  background-size: cover;
}
```
The media queries were no longer necessary.
<br>

<div align="right"><a href="#top">🔝</a></div>

#### Mobile nav
Once the background images bug was fixed, the hamburger menu icon looked like this:<br>
<img src="../testing/testing_images/mobile_nav_start.png" alt="Mobile nav start" width="30%" height="30%"> <br>
The following CSS code was used to get it fixed:
```
header {
  position: absolute;
  z-index: 5;
}
```
Which resulted in this:<br>
<img src="../testing/testing_images/mobile_nav_1.png" alt="Mobile nav 1" width="30%" height="30%"><br><br><img src="../testing/testing_images/mobile_nav_2.png" alt="Mobile nav 2" width="30%" height="30%"><br>
But when the nav links were clicked, nothing happend, you stayed at the same page, the links weren't working anymore.
After thoroughly checking the HTML code of the side nav and mobile nav, this was causing the problem:
```
<!-- mobile navbar-->
<a href="#" data-target="slide-out" class="sidenav-trigger">
  <i class="fas fa-bars hamburger-menu opaque-overlay hide-on-large-only"></i>
</a>
```
To fix it the CSS of the hamburger menu was changed to:
```
.hamburger-menu {
  font-size: 30px;
  margin-top: 20px;
  margin-left: 30px;
  color: #fff;;
  position: absolute;
  z-index: 3;
}
```
After that the nav links worked again.
<br>

<div align="right"><a href="#top">🔝</a></div>

#### Flash messages
Once the mobile nav bug was fixed, another bug arose:<br>
<img src="../testing/testing_images/flash_message_bug_1.png" alt="Flash message bug 1" width="30%" height="30%"><br>
The flash message pussed the background down.
This was tried to fix with the following css:
```
.flashes {
  position: absolute;
  z-index: 5;
}
```
Which resulted in:<br>
<img src="../testing/testing_images/flash_message_bug_2.png" alt="Flash message bug 2" width="30%" height="30%"><br>
Of course this didn't look very nice.
The CSS was adjusted to:
```
.flashes h4 {
  font-family: 'Chicle', sans-serif;
  color: #DF5B5B;
  padding-left: 300px;
}
.flashes {
  position: absolute;
  z-index: 5;
  background-color: rgba(255, 255, 255, 0.9);
  width: 100%;
  line-height: 1;
  top: 650px;
}
```
<img src="../testing/testing_images/flash_message_bug_3.png" alt="Flash message bug 3" width="30%" height="30%"><br>
The contrast of the pink text with the white background wasn't good enough, so it was changed to a blue color #4478b1 which has no problems with the contrast and fits nicely with the design.<br>
<img src="../testing/testing_images/flash_message_bug_4.png" alt="Flash message bug 4" width="30%" height="30%"><br>

<div align="right"><a href="#top">🔝</a></div>

#### Logo in sidenav
Once the profile page was made I saw that when logged in and on the personal recipe page the logo in the sidenav disappeared and gave a 404 for the image.<br>
<img src="../testing/testing_images/logo_logged_in_not_working.png" alt="Logo logged in not working" width="30%" height="30%"><img src="../testing/testing_images/img_404.png" alt="Logo 404" width="70%" height="70%"><br>
It was only on this page, for example on the about page it gave no problem and as soon when you logged out it was also fine.<br>
<img src="../testing/testing_images/logo_logged_in_working.png" alt="Logo logged in not working" width="30%" height="30%">
<img src="../testing/testing_images/logo_logged_out_working.png" alt="Logo logged out working" width="30%" height="30%"><br>
I didn't see what caused the problem and posted my question on Slack, fellow student Benjamin Kavanagh, looked into my code and reminded me to use also the 
```
{{ url_for('static', filename='images/logo.png') }}
```
for my images to prevent them from giving a 404. This solved the bug.
<br>

<div align="right"><a href="#top">🔝</a></div>
