# *Sewing Squad* 


![Overview](./sewingsquad/static/images/readme_docs/responsive_design.PNG)


Link to the page: [Sewing Squad](http://sewing-squad-a989d3fdde75.herokuapp.com/)


# Project Overview


Sewing Squad is a friendly community of people who share the same passion for sewing, making their own clothes. They desire to combine their skills together with those of others to not only become better seamsters/seamstresses themselves but to help others reach their potential. 

The platform facilitates /enables the members to share their patterns, sewing instructions and advice/tips on making the garment more customised/ to alter the garments to fit their style. The squad consists of members of variety of ages and experience levels.



# Project objectives


## User Goals


* Find people who share the same interest
* Get inspiration from other people’s creations
* Store my work  
* Post some of my work for others to see
* Help others with their sewing journey 


## Site Owner Goals


* Build a community of people who are passionate about sewing
* Enable users to share their sewing projects with others
* Enable users to save their own projects
* Encourage people to register (plant charge for membership in the future)
* Make it easy for users to navigate across the site


# User Experience


## User Stories


### Target user


* People who are interested in sewing 
* People who want to get some ideas for their sewing projects
* People who like fashion 
* People who like making their own clothes
* People who want to share their ideas with others
* People who want to learn hot to make new clothes 
* People who want to improve their sewing skills




### First Time Visitor Goals


1. I want to be able to see what this website is for
2. I want to have my own account with my entries
3. I want to be able to create my own account easily
4. I want to see a confirmation when my account gets created
5. I want to be told clearly what information is needed for registration
6. I want to know what my password should look like0
7. I want to be notified when I fill in something incorrectly or when missed something
8. I want to be able to add my own projects
9. I want to be able to see a list of other people’s projects
10. I want to be able to narrow the list of all the projects that are on the website to what fits my needs
11. I want to see a quick overview of the project to be able to decide whether that I would like to know more about that particular project 
12. I want to see image of the finished product 
13. I want to see more information on the projects that are interesting to me
14. I want to have an option to see more detailed description of project I choose
15. I want to be able to navigate through the website and find information easily 
16. I want to be able to navigate the site across variety of screen sizes
17. I want to be able to view the website on the variety of web browsers
18. I want the links to work when I click on them 


### Returning Visitor Goals


19. I want to be able to comment other user's posts and see what other people are commenting
20. I want to be able to log in to my account repeatedly
21. I want to be able to navigate the site across variety of screen sizes
22. I want to be given a confirmation that I am logged in 
23. I want to be able to view a list with projects I added
24. I want to be able to go to add a project directly
25. I want to be able to edit my projects
26. I dont want other people to edit my projects
27. I dot want other people to delete my project
28. I want to be able to delete my projects
29. I want to be able to quick find individual projects of interest
30. I want to be able to log out from my account when I finish working with it


### Site owner's Goals 

31.	I want to be able to control content on the webpage
32.	I want only registered users to be able to view full content
33.	I want users to create their account
34.	I want to store the user’s project entries in a database
35.	I want to be able to add categories user’s can chose from 
36.	I want the projects entries to be linked to each account
37.	I want users to see all the projects in database
38.	I want users to be able to read more details on the project of their choice
39.	I want users to see their own projects
40.	I want to be able to edit and delete categories 
41.	I want users to be able to edit their own projects
42.	I want users to be able to delete their own projects
43.	I want users to be able to understand what the website is for
44.	I want users to be able to navigate through the website easily


# Design

## Design choices

The site will be visited by people who sew for fun or professionally. The users are expected to visit the website with intention to present and share their work as well as help each other to find easier and more efficient ways to complete their projects. Threrore, the website design will be a mean of presenting each  Therefore, the design elements aim to make it easy to navigate through the site and find and read relevant information. 

## Color Scheme

The main colors of the website are pink and white. Lighter shades of pink are used for nagivation bar, footer and the title. Darker shades of pink were used to hightlight certain information such as project names or buttons. White color was used for text on pink background for better contrast while the rest of the text is in black. 

In addition to main colours, teal color was used for edit buttons and red for delete buttons in order to aid intuitive navidation. 

![Color Scheme](./sewingsquad/static/images/readme_docs/color_and_font/color_scheme.PNG)
## Typography

Google Fonts website was used to import the fonts chosen for this website.

Roboto was used as a general font for the website. Sacramento was used for logo in order to give a feel of embroidered letters. San seriff was added in case browser doesn't support the other two fonts. 

![Font Sacramento](./sewingsquad/static/images/readme_docs/color_and_font/font_sacramento.PNG)
![Font Roboto](./sewingsquad/static/images/readme_docs/color_and_font/font_roboto.PNG)
## Imagery

The images used by copying email addresses from etsy and other google search. Image addresses are saved in the database.

# Database Scheme & User Journey

## User Journey

![User journey legend](./sewingsquad/static/images/readme_docs/database_and_user_journey/user_journey_legend.PNG)
![User journey Part1](./sewingsquad/static/images/readme_docs/database_and_user_journey/user_journey1.PNG)
![User journey Part2](./sewingsquad/static/images/readme_docs/database_and_user_journey/user_journey2.PNG)



## Database Scheme 

![Database Scheme](./sewingsquad/static/images/readme_docs/database_and_user_journey/database_scheme.PNG)


# Features

## Register page 

### Registration Form
* Form is positioned in the middle of the screen
* Opens when user clicks Register link in the Login page or Log in link in navigation menu
* Form contains 3 input fields - username, email address, password
* Each input field has a label with information required for that field 
* Icons prefixed placed in front of each input field to aid intuitive navigation

![Register form](./sewingsquad/static/images/readme_docs/register_and_login/register.PNG)

* A form with empty fields will not be submitted and a message prompting the user to fill the field will appear 

![Register empty input fields](./sewingsquad/static/images/readme_docs/register_and_login/register_empty_fields.PNG)

* Information icon on the right side of the password field shows the password requirements  when hovered over 

![Regisrter information icon](./sewingsquad/static/images/readme_docs/register_and_login/register_information_icon.PNG)

![Registration toolpit](./sewingsquad/static/images/readme_docs/register_and_login/register_information_icon_toolpit.PNG)

* Register button  performs the registration and triggers the insertion of input data to database and  directs users to log in page
* Clear button will clear all the text in input fields

![Register form buttons](./sewingsquad/static/images/readme_docs/register_and_login/register_form_buttons.PNG)


* The message "This username already exists" informs the user that the username they entered is already in use and registration will not be successful 

![Duplicated user](./sewingsquad/static/images/readme_docs/register_and_login/register_duplicated%20user_text.PNG)

* Log in link is positioned at the bottom for quick navigation and directs the user to Log in page

![Duplicated user](./sewingsquad/static/images/readme_docs/register_and_login/register_login_link.PNG)

* Relates to following user stories: 3,4,6,7,33

## Log in page

### Log in Form

* Form is positioned in the middle of the screen
* Opens when user clicks Login link in the  Register page or clicks on Log In in navigation menu
* Form contains 2 input fields - username and password
* Each input field has a label with information required for that field 
*  Icons prefixed placed in front of each input field to aid intuitive navigation


![Log in form](./sewingsquad/static/images/readme_docs/register_and_login/login.PNG)

* A form with empty fields will not be submitted and a message prompting the user to fill the field will appear (see register section for more information)
* Information icon on the right side of the password field shows the password requirements  when hovered over (see register section for more information)
* Log in button triggers the validation of the password and username
* Clear button will clear all the text in input fields

![Log in button](./sewingsquad/static/images/readme_docs/register_and_login/login_form_buttons.PNG)

* The message "Incorrect Username and/or Password" informs the user tha the log in was not successful

![Log in error message](./sewingsquad/static/images/readme_docs/register_and_login/login_incorrect_username_message.PNG)

* Register  link is positioned at the bottom for quick navigation and directs the user to the user to Registered page

![Log in successful ](./sewingsquad/static/images/readme_docs/register_and_login/login_successful.JPG)

* The message "Welcome + username" informs the user that the registration was successful and the user is redirected to My Projects page

![Log in error message](./sewingsquad/static/images/readme_docs/register_and_login/login_register_link.PNG)

* Relates to following user stories: 6,7,20, 22



## My Projects 

* My project page is visible only to logged-in user while home page is visible to everyone

###	Add Project button

* The button directs the user to Add project page

## Home page
### Hero image 

* Indicates to the user what the website is for
* Takes up about 1/3 of the sreensize to allow content hinting

### Title

* The company name, Sewing Squad, denotes that this website is for a community of sewers

### Slogan

* Serves to catch attention of the user and suggest that the website is for people who want to sew their own clothes and then wear it
### Search

* Allows users to find posts quickly
* The users can search by name, category or fabric type
* When the search is successful a message with the number of posts containing the search word
* When the search is not successful a message will appear informing the user that nothing was found for that word

##	Card

* Appears on My Projects and home page
* When hovered over, the card will get shadows
* Relate to following user stories: 9, 23, 37

### Card Image

* Shows the pictures added by the user
* When hovered over, the images changes
* Relate to following user stories: 12

### Card Content

* Contains title and short description
* Relate to following user stories: 11

### Card action 

* At the bottom of the card
* Contains two buttons with option to edit or delete the post
* Edit form button opens edit form (for more details see Edit Project Form section)
* Delete button opens delete form
* Relate to following user stories: 15

![Card](./sewingsquad/static/images/readme_docs/home_and_my_project_page/card.PNG)
![Card - hover effect](./sewingsquad/static/images/readme_docs/home_and_my_project_page/card-hover.PNG)

## Add Project Form

* It will open when user clicks on Add Project link in nav bar or add project button in My Project page
* It contains 10 input fields
* There is one field with drop down selection option and the rest gets filled up by typing values in. 
* Labels and icons aid intuitive navigation for better user experience

![Add project part 1](./sewingsquad/static/images/readme_docs/add_project/add_project.PNG)
![Add project part 2](./sewingsquad/static/images/readme_docs/add_project/add_project2.PNG)

* Helper text prompts the user to separate each instruction step with full-stop

![Helper text](./sewingsquad/static/images/readme_docs/add_project/helper_text.PNG)

* A form with empty fields will not be submitted and a message prompting the user to fill the field will appear (see register section for more information)
* The project name must be unique in order to prevent duplicated entries. The users who use existing project name will get notified by flash message: "This project already exists.."

![Duplicted project name](./sewingsquad/static/images/readme_docs/add_project/duplicated_project_name.PNG)

* Add Project button will perform the upload of data to database
* Back button will take the user back My project page

![Duplicted project name](./sewingsquad/static/images/readme_docs/add_project/add_project_button.PNG)

* Relates to following user stories: 3, 7, 8, 15, 18, 23, 24, 34, 36


## Edit From

* Opens when user clicks on Edit button at the bottom of card in Home or My Project Page 

![Edit project open button](./sewingsquad/static/images/readme_docs/edit_project/edit_project_open_button.PNG)

* It contains 10 input fields
* The input fields are pre-populated with current data for that project

![Edit project form part 1](./sewingsquad/static/images/readme_docs/edit_project/edit_project.PNG)

![Edit project form part 2](./sewingsquad/static/images/readme_docs/edit_project/edit_project2.PNG)

* Edit Project button will trigger the update the project data in database when user clicks on it

![Edit Project button](./sewingsquad/static/images/readme_docs/edit_project/edit_project_button.PNG)

* The user will be notified when the project gets edit with flash message "Your project has been edited successfully and they will be redirected to My project page

![Edit Successful Message](./sewingsquad/static/images/readme_docs/edit_project/edit_confirmation.PNG)

* User must be logged in to edit the post and must be the owner of the post otherwise they will receive a flash message
* Admin can edit all the posts

![No permission to edit](./sewingsquad/static/images/readme_docs/edit_project/edit_no_permission.PNG)
![Must be logged in to edit](./sewingsquad/static/images/readme_docs/edit_project/edit_logged_out_user.PNG)

* Relates to following user stories: 3, 7, 15, 18, 25, 39, 41 

## Delete button

* Modal opens when user clicks on Delete button at the bottom of card in Home or My Project Page 

![Card Delete button](./sewingsquad/static/images/readme_docs/delete/delete_button_open_modal.PNG)

* Users can only delete their own posts. If user tries to delete someone else's post the flass message notifying them will appear 

![No permission to delete ](./sewingsquad/static/images/readme_docs/delete/delete_modal_no_permission.PNG)

* When the delete button is clicked, a user will be prompted to confirm whether they want to delete the post 
* When user clicks Yes button they the post will be deleted and they notified about it with flash message saying
* When user clicks No button they be redirected back to Home or My project page

![Confirm deletion ](./sewingsquad/static/images/readme_docs/delete/delete_modal_confirm_deletion.PNG)
![Delete successful](./sewingsquad/static/images/readme_docs/delete/delete_successful.PNG)

* Admin can delete all the posts
* Relates to following user stories: 27, 28, 31, 42

## Project page

### Content 
* Contains project image, description and details instrutions 
* The above sections will get bellow each other on smaller devices 
* Image will change when next or previous button are clicked
* Relates to following user stories: 27, 28, 31, 42

![Project page large devices](./sewingsquad/static/images/readme_docs/project/project_page.PNG)
![Project page large devices second picture](./sewingsquad/static/images/readme_docs/project/project_page_second_image.PNG)

![Project page small devices](./sewingsquad/static/images/readme_docs/project/project_page_small_devices.PNG)
![Project page small devices](./sewingsquad/static/images/readme_docs/project/project_page_small_devices2.PNG)

### View All projects or My projects button

* View All projects button directs user to Home page
* View My projects button directs user to Home page
* Relates to following user stories: 15, 18

![Project page](./sewingsquad/static/images/readme_docs/project/project_page_navigation_buttons.PNG)

### Comment 

* User can add, edit and delete comment 
* Edit and delete button are shown as icons 
* Add function has it's own secion with input field
* Users comment will appear under the project content


![Project comment section](./sewingsquad/static/images/readme_docs/project/project_page_comment.PNG)


* User will be notified when adding, editing will be successful

![Comment adding successful](./sewingsquad/static/images/readme_docs/project/comment_add_successful.PNG)
![Comment edit successful](./sewingsquad/static/images/readme_docs/project/comment_edit_successful.PNG)

* When the user clicks on delete icon a modal will appear asking them to confirm deletion
* When the user clicks "Yes" button the comment will get deleted and they will be notified about that with a flash message
* When the user clicks "No" button they will be redicrect to project page

![Project page](./sewingsquad/static/images/readme_docs/project/comment_delete.PNG)
![Project page](./sewingsquad/static/images/readme_docs/project/comment_delete_successful.PNG)

* Edit button will open a modal pre-populated with the current comment 

![Project page](./sewingsquad/static/images/readme_docs/project/project_page_comment_edit.PNG)

* Relates to following user stories: 19

## Categories (admin only)

* Only visible to admin
* Admin login details -> username: admin, password: adminss123
* Opens when admin click on Categories link in nav bar
* Contains a section where admin can add the category
* Containes a list of added categories 
* Admin can add, edit and delete categories
* Edit and delete button are shown as icons 

![Category](./sewingsquad/static/images/readme_docs/category/category.PNG)

* Admin will be notified when adding, editing of categories will be successful

![Category adding successful](./sewingsquad/static/images/readme_docs/category/categories_add_successful.PNG)
![Category edit successful](./sewingsquad/static/images/readme_docs/category/categories_edit_successful.PNG)

* When the user clicks on delete icon a modal will appear asking them to confirm deletion
* When the user clicks "Yes" button the comment will get deleted and they will be notified about that with a flash message
* When the user clicks "No" button they will be redicrect to project page

![Delete category modal](./sewingsquad/static/images/readme_docs/category/categories_delete.PNG)
![Delete successful](./sewingsquad/static/images/readme_docs/category/categories_delete_successful.PNG)

* Edit button will open in a separate page and input field will be pre-populated with text from database

![Edit ](./sewingsquad/static/images/readme_docs/category/categories_edit.PNG)

* Relates to following user stories: 31, 35, 40

## About page

* gives the user more details on what the website is for
* register link directs the user to register page so they can get started

![ About page ](./sewingsquad/static/images/readme_docs/about.PNG)

* Relates to following user stories: 1
 

## Log out

* is situation in the far right of the nav bar
* logs the user out of their account and notifies them with a flash message

![ Loggout ](./sewingsquad/static/images/readme_docs/logout.PNG)

* Relates to following user stories: 15, 18, 30, 32

## 404 and 505 error page

* Opens when user tries to access a website or data that doesn't exist
![ 404 and 500 error ](./sewingsquad/static/images/readme_docs/404_500_error.PNG)
* Relates to following user stories: 15, 18, 30, 32

## Logo and Navigations Bar

### Header
* Repeats across all pages for consistency and easy navigation
* Logo is positioned on the left size
* Logo brings user to the Home page when clicked
* Links to other pages are placed on the right to maintain the conventions expected by the user
* Navigation menu will turn into hamburger menu on smaller devices
* Hamburger menu opens to show list of other pages
* Relates to following user stories: 15, 18, 44


![Header desktop](./sewingsquad/static/images/readme_docs/header_and_footer/header_desktop.PNG)
![Header small devices](./sewingsquad/static/images/readme_docs/header_and_footer/header_small_devices.PNG)

### Footer
* Repeats across all pages for consistency and easy navigation
* Logo is centred in the middle
* Logo brings user to the Home page when clicked
* Links bring the user to the Github repositories or Linked in
* Links open in a new tab
* Links get bigger when hovered over for easier navigation
* Link description added for accessibility and SEO
* Relates to following user stories: 15, 18 

![Footer](./sewingsquad/static/images/readme_docs/header_and_footer/footer.PNG)






![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Veronika Nemergutova,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
