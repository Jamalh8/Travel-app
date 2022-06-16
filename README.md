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

## Project Introduction

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

## Designing the application

The first step was to come up with a model for my application. The miminum requirements for this project was to have a one-to-many database relationship. I pushed myself and decided to implement a many-to-many relationship for my application. 

My idea was that a user can visit many countries, but also be able to display all the users that have visited that particular country. It can be a great competition between users to see who has visited the most countries!

The entitiy relationship diagram demonstrates how I planned out my database models to acheive this. 

![alt text](https://github.com/Jamalh8/Travel-app/blob/dev/images/db-model.png "db-model")

In order to acheive the many-to-many relationship I used a join table named 'CountryVisit' which takes in user_id and country_id as the foreign key. This model was put into practice in python and the result of this is shown on the below image.


