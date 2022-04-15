# Cornflake Test

## Python Essentials Project

<img src="./assets/images/responsive_screen_shot.png" alt="Website on different screen sizes" style="height: 400px; width: 730px">

The application is designed to return insights on survey result carried out on the current cereal customers buying habits.

### [View the live application on Heroku](https://cereal-survey.herokuapp.com/)

## Table of contents

- [UX](#UX)
    - [Business goals](#Business-goals)
    - [User goals](#User-goals)
- [Features](#Features)
- [Technology](#Technology)
- [Testing](#Testing)
    - [Code Validation](#Code-validation)
    - [Issues found during testing](#Issues-found-during-testing)
    - [Performance testing](#Performance-testing)
- [Deployment](#Deployment)
- [Credits](#Credits)
- [Screenshots](#Screenshots)

# UX

## Business goals

A survey of 3 questions was carried out on 20 cereal buying customers. The purpose of the survey is to see if there is potential room for a new brand to enter this market.

The questions asked were;

1. Which of the following brands do you buy?

Answer options were;

a) Kellogs 
b) Nestle 
c) Quaker 
d) Other brands 

2. Would you consider changing to a different cereal in the future?

Answer options were;

a) Yes 
b) No 

3. What do you consider when picking a new cereal?

Answer options were;

a) Price 
b) Packaging 
c) Box Size 
d) Healthier Option 

## User goals

The application is designed to give the user a recap of the question asked and then followed by some actionable insights based on the answers.

The user can then move onto the next question when they are ready to do so by pressing 'Enter'.

# Features

The application is a command line application.

There has been spacing added to help breakdown some of the text to make it easier for the user to absorb the information.

[Return to the table of contents](#table-of-contents)

# Technology

### Python

- The back end of the application is written in Python.

### HTML

- The HTML part of the application was developed by the Code Institute.

### CSS

- The CSS part of the application was developed by the Code Institute.

### Heroku

- Where the site is hosted.

### Google Sheets

- Where the data (answers from teh survey) are stored

### Github

- Where the repository for the app is stored.

### Gitpod

- Where the application was developed.


# Testing

## Code validation

The code was tested using pep8online.com with no errors or warnings.

<img src="./assets/images/online_pep8_check.png" alt="Screenshot showing the result of the pep8 test" style="height: 330px; width: 400px">

### Issues found during testing

When the app was deployed on Heroku, i didn't like that there was no padding betweent the forst character of the text in each line and the edge of the command line window. So 2 spaces were input to each text line, to help the user to follow the text.

### Performance testing

To check the user feedback to the data collected, the data was changed to test for accurate outcomes. There were a couple of errors found early on, for example if 100% of people would try a new cereal the app missed this as still gave a positive outcome (i.e. There is room for a new cereal).

These were modified an no further errors were found.

# Deployment

The application has been deployed on Heroku. In order to do this I carried out the following actions;

1. Click new

2. Click create new app

<img src="./assets/images/1_new_app.png" alt="Drop down box with option for 'Create new app'" style="height: 100px; width: 120px">

3. Entered the app name, confirmed my region and then pressed 'create app'. Note: The app name must be uique on Heroku

<img src="./assets/images/2_name_region.png" alt="Data entry fields for entering app name and reqgion" style="height: 150px; width: 320px">

4. Then clicked on 'settings' and created some 'config vars' - these are files / connection data that Heroku will use to build the app, but will not keep secure.

<img src="./assets/images/3_config_vars.png" alt="Text box explaining what config vars do" style="height: 100px; width: 220px">

5. Added 2 buildpacks - Python and node.js

<img src="./assets/images/4_buildpacks.png" alt="Buildpacks screenshot showing python and node.js buildpacks being included" style="height: 100px; width: 520px">

6. Clicked 'deploy' and then connected to Github by clicking on GitHub and following the instructions to find the repository.

<img src="./assets/images/5_github_connection.png" alt="Screenshot showing GitHub connected to Heroku" style="height: 130px; width: 520px">

7. Then scrolled down and clicked on manual deployment. This builds the app and shows the steps it is taking to do so.

<img src="./assets/images/6_manual_deployment.png" alt="Screenshot showing the option and button for manual deployment of the app" style="height: 130px; width: 520px">

8. Finally I clicked the view app button to test the deployment of the app and test run the app on Heroku.

<img src="./assets/images/7_view_app.png" alt="Screenshot showing the text 'Your app was successfully deployed and a button with the text 'view app' on it" style="height: 130px; width: 420px">

# Credits

This app was heavily influenced by the Love Sandwiches project. A lot of the code was taken and then modified from that project.

There were a couple of other areas where I got ideas for code to be used in this app;

w3schools.com
tutorialsteacher.com/python
stackoverflow.com

Although no code was directly lifted from these sites, I certainly did modify some code I found on there for my own needs in building this site.


# Screenshots

<img src="./assets/images/intro_screenshot.png" alt="Screenshot showing the deployed with the 'Intro' showing" style="height: 330px; width: 370px">

<img src="./assets/images/user_input_error.png" alt="Screenshot showing the deployed with a user input error" style="height: 70px; width: 330px">

<img src="./assets/images/question_1_screenshot.png" alt="Screenshot showing the deployed with question 1 recap and data" style="height: 330px; width: 370px">

<img src="./assets/images/question_2_screenshot.png" alt="Screenshot showing the deployed with question 2 recap and data" style="height: 330px; width: 370px">

<img src="./assets/images/question_3_screenshot.png" alt="Screenshot showing the deployed with question 3 recap and data" style="height: 330px; width: 370px">