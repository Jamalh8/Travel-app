# Travel-app
An application to track travellers and destinations they've visited.

## Table of content 

[Project Introduction](#Project-Introduction)

[Designing the application](#Designing-the-application)

[Project tracking](#Project-tracking)

[Risk assesment](#Risk-assesment)

[Unit Test](#Unit-Test)

[Selenium Test](#Selenium-Test)

[The application](#The-application)

[CICD Pipeline](#CICD-Pipeline)

[Known app issues](#Known-app-issues)

[Challenges faced](#Challenges-faced)

[Possible future changes to application](#Possible-future-changes-to-application)

[Conclusion and learning from this project](#Conclusion-and-learning-from-this-project)

[Credits](#Credits)

### Project Introduction

To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

This project will involve concepts from all core training modules; more
specifically, this will involve:

- Project Management
- Python Fundamentals
- Python Testing
- Git
- Basic Linux
- Python Web Development
- Continuous Integration
- Cloud Fundamentals
- Databases

### Designing the application

The first step was to come up with a model for my application. The miminum requirements for this project was to have a one-to-many database relationship. I pushed myself and decided to implement a many-to-many relationship for my application. 

My idea was that a user can visit many countries, but also be able to display all the users that have visited that particular country. It can be a great competition between users to see who has visited the most countries!

The entitiy relationship diagram demonstrates how I planned out my database models to acheive this. 

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/db-model.png "db-model")

In order to acheive the many-to-many relationship I used a join table named 'CountryVisit' which takes in user_id and country_id as the foreign key. This model was put into practice in python and the result of this is shown on the below image.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/db-model-python.png)

### Project tracking 

For project tracking I used Kanban board through Jira. I progressed my project through the use of tasks that I set myself based off the project requirements. 

I completed each tasks under a MoSCoW prioritisation. The MUST HAVE were completed first. Followed by the SHOULD HAVE. Finally a COULD HAVE task was also completed. There was one task to stop users entering in the same country more than once which I was unable to complete. This is something that I can work on for future developments. I have referenced pictures of my Jira Kanban board below to help visualise this process.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/kanban-1.png)

This shows the mid stage of my project where I've completed a fair amount of my tasks.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/kanban-2.png)

This shows the final Kanban board at the end of production. 

A link to my Kanban board can be found by clicking [here](https://jamalh-888.atlassian.net/jira/software/projects/TA/boards/5)

### Risk Assesment

A short risk assesment was also carried out prior to project start. The aim of the risk assesment was to consider possible challenges/issues and have mitigations in place, if possible, to reduce the impact of these risks. I have provided a diagram of the risk assesment that was carried out below.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/risk-assesment.png)

### Unit Test

Testing is a key element of the application production process. Testing allows me to check the codes that I have written and make sure that they are working. As this is not a full production app, that will be going live to customers, I'm not required to carry out any testing for performance or security. Therefore, I only carried out Unit testing and Selenium.  

I started off with using unit testing and was able to achieve a coverage of 97% of my code. The result of this can be seen on the image below.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/test-term-missing.png)

Once I was satisfied and successful with my test results I moved this over to Jenkins to carry out as part of my CI/CD pipeline. Using webhooks on Jenkins, everytime I ran a new build it would automatically carry out my tests. This allows me to focus on any changes to my application as Jenkins will automatically carry this out everytime I push changes up to GitHub. The HTML coverage from the jenkins machine can be seen on the below image.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/jenkins-html-cov.png)

However, as seen from the above image I'm still missing the 3 percent coverage. The code line 107-110 on routes was missing. To test this particular missing code I used selenium. I made 3 tests using selenium to which all 3 passed. The selenium tests that was carried out and the result can be seen from the images below.

### Selenium test

The selenium test that was made.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/Selenium-test-show.png)

The result of the selenium test.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/selenium-result-3test.png)

The selenium test can only be run on an Ubuntu 18.04 machine. My development VM was made using Ubuntu 18.04 hence why I was able to perform this test. However, both my Jenkins and deployment server are running on Ubuntu 20.04 hence why no selenium tests are carried out by my Jenkins VM.

### The application

This section will go through a brief overview of the application.

Upon entering home page, which is also the read page, the user will be greeted with the below page.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/app-home.png)

A navigation bar is visible at the top of the homepage with the options of 'Create Traveler', 'Enter Country', 'Add Country you visited', and 'See all Traveler(s) and Country, or Countries, they visited'.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/app-name-validator.png)

The 'Create Traveler' section allows the user to enter in the name, age, and gender of the traveler. If the user tries to enter in an traveler name that's already in the database then they'd be given a message to pick another name and the input is not commited to the database.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/app-country-validator.png)

The 'Enter Country' section allows the user to enter in the name of the country to the database. Again, if that country name already exists in the database then a customer validator is in place to inform the user and the country is not commited to the database.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/app-link-user-country.png)

Once there is a user and country entered into the database, the section named 'Add Country you visited' allows the user to pick a traveler and the country they visited.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/app-home-user-country-fill.png)

Once the user has picked the traveler, and country, they'll be shown on the home/read page. As you can see from the above image it'll show the traveler that visited the country and the visitors that country has received.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/app-read-all.png)

Finally, the above image shows the outcome when multiple travelers and countries are added to the application. You'll see multiple users that have visited the countries they've mentioned, along with the visitors these particular countries have received.

### CICD Pipeline

Kanban board from Jira was used as my project tracker. GitHub was used as my VSC (Version Control System). Jenkins was used as my CI/CD server. Jenkins was also used to deploy my application to a Google cloud platform VM via Gunicorn. A GitHub webhook was integrated with my Jenkins, everytime I pushed changes up to my repositry it'll trigger Jenkins to automatically test, build, and deploy the application via Gunicorn.

The below diagram explain the CI/CD pipeline that was implemented for my particular project. 

![alt text]()

A copy of a successful Jenkins build log can be found by clicking [here](https://github.com/Jamalh8/Travel-app/blob/dev/images/Jenkins-log.txt)

### Known application issues

* The only known issue within the application is the duplication of travelers visiting the same country more than once. For example, traveler "Dave" can enter that they've visited "Spain" more than once. This then creates duplicate output of "Dave" visiting "Spain" 2 times and with "Spain" having "Dave" visited it twice. 

An image of this issue can be shown below.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/app-duplication-error.png)

### Challenges faced

I faced many challenges during this project. However, there were some that were more noteable than others.

* Implemnting a many-to-many relationship. This was a challenge as I've ventured into the unknown without prior experience in this.
* Creating the application according to the tasks I set. I had to be flexible and carry out some tasks not in the order I originally set them as.
* Creating tests to achieve a high coverage.
* Using selenium to test the code that my unit test did not cover.
* Setting up environment variables to ensure there is no credentials leak.
* Using Jenkins with a webhook that automatically builds, test, and deploys application to a production environment.

### Possible future changes to application

If I was to work on this application in the future my first priority would be to fix the known issues that I've listed above. 

Secondly, I would seek to increase my test coverage to 100%, even though I used Selenium to test the missing coverage, I'd still like to get full coverage from the Unit test. 

Finally, I would plan to expand the application to have more information to display. 

- An idea I have would be to have a date the user has visited a country. Using details of the date it'd like to display the date they've visited a country and put them into cronological order. This way the user will be track when they visited the country.

- Another expansion idea would be to display if a country has been visited by 'Male, 'Female', or 'Other' traveler the most. 

- One final idea I also have, at this moment, would be to display users based on age range. This will allow us to see which age bracket has the most travelers.

### Conclusion and learning from this project

Overall, I'm very pleased with the outcome of this project. I'm proud that I've been able to implement a many-to-many relationship on my application. I ventured into the unkown and challenged myself. I was resilient and was not afraid to ask questions to things I had no or little knowledge of. 

This project has given me the confidence going forward to continue learning and enhance upon these new skills I've learned along the way. 

### Credits

I would like to thank Leon, Earl, and Adam for their support in helping me deliver this project.

