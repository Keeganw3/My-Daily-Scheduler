# My Daily Scheduler
## Project Description
<p> My Daily Scheduler is a command line application to help you plan out what you would like to do in a day no matter what that may be!

The user can input all the activities they would like to do and the application will give them back to the user in a list for them to do as they please.
</p>

# Features
## Existing Features
## Welcome Screen
* The user is told what the program is and how to use it. After they hit enter it shows the main menu where the user is given all the options for what they can do with the daily planner in a straightforward and easy to read format.

![Screenshot](/assets/screenshots/welcome_screenshot.jpg)

## Main Menu
* The first 4 options are suggestions for their schedule and option 5 lets the user make their own option. The user can leave the program when they're on the menu by clicking 6.
![Screenshot](/assets/screenshots/main_menu_screenshot.jpg)

* When an option is chosen and placed in the list it is displayed a line space away from the choices to give the user better readability. The user will always be shown their current list everytime a task has been added to it. 
![Screenshot](/assets/screenshots/list_screenshot.jpg)

## Main Menu Validator
* The user is asked to enter a number from 1-6. If they use a number outside of this range an error is displayed which asks the user to pick a number within this range.
![Screenshot](/assets/screenshots/incorrect_num_screenshot.jpg)

* The user is given a similar response if they submit a letter instead of a number.
![Screenshot](/assets/screenshots/incorrect_variable_screenshot.jpg)

## User created options
* The user can make their own options to be added into their list plans for the day. The user can do this as many times as they want and the input can be as long as they desire to give full flexibility to the user.
![Screenshot](/assets/screenshots/create_options_screenshot.jpg)
 
* The user can exit this screen by typing 'exit'. This will not affect the user's list and they will be returned to the main menu. This gives the user a chance to go back to the main menu if they didn't mean to come to this screen.
![Screenshot](/assets/screenshots/exit_create_options_screenshot.jpg)

## Exiting Daily Planner
* Once the list has 3 tasks in it, the user is prompted to exit the daily planner by hitting "y" or "n". If they enter another key the code will tell them they hit the wrong key and ask them to put in "y" or "n". "y" or "n" can be put in with spaces or as capital letters to give the user more flexibilty when using the app.
![Screenshot](/assets/screenshots/exit_planner_screenshot.jpg)

* If they hit "y", they will leave the planner. They will have to hit enter to get to the End Results screen.
![Screenshot](/assets/screenshots/y_exit_planner_screenshot.jpg)

* If they hit "n" they can add another task and will be asked if they want to leave again every time they add a new task. They will have to hit enter once again to return to the main menu.
![Screenshot](/assets/screenshots/n_exit_planner_screenshot.jpg)

## End Results Screen
* This screen displays the full schedule that the user has made up for the day in a list so it is clearly visible and easy to find once you are done with the app.
![Screenshot](/assets/screenshots/end_results_screenshot.jpg)

# Future Features to be added 
## Time Allotments
* I would ike the user to be able to set these tasks to go on for a set amount of time to allow them to better plan out their day. They could also set a start and end time and try to work within these confines.

## Improved UI of End Results Screen
I would like the final display of the user's daily plan to be displayed one at a time on a line instead of all together in the list. I tried to make this a couple times but couldn't figure it out before submission.

# Technologies Used
## Languages Used
* Python

## Programs Used
* lucid.app: used to create the flowchart for this project.
screenshot()(detail?)
* Git: used for creating the code for this project and sending it to GitHub.
* GitHub: a repository for the code after being made in Git.
* Heroku: used to deploy the application and hosts a page for the code.

# Testing
## Validator Testing
### Python Testing
* No errors or warnings were found through the PEP8 online validator.
![Screenshot](/assets/screenshots/pep8_validator_screenshot.jpg)

## Known Bugs
When creating an option to be used the code will ask you for it twice. This doesn't happen if exit is used the first time the user is asked but if it is used when prompted the second time it will add this to the list. Using exit the first time won't add it to the list. I couldn't figure out why this problem happened.

# Deployment
This app was deployed using Heroku.
* Log into Heroku and make an account.
* In your gitpod code create a file called "requirements.txt" and add all of your code's dependencies to it.
* Go back to Heroku and click create new app. This app must have a unique name and a region.
* Now go to the Settings tab and scroll down to the Config Vars section. You will see two inputs called key and value.
* For the first key put CREDS and paste the contents of creds.json into value. 
* For the second key put PORT and "8000" into value.
* Scroll furthur down on this tab to Buildpack. 
* Click 'add Buildpack' and select Python. Do this again and select Node.js. Make sure Python is first and Node.js is second or it could affect your code.
* Go to the Deploy tab and you will see the deployment method, click Github. Enter the name of your repository and you will be given a list of the closest names that resemble what you have typed, click the one you want for this app.
* Scroll down to the Automatic Deploys section and click automatic deploy. This will make the app update to launch the latest cade that was pushed to Github everytime it is opened.
* You can also use Manual Deploy if this is the final version of your code.  
* Click Open App in the top right of the screen and the app should run.

## Forking
* Log into Github
* Load up the required repository.
* In the top right of the screen below the profile icon there is a fork button, click this.
* The repository should now be copied onto your Github account.

## Cloning
* Log into Github and choose a repository.
* Click on the green code button.
* You will be given three ways to clone the code. If you're using https, click “Clone with https” and copy the link.
* Open the terminal and type in the command "git clone" followed by a space and the copied url.
* The repository will now be cloned onto the computer.

# Acknowledgements

## Credits
* My mentor Brian Macharia who supported me and provided me with both feedback, examples and solutions to problems I faced while creating this project.
* Code institute for the classes, sources and tutors that they provided me.