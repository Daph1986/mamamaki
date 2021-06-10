MAMAMAKI
======

**[Code Institute](https://codeinstitute.net/)  Milestone Project 3: Python and Data Centric Development**

<img src="static/readme images/logo.png" alt="Logo" width="65%" height="65%">

MAMAMAKI is a site where it is possible to see Japanese home cooking recipes and where when loged in you can add and adjust your own recipes.
The focus with this site is to combine knowledge about Japanese home cooking with what was learned this far about HTML, CSS, JavaScript and Python. The site’s goal is to share recipes.

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

This is meant to be a B2C site which targets visitors who are interested in Japanese home cooking.

### User stories

##### Visitor Goals

- To be able to see different recipes and search for them.
- To create an account and log in on that account.
- To create and edit own recipes.

##### Site Owners Goals

- To share the love for Japanese home cooking and promote it.
- Share nice Japanese home cooking recipes.

### Strategy

The design goal is to make a clear, accessible, structured site so that visitors can easily see the recipes, navigate on the site and add + edit their own recipes.

### Scope

The site shows a home page with a small introduction. Second is the about page which tells a bit about the creator of the site and why the site was created. Furthermore, the site contains a recipe page on which you can you choose to go to a specific recipe. It also contains a register page, a log in page, a profile page and a add recipe page.
The profile page and add recipe page will only be visible when you are logged in.

### Structure

The site will be structured as clear as possible, it should be easy to see what you can do on the page, on all screen sizes it should be clear what you can do on each part of the site. 

### Skeleton

Desktop wireframes <br>
<img src="static/readme images/desktop_all_pages.png" alt="Desktop overview" width="85%" height="85%">

Tablet wireframes <br>

<img src="static/readme images/tablet_all_pages.png" alt="Tablet overview" width="85%" height="85%">

Mobile wireframes<br>

<img src="static/readme images/mobile_all_pages.png" alt="Mobile Overview" width="85%" height="85%">

**Surface**

The following colors will be used:

<img src="static/readme images/hex_DF5B5B.png" alt="Side menu color" width="25%" height="25%"> <img src="static/readme images/hex_FFFFFF.png" alt="Side menu text color" width="25%" height="25%"> <img src="static/readme images/hex_212121.png" alt="Text color"  width="25%" height="25%"> <br>

And for a gradient background: <br>
<img src="static/readme images/hex_DE5959.png" alt="Gradient 1"  width="25%" height="25%"> <img src="static/readme images/hex_EFAA9C.png" alt="Gradient 2"  width="25%" height="25%"> <img src="static/readme images/hex_F3BEA2.png" alt="Gradient 3"  width="25%" height="25%"><img src="static/readme images/hex_F1DEC2.png" alt="Gradient 4"  width="25%" height="25%"> <br>

Which results in this: <br>
<img src="static/readme images/gradient_backrgound.png" alt="Gradient background colors" width="25%" height="25%"> <br>
For this [ColorSpace](https://mycolor.space/gradient3?ori=to+right+top&hex=%23FEFFFA&hex2=%23E9E1C7&hex3=%23A0C7D7&submit=submit) was used.

The colors were chosen because they fit very well with Japan, reminding of Sakura blossoms. The background of the sea is a reference to a traditional Japanese painting, called “The Great Wave off Kanagawa”. <br>
<img src="static/readme images/background_login.png" alt="Waves background" width="45%" height="45%"> <br>

This was chosen because it gives a nice separation to the register and log in page from the rest of the site and I think it connects well with the recipes, because a few of them use fish as an ingredient. And fish comes from the sea.

The first set up for the wireframes was with a grey background and footer, but it was felt to be UX unappealing, that’s why this was changed to the current wireframes.

<!-- During development the site's layout was restructured a little bit, because this seemed visually or otherwise better.
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

[Google Fonts](https://fonts.google.com/) was used to embed the Chicle and Ubuntu font in the code. Chicle was chosen because this reminds of Japanse calligraphy. Ubuntu was chosen because for the main text I felt this has a better readability which gives better UX.

For the icons [Font Awesome](https://fontawesome.com/) was used.

Features
======

The site contains the following features: 

- See an overview of multiple recipes.
- Select a specific recipe and see the details of that recipe.
- Have clear and easy to use page navigation.
- Register an account.
- Log in to that account and log out of it.
- Add and edit one’s own recipes.


### Features for the future 

The following items can be added: 

- Comment on other people’s recipes.
- Being able to share a recipe on social media.
- Being able to print out a recipe directly from the site with one click on a button. 
- Put the ingredients on a shopping list which one can print out.

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
All content has been written by me, but the original recipes come out of two books which are:
1. [Culinair genieten - Japans](https://www.lantaarnpublishers.nl/winkel/koken/japans/) 
2. [Japans Koken - Harumi Kurihara](https://www.yutori.co.jp/en/index.html) 


### Media 

#### Images:

1. [MCICON](https://www.mcicon.com/product/sushi-icon-3/) for the sushi icon in the logo.

2. [Adobe Stock](https://stock.adobe.com/nl/images/wave-tides-in-ukiyo-e-style/229859488) The wave image is a licensed image downloaded with a paid Adobe Stock account, the image was used for the background of the register and log in page.

3. Photos of the food, all these photos are my own.

4. [Color-hex](https://www.color-hex.com/) was used to get the images of the colors that were used.

#### Code:

1. [ColorSpace](https://mycolor.space/gradient3?ori=to+right+top&hex=%23FEFFFA&hex2=%23E9E1C7&hex3=%23A0C7D7&submit=submit) to create the gradient background with CSS.

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
