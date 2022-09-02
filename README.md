# Fred's Pizza

Fred's pizza is a popular family pizza restaurant that wants to expand their already successful business onto the online market. 

Therefore I have built a programme which allows the user to place an order online which gives Fred's pizza another avenue of making money.

This fully python written programme is run on a mock terminal.

![Am I responsive](/assets/am%20i%20responsive.PNG)

Live app: [Fred's pizza](https://freds-pizza.herokuapp.com/)

# Table of content

<!-- List of contents -->

# User experience

## User stories

As a user 

* I want to easily navigate my way through the programme to select my order
* Follow a chronological order that makes sense to order my pizza
* Tell me exactly what keys to enter and if I make a mistake, tell me what I done wrong
* Have simple instruction to follow 
* I want to know the prices of all options at every step not just at the end of the order
* I want a selection and variety of pizzas
* I want the options of ordering mutliple pizzas 
* Give me options to re-start my order before confirming if I selected anything wrong
* I want to know exactly how long it will take for my order to be made
* I want to recieve a receipt of excatly what I ordered

As the owner

* I want to provide a simple and easy way of ordering online
* I want a clear, easy to read spreadsheet of the data from the orders recieved

# Flow chart

I used [lucid flowcharts](https://lucid.app/users/login#/login) to help design the flow and outcomes of the project that the user while face depending on their decisions

The final programme may differ from the original flowchart displayed as development progresses

![Lucid flowchart](/assets/flow%20chart.PNG)

# Deployment

This project was developed through Gitpod, using Code Institue's mock terminal for Heroku and their way of linking to Google Sheet API.

## Deploy from GitHub

* Log into your GitHub repository
* Click 'Settings' in the main Repository menu
* Click 'Pages' from the left-hand side navigation menu
* Within the Source section, click the "Branch" button and change from 'None' to 'Main'
* The page should automatically refresh with a url displayed
* Test the link by clicking on the url

## Forking

* Navigate to the [Fred's pizzas](https://github.com/fredboys/freds-pizza)
* Click the 'Fork' button on the upper right part of the page.
* You will now have a fork of the Fred's pizzas repository added to your GitHub profile.

## Cloning

* Login to Github and go to my [Fred's pizzas](https://github.com/fredboys/freds-pizza)
* Above the list of files click the green ‘code’ button.
* This will bring up a few options as to how you would like to clone. You can 4. select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
* Open git bash
* Type ‘git clone’ and then paste the URL you copied. Press Enter.

## Create Data model spreadsheet

* Login to your Google account, create an account if necessary
* Navigate to Sheets, Googles version of Microsoft Excel
* Start a new spreadsheet, amend the title at the top i.e., Freds-pizza
* Create 1 Sheets titling it 'Orders' 
* In the first row of the Orders sheet, add the following column headers:
    * Name, Number, Pizza, Size, Quantity, Dip, Price, Time, Order No


## Set up API

Credit to [Jorgen Brattang](https://github.com/JorgenBrattang/daily-math) for the description

* Head to [Google cloud platform](https://console.cloud.google.com/) and sign in or create a free google account
* From the google cloud platform dashboard click 'Select a new project'. Then select 'New project'.
* Create a name for your project under 'Project name' then click 'Create'.
* This should bring up a box with your project in. Underneath click 'SELECT PROJECT'.
* From the sidebar navigate to 'APIs and services', 'Library'.
* In the search bar search for google drive.
* Select 'Google drive API' and click 'ENABLE'.
* Click the 'CREATE CREDENTIALS' button located to the top right of the page.
* From the dropdown menu under 'Which API are you using?' select 'Google drive API'.
* Under 'What data will you be accessing' choose 'Application data'.
* Under 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine or Cloud Functions?' select 'No, i'm not using them' and click 'NEXT'.
* Enter a Service Account Name. You can name it whatever you like. I would suggest naming it the same as what you named your project. Then click 'CREATE AND CONTINUE'.
* In the 'Role' dropdown menu select 'Basic', 'Editor', then click 'Continue'.
* The next page can be left blank so just click 'DONE'.
* Under 'Service Accounts' find the account you just created and click it.
* Navigate to the 'KEYS' tab and click 'ADD KEY', 'Create new key'. Select 'JSON' and click 'CREATE'.
* This will download a json file to your machine. This normally downloads into your 'downloads' folder but if you're unsure you can right click the file once it's downloaded and click 'show in folder' to locate it.
* Next we will have to link the Google Sheets API. To do this navigate back to the library by clicking on the burger icon in the top left hand corner and selecting 'APIs and services', 'Library' from the dropdown menu.
* In the search bar search for 'Google Sheets' and select 'Google Sheets API' and click 'ENABLE'.
* Now, using a programme like Gitpod open or create a repository.
* Drag and drop the json file that you downloaded earlier into your workspace. Rename this file to 'creds.json'.
* Open the file and copy the email address under 'client_email' without the quotation marks.
* Open up the google sheet you want to use and click the 'Share' button.
* Paste in the client email. Make sure 'Editor' is selected, untick 'Notify people' and then click 'Share'.
* To protect sensitive information be sure to add your creds.json file to your .gitignore file inside your editor.
* In order to use our google sheets API you need to install two additional dependencies into your project.
* Copy the following code on the first two lines of your workspace

![gspread](/assets/gspread.PNG)

* Below this, add the following code:

![scope](/assets/scope.PNG)

## Set up Heroku

Credit to [Jorgen Brattang](https://github.com/JorgenBrattang/daily-math) for the description

* The requirements.txt file in the IDE must be updated to package all dependencies. To do this:
    * Enter the following into the terminal: 'pip3 freeze > requirements.txt'
    * Commit the changes and push to GitHub
    
* Go to Heroku.com and sign in or create a free account.
* From the heroku dashboard click the 'Create new app' button.
* Name the app something unique and choose what region you are in then click 'Create app'.
* Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.
* In the field for KEY enter the value CREDS in all capitals. 
* In the field for VALUE copy and paste the entire contents of your creds.json file from your project. Then click 'Add'.
* In the field for KEY enter PORT in all capitals, then in the field for VALUE enter 8000. Then click 'Add'.
* Scroll down to the Buildpacks section and click 'Add buildpack'.
* Click Python then save changes.
* Add another buildpack by clicking 'Add buildpack' and this time click Nodejs then save changes.
* Make sure that Python appears above Nodejs in the buildpack section. If it does not you can click and drag them to change the order.
* Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
* From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
* Enter the repository name as it is in GitHub and click 'search'.
* Click the 'connect' button next to the repository to link it to heroku.
* To deploy, scroll down and click the 'Deploy Branch' button.
* Heroku will notify you that the app was successfully deployed with a button to view the app.
* If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.


# Credits

I used [Jorgen Brattang](https://github.com/JorgenBrattang/daily-math) for the description on how the deployment process of the API google sheet and Heroku went

I used [Stack overflow](https://stackoverflow.com/questions/14639077/how-to-use-sys-exit-in-python) for the code to allow the user to exit the system

![sys.exit()](/assets/sys.PNG)

![sys.exit()](/assets/exit.PNG)

I used [The web dev](https://thewebdev.info/2021/10/24/how-to-create-a-guid-or-uuid-in-python/?fbclid=IwAR16O6f7oQc62Uo-lG0VW7wzm-_6GxAsuMkFnzIb-5_cKQlTXUveOWsXGgg) for the code to generate a random code for my order numbers

![UUID](/assets/uuid.PNG)

![UUID](/assets/uuid.uuid.PNG)
