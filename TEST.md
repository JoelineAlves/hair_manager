# Hair Styles Website - Joeline Alves
## Backend Development Milestone Project

## Testing

## Table of Contents

4. [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Testing User Stories](#testing-user-stories)
    - [Manual Testing](#manual-testing)
    - [Bugs & Fixes](#bugs-&-fixes)

## Code Validation

### W3C Markup Validator

All .html files were checked with the [W3C HTML Validator](https://validator.w3.org/) using the 'direct input' method.
These checks showed no errors and few warnings.

![W3C image](/documentation_TEST/html_validator.png)

The validator also highlighted missing head elements, illegal characters, missing lang attributes and no-space characters however these are due to use Jinga templating (see example below).

![W3C HTML image](/documentation_TEST/html_validator.png)


### CSS Validator

All CSS code was checked with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) using the 'direct input' method. No errors found.

![W3C CSS image](/documentation_TEST/cssvalidator.png)


### JSHint Validator

The script.js was checked with the [JS Hint](https://jshint.com/). No errors found. 

![jshint image](/documentation_TEST/js_validator.png)

Also the sendEmail.js was checked. 

![jshint email image](/documentation_TEST/sendemails_validator.png)


### PEP8 Validation

PEP8Ci was used to validate the python code used in the app.py file. Some errors were detected, such as whitespaces, over-indented and blank lines.
These errors have all been duly corrected.

![PEP8CI image](/documentation_TEST/python_validator.png)


## Lighthouse

Responsivity tests were carried out using Google Chrome DevTools throughout the project.
The site has been run through the Lighthouse test on Google Developer Tools and achieved the following results:

Home Page <br>
![lighthouse](/documentation_TEST/lighthouse_web.png)


___

## Manual Testing

* The site was tested on Google Chrome and Microsoft Edge for desktop and Chrome on mobile and tablet.

* It was tested using Google Developer Tools on the following devices:
    * iPhone SE
    * iPhone XR
    * Pixel 5
    * Samsung Galaxy S8+
    * iPad Air
    * iPad mini

* The site was responsive on all browsers and all devices.

___

## Testing User Stories

As a first time user, I want to:
* be able to view the site clearly on any device. 
    - testers reported that the site was responsive on their devices.
* be able to easily navigate around the site.
    - Friends and family reported that the site was easy to navigate around.
* be able to search for hairstyles.
    - All users can access the search tool regardless of whether they have an account. 
* be able to sign up to the site quickly.
    - testers reported that they found signing up easy and quick.
* be able to add and edit a hairstyles.
    - all testers reported being able to add and edit a hairstyle easily.
* know that my hairstyles are protected from other people editing or deleting them.
    - testing showed that hairstyles could not be deleted by different users.
* be able to send the site owner a message.
    - the contact form sends emails and the user received modal with the message that the email was successfully sent.
* be able to sign out of my account.
    - testers confirmed they could sign out.


### Frequent User Goals

As a returning user, I want to 
* be able to view the site clearly on any device.
    - testers reported that the site was responsive on their devices.
* be able to sign back into my account quickly.
    - all users confirmed they could sign back in quickly. Some users suggested the ability to reset their password, which would be implemented in future.
* be able to search for hairstyles.
    - all testers were able to search for hairstyles based on their key words.
* be able to view my hairstyles in one place.
    - the profile page was accurate for all testers.
* be able to add my own hairstyles.
    - testers confirmed they could add their hairstyles successfully.
* be able to edit my own hairstyles.
    - testers confirmed they could edit their hairstyles successfully.
* be able to delete my own hairstyles.
    - testers confirmed they could delete their own hairstyles and not those from others.
* know that my hairstyles are protected from other people editing or deleting them.
    - testers confirmed their hairstyles had not been deleted by others.
* be able to sign out of my account.
    - Testers confirmed they could sign out successfully.


### Administrator Goals

As an administrator of the site, I want to be able to:
* view the site clearly on any device.
    - testers reported that the site was responsive on their devices.
* sign back into my account quickly.
    - admin testers confirmed they could sign back in quickly.
* edit all hairstyle categories if necessary.
    - admin testers confirmed they could edit hairstyle categories.
* delete all hairstyle categories if necessary.
    - admin testers confirmed they could delete all hairstyle categories individually.
* add new  hairstyle categories.
    - admin testers confirmed they could add new hairstyle categories.
* edit  hairstyle categories.
    - admin testers confirmed they could edit hairstyle categories.
* delete hairsstyle categories.
    - admin testers confirmed they could delete hairstyle categories.
* receive email messages from site users.
    - admin testers confirmed they could receive messages via the form.

___

## Manual Testing on Mobile and Desktop Devices

### Nav Bar

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Hairstyles Logo | redirect user to home page when clicked | clicked title | redirected to home page | pass |
| Home page link | redirect user to home page when clicked | clicked link | redirected to home page | pass |
| contact us link | redirect user to contact page when clicked | clicked link | redirected to contact page | pass |
| log in link | redirect user to log in page when clicked | clicked link | redirected to log in page | pass |
| sign up link | redirect user to sign up page when clicked | clicked link | redirected to sign up page | pass |
| log out link | log user out of session and redirect user to home page when clicked | clicked link | user logged out of session and redirected to home page | pass |
| profile link | redirect user to profile page when clicked | clicked link | redirected to profile page | pass |
| New Hairstyle link | redirect user to add hairstyle page when clicked | clicked link | redirected to add hairstyle page | pass |
| manage Categories link | redirect user to manage categories page when clicked | clicked link | redirected to manage categories page | pass |

### Footer

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Social media links | link open browser window and go to correct site when clicked | clicked link | New browser window opens for each link clicked. Links redirect to the correct sites. | pass |

### Cards area

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Cards area | Cards area resizes on mobile devices | opened site on mobile device | Cards area resizes as expected | pass |


### Home Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Search bar | search is performed when user enters a search term. | searched for clip-in, braids, wigs, micro | The search returned cards containing the search term. | pass |
| Search bar | Message appears to inform user there are no search results when search is performed without a matching search term. | searched for cookie, chocolate, dori, abna, git | The search returned the error message. | pass |
| search button | Performs search when button is clicked. | clicked button | Search successfully performed | pass |


### Profile Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Users site hairstyles | Profile page displays all of the user's hairstyles | clicked on Profile hyperlink on Nav Bar | redirected to Profile page, hairstyles cards displayed  | pass |
| Username  | Username displays in title  | logged in and went to Profile page | Username displayed in title | pass |
| Edit button | redirects to edit card id hairstyle | clicked button | redirects to correct card id hairstyle to edit | pass |
| Delete button | redirects to delete modal | clicked button | redirects to delete modal | pass |


### Add hairstyle Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless user is logged in | stayed logged out | hyperlink hidden | pass |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Category input | dropdown list should appear | clicked dropdown icon | category drop down appeared | pass |
| Date input | Should open date picker | clicked on input field | datepicker appeared | pass |
| Add hairstyle button | add hairstyle to database | clicked add button | hairstyle added to database | pass |


### Manage Categories Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless Admin user logged in | logged in as non-admin user | hyperlink hidden | pass |
| Add categories button | redirect to Add Categories page | clicked add button | redirected to Add Categorie page | pass |
| Edit button | redirects to edit categorie id page | clicked button | redirects to correct categorie id to edit | pass |
| Delete button | redirects to delete modal | clicked button | redirects to delete modal | pass |

### Add Categories Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless Admin user logged in | logged in as non-admin user | hyperlink hidden | pass |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| cancel button | redirect to Manage Categories page | clicked cancel button | redirected to Manage Categories page | pass |
| Add categories button | add categories to database | clicked add button | categories added to database | pass |

### Edit Categories Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Access to page | page should not display unless Admin user logged in | logged in as non-admin user | hyperlink hidden | pass |
| Form input | Should be prepopulated correctly for categorie id | checked prepopulated correctly | Correct categorie prepopulated | pass |
| cancel button | redirect to Manage Categories page | clicked cancel button | redirected to Manage Categories page | pass |
| Edit categories button | append categories name to database | clicked edit button | categories appended to database | pass |


### Register Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Form input - username & password | The field should be between 5-15 characters long  | enter less than 5 characters | tooltip indicates the field is invalid | pass |
| Form input - username & password | The field should be between 5-15 characters long  | enter more than 5 characters | tooltip indicates the field is invalid | pass |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Invalid username | Error message should display if username is already registered  | user pre-registered username | error message appeared | pass |
| Register button | add user to database | clicked Register button | user added to database | pass |
| Logn In hyperlink | redirect user to Log In page | clicked hyperlink | redirected to Log In page | pass |


### Log In Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Log In button | add user to session and redirects to Profile page. Flash message to welcome user | clicked Login button | user redirected to Profile page. Flash welcome message displayed | pass |
| Sign Up hyperlink | redirect user to Sign Up page | clicked hyperlink | redirected to Sign Up page | pass |

### Contact Us Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Form input | Should prompt user to enter input if left blank | left input blank and clicked send button | tooltip indicates the field needs completing | pass |
| Send button | Should send the form to the admin email account | completed form and clicked send button, checked admin mailbox | Email received containing information from form | pass |

### Delete Modal

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| delete hairstyles | hairstyle should be deleted from database | clicked delete | hairstyles deleted from database | pass |
| delete categories | categories should be deleted from database | clicked delete | categories deleted from database | pass |



___

## Bugs & Fixes

| Bug | How I solved the issue |
| :--- | :--- |
| Werzberg error showed Log out link not working  | On inspection the redirect in app.py was set to login rather than landing_page. Changed the redirect address. |
| Contact form wasn’t sending email |  Wrong setting saved for service, changed to correct service id. |
| Linting error for app.py - PEP8 warning: too many blank lines | deleted blank lines. |
| Linting error for app.py - PEP8 warning: trailing whitespace | deleted whitespace. |
| Linting error for app.py - PEP8 warning: no newline at end of file | Added additional blank lines. |
| Linting error for app.py - PEP8 warning: blank line contains whitespace | deleted whitespace. |
| Delete app route not working | Added the missing @ in app route |
| Not redirecting to Login page when I tried to log in as an unregistered user | Change app route to return redirect(url_for("login")) |

___

Back to [README.md](README.md)

___