MAMAMAKI
======

**[Code Institute](https://codeinstitute.net/)  Milestone Project 3: Python and Data Centric Development**

<img src="static/readme images/logo.png" alt="Logo" width="55%" height="55%">

MAMAMAKI is a site for Japanese home cooking recipes and when you are logged in, you can add, edit and delete your own recipes.
The focus with this site is to combine knowledge about Japanese home cooking with what was learned this far about HTML, CSS, JavaScript and Python. The site’s goal is to share recipes.

:clapper: Demo
======

By clicking this [link](https://mamamaki.herokuapp.com/) a live demo version will be visible.

<img src="static/readme images/mockup_1.png" alt="Mockup 1" width="65%" height="65%">
<img src="static/readme images/mockup_2.png" alt="Mockup 2" width="65%" height="65%">

<div align="right"><a href="#top">🔝</a></div>

:open_file_folder: Table of Contents
======

**<details><summary>UX</summary>**
* [**_User stories_**](#user-stories)
    * [_Strategy_](#strategy)
    * [_Scope_](#scope)
    * [_Structure_](#structure)
    * [_Skeleton_](#skeleton)
</details>

**<details><summary>Features</summary>**
* [**_Existing Features_**](#existing-features)
* [**_Features for the future_**](#features-for-the-future)
</details>

**<details><summary>Technologies</summary>**
* [**_Languages_**](#languages)
* [**_Libraries and frameworks_**](#libraries-and-frameworks)
* [**_Wireframes_**](#wireframes)
* [**_Tools_**](#tools)
</details>

**<details><summary>Testing and Bugs</summary>**
* [**_Testing file_**](#testing-file)
</details>

**<details><summary>Deployment</summary>**
* [**_Live version_**](#live-version)
* [**_Run local_**](#run-local)
* [**_Heroku_**](#heroku)
* [**_Setting EmailJS up_**](#setting-emailjs-up)
</details>

**<details><summary>Credits</summary>**
* [**_Content_**](#content)
* [**_Code_**](#code)
* [**_Media_**](#media)
* [**_Other_**](#other)
* [**_Acknowledgements_**](#acknowledgements)
</details>
<br>

<div align="right"><a href="#top">🔝</a></div>

:busts_in_silhouette: UX
======

This is meant to be a B2C site which targets visitors who are interested in Japanese home cooking.

### User stories

##### Visitor Goals

- To be able to see different recipes and search for them using keywords.
- To create an account and log in on that account.
- To create, read, update and delete my own recipes.

##### Site Owners Goals

- To share the love for Japanese home cooking and promote it.
- Share nice Japanese home cooking recipes.

### Strategy

The design goal is to make a clear, accessible, structured site so that visitors can easily see the recipes, navigate on the site and add, edit and delete their own recipes.

### Scope

The site shows a homepage with a small introduction. Second is the about page which tells a bit about the creator of the site and why the site was created. Furthermore, the site contains a recipes page on which you can you choose to go to a specific recipe. It also contains a register page, a log in page, a personal recipe page and a add recipe page.
The personal recipe page and add recipe page will only be visible when you are logged in.

### Structure

The site will be structured as clear as possible, it should be easy to see what you can do on the page, on all screen sizes it should be clear what you can do on each part of the site. 

### Skeleton

Desktop wireframes <br>
<img src="static/readme images/desktop_all_pages.png" alt="Desktop overview" width="85%" height="85%">

Tablet wireframes <br>

<img src="static/readme images/tablet_all_pages.png" alt="Tablet overview" width="85%" height="85%">

Mobile wireframes<br>

<img src="static/readme images/mobile_all_pages.png" alt="Mobile Overview" width="85%" height="85%">

Raw data diagram<br>

<img src="static/readme images/raw_data_diagram.png" alt="Data Overview" width="65%" height="65%"><br>
Eventually some items were added to the diagram and it has been simplified.
<img src="static/readme images/updated_data_diagram.png" alt="Data Overview" width="65%" height="65%">

<div align="right"><a href="#top">🔝</a></div>

**Surface**

The following main colors will be used:

<img src="static/readme images/hex_EA5757.png" alt="Side menu color" width="25%" height="25%"> <img src="static/readme images/hex_FFFFFF.png" alt="Side menu text color" width="25%" height="25%"> <img src="static/readme images/hex_212121.png" alt="Text color" width="25%" height="25%"> <br>

For the buttons and forms the following colors will be used:

<img src="static/readme images/hex_1A581C.png" alt="Green btn" width="25%" height="25%"> <img src="static/readme images/hex_338436.png" alt="Green btn hover" width="25%" height="25%"> <img src="static/readme images/hex_C62828.png" alt="Red btn" width="25%" height="25%"> <br>
<img src="static/readme images/hex_6D1B1B.png" alt="Red btn hover" width="25%" height="25%"> <img src="static/readme images/hex_4478B1.png" alt="Blue btn" width="25%" height="25%"> <img src="static/readme images/hex_103D6D.png" alt="Blue btn hover" width="25%" height="25%"><br>
<img src="static/readme images/hex_707070.png" alt="Form color 1" width="25%" height="25%"> <img src="static/readme images/hex_757575.png" alt="Form color 2" width="25%" height="25%"> <br>

For a gradient background: <br>
<img src="static/readme images/hex_DE5959.png" alt="Gradient 1" width="25%" height="25%"> <img src="static/readme images/hex_EFAA9C.png" alt="Gradient 2"  width="25%" height="25%"> <img src="static/readme images/hex_F3BEA2.png" alt="Gradient 3"  width="25%" height="25%"><img src="static/readme images/hex_F1DEC2.png" alt="Gradient 4"  width="25%" height="25%"> <br>

Which results in this: <br>
<img src="static/readme images/gradient_backrgound.png" alt="Gradient background colors" width="25%" height="25%"> <br>
For this [CSS Gradient](https://cssgradient.io/gradient-backgrounds/) was used.

The colors were chosen because they fit very well with Japan, reminding of Sakura blossoms. The [background](https://stock.adobe.com/nl/images/wave-tides-in-ukiyo-e-style/229859488) of the sea, is a reference to a traditional Japanese painting, called “The Great Wave off Kanagawa”. <br>
<img src="static/readme images/background_login.png" alt="Waves background" width="45%" height="45%"> <br>

This was chosen because it gives a nice separation to the register and log in page from the rest of the site and I think it connects well with the recipes, because a few of them use fish as an ingredient. And fish comes from the sea.

The first set up for the wireframes was with a grey background and footer, but it was felt to be UX unappealing, that’s why this was changed to the current wireframes.

During development the site's layout was restructured a little bit, because this seemed visually or otherwise better.
They are listed below, the more extensive ones, with a link to the issue item where they are further explained.

1. [Headers](https://github.com/Daph1986/mamamaki/issues/22) on register and login page
2. [Text alignment](https://github.com/Daph1986/mamamaki/issues/23)
3. Two call to action buttons have been added to the homepage to make it more user-friendly and to register or log in right away. A contact form has also been added, again to increase user-friendliness.
4. A scroll to the top button has been added on all pages, so you don't have to scroll all the way up again, this improves user-friendliness. They will appear automatically as soon as you have to scroll down.
5. On the about page the words "register page" have been linked to go directly to that page.
6. On the single recipe page, the ingredients list and the instruction list have been made collapsible to make it easier during cooking, when you have the ingredients ready, just close it and keep only the instruction list open. Because not all the recipes show the calories, it has been decided to omit that and instead put down which user has added the recipe.
7. Some additional text has been added to the personal recipe page to indicate what it displays, and the white block was removed, the content is merged with the header.
8. Some extra fields have been added to the add recipe page, namely "remarks", "additional notes" and a switch for if it's a vegetarian recipe.
9. Initially the color of the sidenav was #df5b5b but this has been changed to #ea5757 to ensure that even when a page has a lot of content there is always a color difference between the sidenav and the background.

<div align="right"><a href="#top">🔝</a></div>

### Fonts and icons

[Google Fonts](https://fonts.google.com/) was used to embed the Chicle and Ubuntu font in the code. Chicle was chosen because this reminds of Japanese calligraphy. Ubuntu was chosen because for the main text I felt this has a better readability which gives better UX.

For the icons [Font Awesome](https://fontawesome.com/) was used.

<div align="right"><a href="#top">🔝</a></div>

:star2: Features
======

### Existing Features

The site contains the following features: 

- See an overview of multiple recipes.
- Select a specific recipe and see the details of that recipe.
- Have clear and easy to use page navigation.
- Register an account.
- Log in to that account and log out of it.
- Add, edit and delete your own recipes.

### Features for the future 

The following items can be added: 

- Comment on other people’s recipes.
- Being able to share a recipe on social media.
- Being able to print out a recipe directly from the site with one click on a button. 
- Put the ingredients on a shopping list which one can print out.
- Share videos of the cooking techniques.

<div align="right"><a href="#top">🔝</a></div>

:gear: Technologies
======

### Languages

- HTML
- CSS
- Python
- JavaScript

### Libraries and Frameworks

- Materialize 1.0.0
- jQuery
- PyMongo
- Flask
- Jinja
- Werkzeug

### Wireframes

- Adobe XD

### Tools

- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html): to resize the images.
- [tinypng](https://tinypng.com/): was used to downsize the images.
- [Cloudinary](https://cloudinary.com/): was used to store the images and get an URL-link for them which are used in my recipes.
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html): to create the logo.
- [VSCode](https://code.visualstudio.com/): to write the code in.
- [EmailJS](https://www.emailjs.com/): for receiving the content of the contact form
- [MongoDB Atlas](https://www.mongodb.com/): as a database for this project
- [Heroku](https://www.heroku.com/): as a host for the deployed site
- [GitHub](https://github.com/): for the repository

<div align="right"><a href="#top">🔝</a></div>

:white_check_mark: :bug: Testing and Bugs 
======

### Testing file

The tests have been done on multiple devices and browsers. In the end everything works as intended. Because this topic contained more content than expected, a separate page was created.
For more details about testing and bugs please view this [file](testing/README.md).

<div align="right"><a href="#top">🔝</a></div>

:computer: Deployment
======

### Live version

To view the deployed version, the steps underneath can be followed:

1. Go to [GitHub](https://github.com/)
2. Find Daph1986's [page](https://github.com/Daph1986)
3. Select repositories.
4. Select the mamamaki repository.
5. Click on the link on the right side or on the link under "Demo".
By clicking that link the live demo version will be visible. <br>

<img src="static/readme images/deployment_link_1.png" alt="Deployment link 1" width="75%" height="50%"/>
<img src="static/readme images/deployment_link_2.png" alt="Deployment link 2" width="75%" height="50%"/>

<div align="right"><a href="#top">🔝</a></div>

### Run local

If you would like to run this website locally you can clone this repository in an IDE such as VSCode. Make sure that `PIP3`, `Flask`, `Python3` and `Git` are installed. Set up your account for [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), how to do that you can see [here](https://docs.atlas.mongodb.com/).
You can clone it by following the next steps: <br>

1. Log in at [GitHub](https://github.com/) 
2. Find Daph1986's [page](https://github.com/Daph1986)
3. Select repositories.
4. Select the mamamaki repository.
5. Click on the "Code" button. <br>
<img src="static/readme images/run_local_1.png" alt="Run local 1" width="75%" height="50%"/> <br>

6. Copy the URL.
7. Open VScode or your preferred IDE, open the file or folder in which you want to use the project and open a CLI terminal.
8. Put the following command in the CLI terminal:

``` 
git clone https://github.com/Daph1986/mamamaki.git
``` 

9. Press enter, and the clone will be created.
10. Create a new `Cluster` and a new `Database` in your MongoDB account.
In this case the database is called `mamamaki_recipe_manager`, two collections are used:<br>
<img src="static/readme images/db_1.png" alt="MongoDB 1" width="25%" height="25%"/> <br> 
and they are filled out like this:<br> 
<img src="static/readme images/db_2.png" alt="MongoDB 1" width="75%" height="75%"/>
<img src="static/readme images/db_3.png" alt="MongoDB 1" width="75%" height="75%"/>

11. Create an `env.py` file, type
```
touch env.py
```
in the CLI terminal, use this file for storing your variables. It should contain this:
```
import os

os.environ.setdefault("IP", "value")
os.environ.setdefault("PORT", "value")
os.environ.setdefault("SECRET_KEY", "value")
os.environ.setdefault("MONGO_URI", "value")
os.environ.setdefault("MONGO_DBNAME", "value")
```
For `IP` you can use `0.0.0.0`, for `PORT` you can use `5000` for `SECRET_KEY` you can make up your own password or use [RandomKeygen](https://randomkeygen.com/) to generate a password. The `MONGO_URI` and `MONGO_DBNAME` values you can find in your MongoDB account.
Your `MONGO_DBNAME` is here:<br>
<img src="static/readme images/mongo_db_1.png" alt="MongoDB 1" width="75%" height="50%"/> <br>
The `MONGO_URI` you'll find when you click `Clusters` and then `Connect`.
<img src="static/readme images/mongo_db_2.png" alt="MongoDB 2" width="75%" height="50%"/> <br>
Choose the option in the middle<br>
<img src="static/readme images/mongo_db_3.png" alt="MongoDB 3" width="75%" height="50%"/> <br>
Set it to `Python` and version `3.6 or later`. Copy the code you see here:<br>
<img src="static/readme images/mongo_db_4.png" alt="MongoDB 4" width="75%" height="50%"/> <br>
Replace the password with your own and replace the database name for your own.
For more information about MongoDB Atlas, you can look [here](https://docs.atlas.mongodb.com/).

12. Create a `.gitignore` file type
```
touch .gitignore
```
in the CLI terminal, this file is to make sure that the variables of the `env.py` are not being published. It should contain:
```
env.py
__pycache__/

```
13. You can now run the app by tying:
```
python3 app.py
```
in the CLI terminal. It will show ` * Running on http://192.168.1.170:5000/ (Press CTRL+C to quit)` in the terminal, you can visit the website by pressing the link holding the CTRL or COMMAND button, depending on if you are using a Windows or IOS system.

<div align="right"><a href="#top">🔝</a></div>

### Heroku

To create a live version of the website VSCode was used together with Heroku.
To deploy the website with Heroku the following steps were made:

1. Create a `requirement.txt` and `Procfile` file by typing `pip3 freeze --local > requirements.txt` and then `echo web: python app.py >Procfile` in the CLI terminal.
2. Make sure that these files are committed, added and pushed to your GitHub repository.
3. Log in or create an account on [Heroku](https://www.heroku.com) and create a new app by clicking the button.<br>
<img src="static/readme images/heroku_deployment_1.png" alt="Deployment to Heroku 1" width="75%" height="50%"/>

4. Give the app a name in all lowercase letters and set `Choose a region` to Europe, click on create app.<br>
<img src="static/readme images/heroku_deployment_2.png" alt="Deployment to Heroku 2" width="75%" height="50%"/>

5. On you app dashboard click deploy and select GitHub, connect it to your GitHub respository. Don't click `Enable Automatic Deploys` yet. <br>
<img src="static/readme images/heroku_deployment_3.png" alt="Deployment to Heroku 3" width="75%" height="50%"/>

6. Click on Settings and then Reveal Config Vars. <br>
<img src="static/readme images/heroku_deployment_4.png" alt="Deployment to Heroku 4" width="75%" height="50%"/>

7. Fill in the vars with your own username, password, database name and secretkey which you have in your `env.py` file: <br>

| Key | Value |
 --- | ---
IP | 0.0.0.0
MONGO_DBNAME | `<your_mongodb_database_name>`
MONGO_URI | `mongodb+srv://<username>:<password>@myfirstcluster.z7l4s.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

For more information about your MONGO_URI in MongoDB Atlas you can look [here](https://docs.atlas.mongodb.com/).
<br>

8. Now click on `Enable Automatic Deploys` and then `Deploy Branch`
9. This can take a little bit, when it's ready you should see something like this:<br>
<img src="static/readme images/heroku_deployment_5.png" alt="Deployment to Heroku 5" width="75%" height="50%"/>
You can click the view button to launch your app.

<div align="right"><a href="#top">🔝</a></div>

### Setting EmailJS up

1. Go to [EmailJS](https://www.emailjs.com/) sign into your existing account or sign up to create an account.
2. Click on Email Services and then add new service. <br>
<img src="static/readme images/emailjs_1.png" alt="Set up EmailJS" width="50%" height="50%"/>
3. Save and click on Email Templates. <br>
<img src="static/readme images/emailjs_2.png" alt="EmailJS new template" width="50%" height="50%"/>
4. Make a template and give it the id names of `send contact mail` to ensure they work with the function in this code. <br>
<img src="static/readme images/emailjs_3.png" alt="Template settings" width="50%" height="50%"/>
5. Copy the service id as shown at step 2.<br>
6. Replace the id in the code for your own id. <br>
<img src="static/readme images/scriptjs.png" alt="JS file" width="50%" height="50%"/>
7. Go to Integration and copy the user id and replace your id for the id in the JavaScript file.<br>
<img src="static/readme images/integration.png" alt="Integration" width="50%" height="50%"/>
8. The EmailJS service is set up and everything should work.

:copyright: Credits
======

### Content
All content has been written by me, but the original recipes come out of two books and two websites which are:

1. [Tori to piman no itame ni - Japans Koken - Harumi Kurihara](https://www.yutori.co.jp/en/index.html) 
2. [Tamago - SUSHITOTAAL.NL](https://www.sushitotaal.nl/tamago_bereiden) 
3. [Miso soup - THE SUSHI TIMES](https://www.thesushitimes.com/recept-miso-soep-onmisbaar-japanse-keuken/) 
4. [All the other recipes - Culinair genieten - Japans](https://www.lantaarnpublishers.nl/winkel/koken/japans/) 

The recipes added by users "admin" and "daphnehf" are all cooked and photographed by me.
I have sometimes edited these recipes to my own liking while cooking, the edited versions are on the site.
Recipes posted by other users are not pre-tested!

### Code:

1. [Code Institute LMS Backend Development Task Manager Miniproject by Tim Nelson](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/) this was used as the basis of the code and then modified to make it my own site.
2. [CSS Gradient](https://cssgradient.io/gradient-backgrounds/) to create the gradient background with CSS.
3. [Stack Overflow](https://stackoverflow.com/questions/16841323/making-gradient-background-fill-page-with-css/16841457) to prevent the gradient background from repeating and without having to use a fixed height value with px.
4. [Sanwebe.com](https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery) as help to let jQuery add and remove extra fields for the ingredients list and the instruction list.
5. [Stack Overflow](https://stackoverflow.com/questions/20233721/how-do-you-index-on-a-jinja-template) to help me figure out how to loop over the ingredients list and the instruction list and get them displayed.
6. [W3schools](https://www.w3schools.com/howto/howto_js_collapsible.asp) to help me make a collapsible with HTML and JavaScript.
7. [W3schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) to help me make a scroll back to the top button.
8. [Autoprefixer CSS](https://autoprefixer.github.io/) to optimize the use of vendor extensions in the CSS code.
9. [Materialize](https://materializecss.com/) as a reference work on the framework.
10. [Python Programming](https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/) as how to use the Login_Required decorator.

<div align="right"><a href="#top">🔝</a></div>

### Media 

#### Images:

1. [MCICON](https://www.mcicon.com/product/sushi-icon-3/) for the sushi icon in the logo.

2. [Adobe Stock](https://stock.adobe.com/nl/images/wave-tides-in-ukiyo-e-style/229859488) the wave image is a licensed image downloaded with a paid Adobe Stock account, the image was used for the background of the register and log in page.

3. Photos of the food, for recipes added by users "admin" and "daphnehf", all these photos are my own.

4. [Color-hex](https://www.color-hex.com/) was used to get the images of the colors that were used.

5. [favicon.io](https://favicon.io/emoji-favicons/sushi/) was used to get an existing favicon for the site.

6. [Rawpixel](https://www.rawpixel.com/image/2400897/free-illustration-png-japan-japanese-culture-art-torii-gate) Japanese torii gate sticker with white border by Tvzsu was used as a background for the error pages.

### Other

1. [creately](https://creately.com/) to create the data diagrams.
2. [RandomKeygen](https://randomkeygen.com/) to get a value for the secret key.
3. [cdnjs](https://cdnjs.com/) to get the fontawesome cdn from.
4. [jQuery](https://code.jquery.com/) to get the jQuery cdn from.
5. [Am I Responsive?](http://ami.responsivedesign.is/) to check the responsiveness and make the mockups.
6. [WebAIM](https://webaim.org/resources/contrastchecker/) used for checking contrasts on the site.

### Acknowledgements

- My mentor from Code Institute, thank you Narender for your time and guidance.
- My husband, thank you Django for taking more care of our son so I can work on my education, thank you for trying my cooking skills with these recipes and thank you for your patience.
- Fellow student, Sean McMahon, in who's Readme file I saw the idea to make a collapsible table of contents.
- Fellow student, Kotaro Tanaka, in who's Readme file I saw the idea to make it possible to go back of the top of a page.
- Fellow student, Benjamin Kavanagh (BenKav_lead), for looking into my code and remind me to use also the url_for also my images to prevent them from giving a 404.
```
{{ url_for('static', filename='images/logo.png') }}
```
- Fellow slack members, Andrew Dempsey, Mike Avgeros and Peter Baker for extensively testing my project.
- Special thanks to my colleagues, friends and family for their support, tips and for testing my project.

<div align="right"><a href="#top">🔝</a></div>