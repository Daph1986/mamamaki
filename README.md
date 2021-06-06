MAMAMAKI
======

**[Code Institute](https://codeinstitute.net/)  Milestone Project 3: Backend Development**

<img src="static/readme images/logo.png" alt="Logo" width="80%" height="80%">

MAMAMAKI is a site where it is possible to see Japanese home cooking recipes and where when loged in you can add and adjust your own recipes. 
The focus with this site is to combine knowledge about Japanese home cooking with what was learned this far about HTML, CSS, JavaScript and Python. The site’s goal is to design share recipes.

Demo
======

<!-- By clicking this [link](https://daph1986.github.io/Postfly-business-card-creator/) a live demo version will be visible.

<img src="assets/images/readme_images/mockup1.png" alt="Mockup 1" width="65%" height="65%">
<img src="assets/images/readme_images/mockup2.png" alt="Mockup 2" width="65%" height="65%"> -->

Table of Contents
======

- [UX](#ux)
    - [User stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
- [Features](#features)
- [Technologies](#technologies)
- [Testing and Bugs](#testing-and-bugs)
- [Deployment](#deployment)
    - [Live version](#live-version)
    - [GitHub Pages](#github-pages)
    - [Run local](#run-local)
    - [Setting EmailJS up](#setting-emailjs-up)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Other](#other)
    - [Acknowledgements](#acknowledgements)

UX
======

This is meant to be a B2B site which targets visitors  who are in need of business cards and want to design it themselves.

### User stories

##### Visitor Goals

<!-- - Create / design your own business card.
- Be able to choose the paper type and quantity.
- Request a sample kit with papers for if you are not familiar with the paper types.
- Request a quotation and download the designed card. -->

##### Site Owners Goals

<!-- - Provide the service of designing your own business cards in an easy way, without additional designing costs.
- Reduce workload on the prepress (design) staff.
- Expand customer base. -->

### Strategy

<!-- The design goal is to make a clear, accessible, structured site so that visitors can easily design their own business cards. -->

### Scope

<!-- The site shows a homepage with an explanation, there the user can either first request a sample kit for the paper types or start designing. On the creator site it allows the user to choose out of three different sizes of business cards, to choose a background color, to choose the paper type, to choose the quantity, to upload an own photo or logo, to edit text content, to download the designed card as a low-res jpeg file, to send a request for a quotation for the designed business cards. -->

### Structure

<!-- This site is structured as clear as possible, it is easy to see what can be done on the page, on all screen sizes it is clear what should be done on each part of the site. The design of the card is visible on all screen sizes. This all ensures that the user knows what to do and what to expect. -->

### Skeleton

Desktop wireframes <br>

<img src="static/readme images/home_page.png" alt="Desktop home page" width="65%" height="65%">

<img src="static/readme images/about_page.png" alt="Desktop about page" width="65%" height="65%">

<img src="static/readme images/recipes.png" alt="Recipes page" width="65%" height="65%">

<img src="static/readme images/specific_recipe.png" alt="Specific recipes page" width="65%" height="65%">

<img src="static/readme images/register.png" alt="Register" width="65%" height="65%">

<img src="static/readme images/log_in.png" alt="Log in" width="65%" height="65%">

<!-- Tablet wireframes <br>

<img src="assets/images/readme_images/tablet_overview.png" alt="Tablet Overview 1" width="85%" height="85%"> -->

<!-- Mobile wireframes<br>

<img src="assets/images/readme_images/mobile_overview.png" alt="Mobile Overview 1" width="85%" height="85%"> -->

**Surface**

<!-- The colors that were used are the existing corporate identity colors, white and an off-white color, which are:

<img src="assets/images/readme_images/red.png" alt="Red" width="25%" height="25%"> <img src="assets/images/readme_images/red2.png" alt="Red 2" width="25%" height="25%"> <img src="assets/images/readme_images/dark_grey.png" alt="Dark Grey"  width="25%" height="25%"> <img src="assets/images/readme_images/white.png" alt="White"  width="25%" height="25%"> <img src="assets/images/readme_images/off_white.png" alt="Off White"  width="25%" height="25%">

The colors used as background colors for the user to select were found when another project was inspected with the DevTools. These colors have been chosen because they are full and bright. <br>
<img src="assets/images/readme_images/colors.png" alt="Background colors" width="25%" height="25%">

During development the site's layout was restructured a little bit, because this seemed visually or otherwise better.
What was changed is:

1. The color for the red headers and buttons were changed from #e73b3b to #e72f4c and #e02a51 because during testing #e73b3b did not give a good enough contrast.
2. The icon for the website was added, because it would be logical to refer to the main website of the company.
3. On the sample kit request form and the quotation request form a checkbox was added to reduce spam by checking if the user is a robot.
4. The layout for desktop view on the creator.html for the card selectors was changed a bit to make it look more appealing on smaller screens and to make it more logical to follow the steps.
5. The Select Size and Select Printing Method options were combined to give it a UX friendly experience.
6. The buttons for adding a text field, downloading the preview file and resetting the made choices are grouped together to present a better and UX friendly experience.
7. The button to upload an own file was separated from the other selectors and made pulsing to give it better attention.
8. The legend which explains all the lines (bleed etc.) of the templates has been put above the template to give it a UX friendly experience.
9. On the bottom of the page above the input fields for name and email address a small explanation was added to create a more UX friendly experience.
10. After testing the user-friendliness was experienced as not good enough, because only the logo could be used to return to the homepage. That is why on the page for requesting the sample kit and for designing the business card, 2 buttons have been added at the top to switch between the other pages. Cancel buttons have also been added to the bottom of the forms and the request quotation button was changed to send. This increases user-friendliness. -->

### Fonts and icons

<!-- [Google Fonts](https://fonts.google.com/) was used to embed the Roboto font in the code. Roboto was chosen because this is already in use on the existing POSTFLY site and it fits the corporate identity.

For the icons on the homepage [Font Awesome](https://fontawesome.com/) was used and for the other two pages the icons of [Materialize](https://materializecss.com/icons.html) were used. -->

Features
======

<!-- The site contains the following features: 

- choose out of three different sizes of business cards
- choose a background color
- choose the paper type
- choose the quantity
- upload an own photo or logo
- edit text content
- download the designed card as a low-res jpeg file
- reset the selected items
- send a request for a quotation for the designed business cards -->

### Features for the future 

<!-- The following items can be added: 

- choose a different color for the frontside and the backside of the card
-	choose the production / delivery time
-	customize the paper size
- choose between round or right angles
-	integrate it on the POSTFLY website
-	show costs in advance without having to ask for a quotation
- set the designed business card through as an order -->

Technologies
======

### Code languages, libraries and frameworks

<!-- - HTML5
- CSS3
- Materialize 1.0.0
- JavaScript
- Fabric
- EmailJS -->

### Wireframes

- Adobe XD

### Others

- Adobe Photoshop: to resize the images.
- Adobe Illustrator: to create the logo.
- VSCode: to write the code in.

Testing and Bugs
======

<!-- The tests have been done on multiple devices and browsers, in the end everything works as intended. Because this topic contained more content than expected, a separate page was created.
For more details about testing and bugs please view this [file](testing/README.md). -->

Deployment
======

### Live version

<!-- To view the deployed version, the steps underneath can be followed:

1. Go to [GitHub](https://github.com/)
2. Find Daph1986's [page](https://github.com/Daph1986)
3. Select repositories.
4. Select the Postfly-business-card-creator repository.
5. Click on the link on the right side or on the link under "Demo".
By clicking that link the live demo version will be visible. <br>

<img src="assets/images/readme_images/deployment_4.png" alt="Deployment link 4" width="75%" height="50%"/>
<img src="assets/images/readme_images/deployment_5.png" alt="Deployment link 5" width="75%" height="50%"/> -->

### GitHub Pages

<!-- To create a live version of the website VSCode was used together with GitHub Pages.
To deploy the website with GitHub pages the following steps were made:

1. Login into the personal GitHub account.
2. Go to the repository: https://github.com/Daph1986/Postfly-business-card-creator
3. Click on settings. <br>

<img src="assets/images/readme_images/deployment_1.png" alt="Deployment link 1" width="75%" height="50%"/>

4. Then almost at the bottom the "GitHub Pages" part is found, the branch "master" was selected and saved. <br>

<img src="assets/images/readme_images/deployment_2.png" alt="Deployment link 2" width="75%" height="50%"/>

5. After a few minutes the published result was visible. <br>

<img src="assets/images/readme_images/deployment_3.png" alt="Deployment link 3" width="75%" height="50%"/> -->

### Run local

<!-- If you would like to run this website locally you can clone this repository in an IDE such as VSCode.
You can clone it by following the next steps: <br>

1. Log in at [GitHub](https://github.com/) 
2. Find Daph1986's [page](https://github.com/Daph1986)
3. Select repositories.
4. Select the Postfly-business-card-creator repository.
5. Click on the green "Code" button. <br>

<img src="assets/images/readme_images/deployment_6.png" alt="Deployment link 6" width="75%" height="50%"/> <br>

6. Copy the URL.
7. Open VScode or your preferred IDE, open the file or folder in which you want to use the project and open a CLI terminal.
8. Put the following command in the CLI terminal:

``` 
git clone https://github.com/Daph1986/Postfly-business-card-creator.git
``` 

9. Press enter and the clone will be created, it is ready to work on.
```
Cloning into 'Postfly-business-card-creator'...
remote: Enumerating objects: 113, done.
remote: Counting objects: 100% (113/113), done.
remote: Compressing objects: 100% (71/71), done.
remote: Total 113 (delta 34), reused 105 (delta 26), pack-reused 0
Receiving objects: 100% (113/113), 8.54 MiB | 11.13 MiB/s, done.
Resolving deltas: 100% (34/34), done.
``` -->

Credits
======

### Content
All content has been written by me.

### Media 

#### Images:

1. [MCICON](https://www.mcicon.com/product/sushi-icon-3/) 
- for the sushi icon of the logo.

2. Photos, all the photos are my own.

#### Code:

<!-- 1. [Autoprefixer CSS](https://autoprefixer.github.io/) to optimize the use of vendor extensions in the CSS code.
2. Adding the defer attribute to the script files in html was a tip given by my mentor Narender, this ensures that the script files are executed when the page has finished loading.
3. [Codegrepper](https://www.codegrepper.com/code-examples/javascript/getting+value+from+radio+button+javascript) for getting the value of the checked radio buttons instead of using for loops.
4. [W3schools](https://www.w3schools.com/howto/howto_js_media_queries.asp) to get an idea of how to do a media query in JavaScript.
5. [Code Institute LMS Sending Emails Using EmailJS](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+IFD101+2017_T3/courseware/03d3f6524ad249d9b33e3336d156dfd0/e4710f80cdf34bffbd607bc102482d5c/) to get understanding on how to EmailJS works, the used EmailJS are based on what waslearned in the course material. -->

#### For research when I forgot how things worked again:

<!-- 1. [Code Institute LMS](https://learn.codeinstitute.net/login)
2. [W3schools](https://www.w3schools.com/)
3. [Stack Overflow](https://stackoverflow.com/)
4. [Materialize](https://materializecss.com/) -->

### Other

<!-- 1. [DIGIdesigner](https://github.com/D1ang/DIGIdesigner) this idea got me the inspiration for my subject on the milestone 2 project.
2. [Fabric](http://fabricjs.com/) as a library to make the functions work on the canvas.
3. [cdnjs](https://cdnjs.com/) to get the JavaScript cdn's from.
4. [JustSunOne](https://www.youtube.com/watch?v=mghXNWvVGTs) his tutorials about Fabric were followed to get an understanding of how things worked.
5. [Our Code World](https://ourcodeworld.com/articles/read/1016/how-to-create-your-own-t-shirt-designer-using-fabricjs-in-javascript) this example was used as an inspiration for the business card creator tool.
6. [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/) this creates a table of contents for Markdown, many thanks to follow student Aukje (byIlsa_lead) for sharing this.
7. [Am I Responsive?](http://ami.responsivedesign.is/?url=https%3A%2F%2Fdaph1986.github.io%2FPostfly-business-card-creator%2Findex.html) to check the responsiveness and make the mockups. -->

### Acknowledgements
<!-- 
- My mentor from Code Institute, thank you Narender for your time and guidance.
- My husband, thank you Django for taking care of our son more so I can work on my education, thank you for your patience, thank you for your extra explanation about JavaScript and thank you for checking my project!
- My colleague Bart Lauwaert for helping with the translation of the correct English names for the paper types.
- Aukje (byIlsa_lead) thank you for hosting a "Preparing for your Second Milestone Project" call on zoom, it was really helpful! Also thank you for your time and effort to go through my code in order to help me with my question about my form.
- Cormac, Johann and Scott from Code Institute tutor assistance, thank you for helping me with my questions.
- Special thanks to my colleagues, friends and family for their support, tips and for testing my site. -->
