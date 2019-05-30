# Milestone Project for Code Institute - Full Stack Frameworks with Django Module - By Irina Nita
---
This project is an Issue Tracker build with Django. As it is clear from the name this web app is an issue tracker.
Easy to use and very efficient for team work. The web app itself is a demo version of the final product. By registering
to the demo version users can contribute to its improvement and give it a go to see its awesome features. Then they can purchase
this app  to make working on their own projects more efficient and clear for the entire team involved.

> Note : This is the initial version of the Readme file while the whole project is still at the beginning, so it may be subjected to
considerable changes until the final version. All the features and UX ar still to be implemented. 

## UX
There are two categories of users registered and not, both of them represent potential customers that may be buying the app. The UX is different for these two groups.
* *NOT* registerd users  
... will be shown only the landing page with all the details and reasons why this app may be useful to them. They will be prompted to register and try out the app.
* Registered users
... will have access to all the web app's functionalities
* Any action can be finalised in less than two steps
* Feadback is given at the end of important events
* Navigation throughout the website is simple and intuitive
* Colour palette is meant to make content easily readable and eye pleasing, providing good contrast between text and background 

[Wireframes](https://drive.google.com/drive/folders/1cM1__363xG0X4xwey0lbOpnczrzyhBps?usp=sharing)

[Main Colour Palette](https://coolors.co/ad343e-f2af29-235046-000000-e0e0ce)

### User Stories

1. I am *NOT* registerd yet and  I am looking for an issue tracker for my new project. I would like more information and a product that better suits my project's needs.
2. I am a registered user and whant to test the product
... * I would like to report bugs I come across wheter functional or design related
... * I would also like to request features by opening a ticket or by upvoting and existent one
... * I would like to know what feature will be implemented next and what bugs the dev team is currently working on
3. I am a registered user and I have been using this app for a while now and decided to buy it to use it for my project
 

## Features

### Existing Features
1. Registration & login
2. View ticket list
3. Filter and sort tickets
4. Search through all the tickets based on a keyword
4. Comment on opened tickets
5. Open new tickets regarding bugs or feature requests
5. Upvote bugs or features
6. Upvoting features requires a payment of 10 euros
7. Upvoting bugs is free
8. Registered users can buy the app after they have tried the demo version

### Other Possible Features and Improvements



## Technologies Used

### Front-end

HTML, CSS - for structure and styling purposes

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) & [jQuery](https://jquery.com/) - mostly components provided by `Bootstrap` were used,
in order to create interaction like alerts that could be closed, burger button that appears on
screen resize. Navigation links that highlight when a user is at the page that matches
href

[Bootstrap](https://getbootstrap.com/) - For a responsive layout & prebuilt components
  
[Google fonts](https://fonts.google.com/) - For additional fonts with particular styling

[Font Awesome](https://fontawesome.com/free) - For responsive and stylish icons

### Back-end

[Python](https://www.python.org/) - Used throughout this project for the whole logic.
Python is a programming language that lets you work quickly and integrate systems more effectively

[Django](http://flask.pocoo.org/) - Python Framework

[Stripe](https://stripe.com/ie) - Used to securely process online payments

## Database

SQL Database that comes with Django for the development environment and Postgress in deployment. 

[Database Schema](https://dbdiagram.io/d/5ced18341f6a891a6a657c0a) - cloud database service for MongoDB databases


## Testing



## Version Control
Git will be used for version control.

## Deployment
This Project was deployed with Heroku in the following way:
* Create Heroku account
* Login into Heroku from console `heroku login`
* Create a new empty App on Heroku as none was created before `heroku create` 
* Rename App `heroku apps: rename issue-tracker`
Run this command from App's Root. The empty Heroku Git repository is automatically set as a remote for your local repository.
Check `git remote -v`
* Create a `Procfile` (instruction to Heroku as which file should be used as an entry point for our App)
The `Procfile` must be in your app’s root directory `echo web python app.py > Procfile`
* Create a requirements.txt file `sudo pip3 freeze --local > requirements.txt`
* To deploy `git push heroku master`
* Set the `IP`,`PORT`, `SECRET_KEY` and any other environment variables in Heroku Account Settings


It is also possible to configure GitHub integration for a Heroku app, Heroku can automatically build and release (if the build is successful) pushes to the specified GitHub repo.
[Read more here](https://devcenter.heroku.com/articles/github-integration)

## Install Locally


## Credits - Recipes were taken from following websites 

> This Project has solely educational purpose

Inspired from
[1] [GitLab](https://gitlab.com/gitlab-com)

