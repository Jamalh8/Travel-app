# Travel-app
An application to track travellers and destinations they've visited.

## Table of content 

[Project Introduction](#Project-Introduction)

[Designing the application](#Designing-the-application)

[Project tracking](#Project-tracking)

[Risk assesment](#Risk-assesment)

[Testing phase](#Testing-phase)

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

Project Management
Python Fundamentals
Python Testing
Git
Basic Linux
Python Web Development
Continuous Integration
Cloud Fundamentals
Databases

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

### Testing phase

Testing is a key element of the application production process. Testing allows me to check the codes that I have written and make sure that they are working. As this is not a full production app, that will be going live to customers, I'm not required to carry out any testing for performance or security. Therefore, I only carried out Unit testing and Selenium.  

I started off with using testing and was able to achieve a coverage of 97% of my code. The result of this can be seen on the image below.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/test-term-missing.png)

Once I was satisfied and successful with my test results I moved this over to Jenkins to carry out as part of my CI/CD pipeline. Using webhooks on Jenkins, everytime I ran a new build it would automatically carry out my tests. This allows me to focus on any changes to my application as Jenkins will automatically carry this out everytime I push changes up to GitHub. The HTML coverage from the jenkins machine can be seen on the below image.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/jenkins-html-cov.png)

However, as seen from the above image I'm still missing the 3 percent coverage. The code line 107-110 on routes was missing. To test this particular missing code I used selenium. I made 3 tests using selenium to which all 3 passed. The selenium tests that was carried out and the result can be seen from the images below.

#### Selenium test

The selenium test that was made.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/Selenium-test-show.png)

The result of the selenium test.

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/selenium-result-3test.png)

The selenium test can only be run on an Ubunti 18.04 machine. 
