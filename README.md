# Hair Styles Website - Joeline Alves
## Backend Development Milestone Project

![mockup image](/documentation/mockup.png)

## Introduction
Welcome to my Milestone Project 3. Hair Styles is a website that allows users to find different types of hair styles, from extensions, braids to different hair textures. The site allows users to search for hair styles, add their own hair styles, and edit and delete hair styles they have created. Furthermore, the admin account allows the admin user to create, edit and delete the different categories of hair styles. Additionally, users can send a message to the website creator via the contact form, which uses the EmailJS API.

View the live project [here.](https://flask-hair-manager-project-54736428c656.herokuapp.com/ "View the Live game here")


___

## Table of Contents

1. [User Experience (UX)](#ux)
    - [User Stories](#user-stories)
        - [Target Audience](#target-audience)
        - [First Time User Goals](#first-time-user-goals)
        - [Frequent User Goals](#frequent-user-goals)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
2. [Features](#features)
    - [Design](#design)
    - [Wireframes](#wireframes)
    - [Features](#features)
    - [Future Features](#future-features)
3. [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [TEST.md](TEST.md)
5. [Deployment](#deployment)
    - [Heroku](#heroku)
6. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

___

## 1. User Experience (UX)

## User Stories

### Target Audience

The target audience for Hair Styles is anyone who likes hair styles and wants to know more about the different types of hair and who wants to be more informed on the subject, as well as who wants to share their hair knowledge. It is also for those who want to know more about hair styles. People who work directly with hair can also use it to find out what hair style trends are and to keep up to date with different types of hair textures.

### First Time User Goals

As a first time user, I want to:
* be able to view the site clearly on any device.
* be able to easily navigate around the site.
* be able to search for diferent hair styles.
* be able to sign up to the site quickly.
* be able to add news hair styles.
* know that my hair styles are protected, I am the only one can be able to edit or delete them.
* be able to sign out of my account.




### Frequent User Goals

As a returning user, I want to 
* be able to view the site clearly on any device.
* be able to sign back into my account quickly.
* be able to search for hair styles.
* be able to view my hair styles in one place.
* be able to edit my own hair styles.
* be able to delete my own hair style.
* know that my hair styles are protected, I am the only one can be able to edit or delete them.
* be able to sign out of my account.


### Administrator Goals

As an administrator of the site, I want to be able to:
* view the site clearly on any device.
* sign back into my account quickly.
* edit all categories if necessary.
* delete all categories if necessary.
* add new categories.
* edit hair styles I created.
* delete hair styles I created.
* add new hair styles.


### Colour Scheme

[Coolors](https://coolors.co) was used to create a calming colour scheme that would not distract from the content.

![colour chart](/documentation/colour_page.jpg)


### Typography
The main font used for the Nav Bar heading and the rest of the site uses Raleway. Both have Sans-Serif as a fall-back font and are easy to read.

[Back to top](#table-of-contents)
___

## 2. Features

### Design

Site Map 

![site map]()

Database

The tables for the data have been created on MongoDB which is a non-relational database.

![ER diagram](/documentation/diagram_er.png)

### Wireframes

[Figma](https://figma.com/) was used to create wireframes of the design of the site for mobile phones, tablets and desktop devices.

Home Page

![homepage](/documentation/homewireframe_web.jpeg)

Register page

![sign up page](/documentation/registerwireframe_web.jpeg)

Log in page

![log in page]()


New Hairstyle page

![add hairstyle page]()

Profile Dashboard

![profile page]()

Manage Categories page

![manage categories]()

### Features

#### Nav Bar
The nav bar is displayed on all pages and allows users to easily navigate the site. The nav bar has a brand name on the left to increase brand identity throughout the site. The brand name links back to the main page for ease of navigation. The links change colour when hovered over to signal to the user which hyperlink they have the mouse over. 
The nav bar presents differently for different user. Unregistered/Logged out users will only be able to see links for 'Home', 'Contact Us', 'Log in', 'Log In' and 'Register'. 

![nav logged out](/documentation/logout_navbar.png)

Once logged in, users will also see nav links for 'New Hairstyle', 'Profile' and will no longer see 'Log In' or 'Register' links.

![nav logged in](/documentation/user_navbar.png)

Admin users can also see a link for 'Manage Categories' once logged in. 

![nav admin logged in](/documentation/admin_navbar.png)

The nav bar is responsive and resizes when viewed on mobile devices as a side nav bar rather than a top one.

Logged out

![side nav logged out](/documentation/mobile_logoutNav.png)

Logged in

![side nav logged in](/documentation/mobile_userNav.png)

Admin

![side nav admin](/documentation/mobile_adminNav.png)

#### Cards area

When accessing the website, the different cards with images of different hairstyles attract attention and immediately convey the context of the website. I decided to only display them on the home page to allow a larger window for forms and analytics on subsequent pages to provide a better user experience.

#### Footer

The footer contains social media links which could direct to Hair Styles social media pages in future. It also contains a copyright. Each link opens in a new browser window to allows user to keep the Hair Styles site open. The links all have an aria-label attribute to improve the experience for assistive technology users.

#### Flash Messages
Flash messages appear to provide the user with feedback on actions for example to confirm if a hair style has been added or deleted and to confirm when users have logged in or logged out. The style of the messages is similar to the rest of the site to provide good user experience.

#### Modals
Modals have been used on pages that involve the ability to delete something, for example on Manage Categories. The button on the page triggers the modal to open, and the delete functionality only works through the delete button on the modal. This is to reduce instances where people accidentally delete something and provides better user experience. Modals are also used to inform users that the form filled out on the contact page was successfully submitted.

___

### Pages

The website consists of nine pages that run from a base page:

* Hair styles Page
* Register page
* Log in page
* Profile page
* Add a hair style page
* Edit a hair style page
* Categories page
* Add category page
* Edit category page
* Contact page


All users can open the following pages: 

#### Home Page

The home page contains a search bar for ease of use to allow users to start searching for hairstyles right away. It also contains twenty cards that contain the different hairstyles with different content - name of the respective hairstyle, common name, a brief description, how to care, and even features a link to a video with more details. It has been deliberately kept minimalist to allow users to easily navigate the site.

![home](/documentation/homepage_web.png)

#### Contact Page

Any user can access the contact page and fill out the contact form. This was deliberately chosen so that anyone who has a problem or question can contact the site administration. The form connects to the EmailJS API to allow the form content to be emailed to the site administrator. The modal is triggered to inform the user that the email was sent successfully.

![contact](/documentation/contact_web.png)

#### Register Page

The Sign Up page comprises of a form for users to complete to create an account. The fields have icons to easily identify each field and to improve the visual effect of the form panel. Users are required to complete each field and are unable to submit the form if fields don't follow a specified format. Users are unable to create a username that already exists as this is checked against the database. Users are prompted 'Username unavailable. Please try a different username.' There is also a link to the Log in page with the prompt 'Already registered?' to avoid multiple accounts being created. The First Name and Last Name fields are listed side by side on larger displays and in blocks on smaller screen sizes to provide ease of accessibility.

![sign up](/documentation/register_web.png)

#### Log In Page

The Log In page again is a simple form that requires both fields to be completed. This is then checked against the database and the user is then redirected to their profile page if the account matches the database, or if it does not match then a flash message is displayed that the username or password is invalid. This wording was deliberately chosen to increase security as the user will be unsure which field is incorrect thus making it harder to hack.

![login](/documentation/login_web.png)


Users who are logged in can access the following pages:

#### Profile Page

The profile page displays the hairs styles that the user has added. The card panels include two buttons: Edit and Delete. The Delete button triggers the modal to confirm whether the user really wants to delete the review. The Edit button takes the user to the  edit hair style page.

![profile](/documentation/profile_web.png)

#### Edit hairstyle Page

This page displays the current revision of the site using the hair_id value to populate the fields with values. Users can then edit the fields and have the option to save the edited hairstyle or cancel and return to the Hairs page. Again, the parameters have been set to the field values, so they are mandatory. 

![edit hairstyle](/documentation/edithair_page.png)

#### Add hairstyle Page

Signed in users can complete the form to submit a new hairstyle. The form includes the keys of category, hair name,  common name, image URL, description, hair care, and added date which is a Materialize date picker for ease of entry and uniformity of values in the database. All values are required except, as previously mentioned. The form can then be submitted and stored in the database, or the Cancel button returns the user to the Hairs page. This all enables ease of navigation and good user experience.

![add hairstyle](/documentation/addHairstyle_web.png)

#### Log Out Link

When users click on the Log Out link their session ends and they are redirected to the log in page. A flash message gives confirmation that they have been logged out successfully.

![log out](/documentation/logout_web.png)


The following pages are only accessible to Admin users:

#### Manage Categories Page

The categories in the database are displayed on Materialize card panels that are responsive based on device size for clear display and good user experience. The card panels contain two buttons: edit and delete. The delete button triggers the modal to confirm the user wants to delete the location. The edit button redirects the user to the edit page. The buttons have been designed to echo the site colours providing brand identity. 

![manage categories](/documentation/manageCategorie_web.png)

#### Edit Categories Page

The edit page contains a very simple form which is prepopulated with the category that the user has selected to edit. Upon clicking the edit category button the user is redirected back to the Manage categories page. A cancel button is also provided if the user changes their mind to avoid them needing to user the browser's back button.

![edit categories](/documentation/editcategorie_web.png)

#### Add Categories Page

Again, this page contains a very simple form. The user is required to enter a category name that is longer than three letters. Upon clicking the Add category button the user is redirected back to the Manage categories page. Again, the cancel button is also provided if the user changes their mind to avoid them needing to user the browser's back button.

![add categorie](/documentation/addcategorie_web.png)

___

### Future Features
Ideas for future implementation include:

- the functionality that allows a user to save a hairstyle as a 'favorite' and have it appear on their profile page.
- the functionality that user received the auto-reply email back.
- the ability for users to change their passwords and a function to accommodate forgotten passwords.
- the option for a user to delete their account.
- the option for a user to choose the language they want on the website.
- add 404 error page.



[Back to top](#table-of-contents)
___

## 3. Technologies

### Languages

HTML, CSS, JavaScript & Python

### Frameworks, Libraries and Programs Used

* MongoDB Atlas - database server, noSQL.
* Heroku - to deploy the project.
* Flask - micro web framework written in Python.
* mongoDB shell - command shell.
* dnspython - DNS toolkit for Python.
* PyMongo - Python-Mongo library. 
* Pip - for installing Python packages.
* Jinga - to generate markup as well as source code.
* Werzberg - for secure password hashing.
* Balsamiq - to produce wireframes.
* Figma - to produce wireframes.
* GitHub - to save files for the website.
* jQuery - for javascrip fuctionality.
* Google Fonts - to import fonts.
* Font Awesome - to icons on the pages.
* Gitpod - to write code, commit and push the code to the GitHub.
* codeanywhere - to write code, commit and push the code to the GitHub.
* Workbench to create the ER diagram.


[Back to top](#table-of-contents)
___

## 4. Testing

A separate [TEST.md](TEST.md) file has been created for the documentation of testing.

[Back to top](#table-of-contents)

___

## 5. Deployment
### Heroku

To deploy the Hair Styles website to Heroku the following steps were taken:
1.	Create a Procfile by using the command echo web: python app.py > Procfile at the terminal prompts. Any extra lines need to be removed from the end of the Procfile.
2.	Create a requirements.txt file using the command pip3 freeze —local > requirements.txt
3.	Create then a Heroku account and then log in.
4.	Click the create new app button. Provide a name for the app (must be unique within Heroku) and choose the closest region to your location (namely Europe).
5.	Set up deployment from GitHub repository (Deploy > Deployment method > GitHub) - at this stage automatic deployment from GitHub repository should not be selected.
6.	Choose the appropriate GitHub repository from the options.
7.	Select the Reveal Config Vars option and set the config vars as follows:

| Key    | Value |
| ----------- | ----------- |
| Set Secret Key  | < secret key value >     |
|  IP | "0.0.0.0"        |
|  PORT | "5000"        |
|  MONGO_DB NAME | "hair_manager"       |
|  MONGO_URI |   “mongodb+srv://joelinealves08:password@myfirstcluster.necz9fz.mongodb.net/hair_manager?retryWrites=true&w=majority&appName=myFirstCluster"      |



### Cloning the Git Hub Repository

It may be necessary to clone the repository from GitHub to your local computer. Cloning the repository makes a copy of all the of repository data and takes it from GitHub to your local machine. The following steps, detailed below, should be taken to clone a repository:

1.	Navigate to the main page of the repository (in this case https://github.com/JoelineAlves/hair_manager).
2.	Select the button labelled Code.
3.	To clone the repo using HTTPS select the "HTTPS" option; to clone using an SSH key select the second option "SSH"; to clone using GitHub CLI select the third "GitHub CLI" option. Use the clipboard icon to copy the relevant information.
4.	Open Git Bash and change the working directory to the location where you wish the cloned repo to be stored.
5.	Use the git clone command and paste in the information copied in step 3 and Press Enter to create a local clone.
6.	If you wish to clone the repo to GitHub Desktop repeat steps 1 & 2 and from there select the "Open with GitHub Desktop" option.
7.	Follow the on-screen prompts from within GitHub Desktop (this option required GitHub Desktop to be installed to be successful).

(source: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

[Back to top](#table-of-contents)
___

## 6. Credits
### Content

* emailJS tutorial
https://www.emailjs.com/docs/sdk/send-form/
https://www.emailjs.com/docs/user-guide/auto-reply/


* Materializecss
https://materializecss.com/text-inputs.html


* Code Institute's Task Manager mini-project tutorial
https://codeinstitute.net/

* Code Institute’s tutorial for EmailJS was used for the Email functionality
Putting it all together > Sending Emails Using EmailJS > Sending Emails!



### Media

[websitemockupgenerator](https://websitemockupgenerator.com/) for creating the multi-device mockup.

https://unsplash.com/pt-br cards images

https://www.istockphoto.com/ cards images

### Acknowledgements


* My Brother, for him unconditional love, help and support in all aspects of life to make possible for me to work on this project.
* My family, for their valuable opinions and and critic during the design and development process.
* My mentor, Marcel, for their invaluable feedback and guidance.
* My Tutor, Rachel, for the all help and support.
* My friend Dorivaldo, for the all help and support.
* Codeanywhere support, to help resolve issues encountered.
* Heroku support, to help resolve issues encountered.
* Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.

[Back to top](#table-of-contents)
___