> # Milestone Project for Code Institute - Full Stack Frameworks with Django Module - By Irina Nita
---
This project is an Issue Tracker build with Django. As it is clear from the name this web app is an issue tracker.
Easy to use and very efficient for team work. The web app itself is a demo version of the final product. By registering
to the demo version users can contribute to its improvement and give it a go to see its awesome features. Then they can purchase
this app  to make working on their own projects more efficient and clear for the entire team involved.

> Note : This is the initial version of the Readme file while the whole project is still at the beginning, so it may be subjected to
considerable changes until the final version. All the features and UX ar still to be implemented. 

## UX
There are two categories of users registered and not, both of them represent potential customers that may be buying the app.
* **NOT** registered users .Will be shown only the landing page with all the details and reasons why this app may be useful to them. They will be prompted to register and try out the app.
* **Registered** users. Will have access to all the web app's functionalities
* Carousel displayed for both users as registered users may not have yet purchase the product this may be a reminder and a prompt why they should
* Any action can be finalized in less than two steps
* Feedback is given at the end of important events through Alert Messages
* Navigation throughout the website is simple and intuitive
* Colour palette is meant to make content easily readable and eye pleasing, providing good contrast between text and background

[Wireframes](https://drive.google.com/drive/folders/1cM1__363xG0X4xwey0lbOpnczrzyhBps?usp=sharing)

[Main Colour Palette](https://coolors.co/ad343e-f2af29-235046-000000-e0e0ce)

### User Stories

1.  I am *NOT* registered yet and  I am looking for an issue tracker for my new project. I would like more information and a product that better suits my project's needs.
2.  I am a registered user and want to test the product:
* I would like to report bugs I come across wheter functional or design related
* I would also like to request features by opening a ticket or by voting an existing one
* I would like to know what feature will be implemented next and what bugs the dev team is currently working on
3.  I am a registered user and I have been using this app for a while now and decided to buy it to use it for my project
 

## Features

### Existing Features
1. Registration & login
2. View ticket list
3. Filter and sort tickets
4. Search through all the tickets based on a keyword
5. Comment on opened tickets
6. Open new tickets regarding bugs or feature requests
7. Vote bugs or features
8. Voting for features requires a small payment
9.  Checkout
10. Registered users can buy the app after they have tried the demo version
11. Password recovery. Users can recover their password, they receive an email with a link. following the link they can insert a new password

## Superusers/admins by accessing the admin panel
1. Can change ticket status from opened to closed
2. Can change ticket label or type in case it's been wrongly assigned based on the description

### Other Possible Features and Improvements
1. Update password


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

### Packages and modules

[Stripe](https://stripe.com/ie) - Used to securely process online payments

[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used for styling Bootstrap4 forms in Django

[Django Countries](https://pypi.org/project/django-countries/) - A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.

[Django Initial Avatars](https://pypi.org/project/django-initial-avatars/) - Django app which generates avatars based on username and initials

[Dj Database URL](https://pypi.org/project/dj-database-url/) - a package that allows us to connect to a database url, allow to use DATABASE_URL environment variable to configure our Django application.

[Whitenoise](https://pypi.org/project/whitenoise/) - allows to serve static files from Heroku without relying on other services

[Gunicorn](https://pypi.org/project/gunicorn/) - WSGI HTTP Server for UNIX

[AWS S3 services](https://s3.console.aws.amazon.com) - used to store media and static files in deployment  

[Django Storages](https://django-storages.readthedocs.io/en/latest/) - a collection of custom storage backends for Django

[Boto3](https://pypi.org/project/boto3/) -Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python to use of services like Amazon S3 

## Database

SQL Database that comes with Django for the development environment and Postgress in deployment. 

[Database Schema](https://dbdiagram.io/d/5ced18341f6a891a6a657c0a) - cloud database service for MongoDB databases



## Testing
### Form Testing
Ensure that all the case scenarios bellow trigger an error alert

####  Registration Form
* leave mandatory field blank
* insert input with a non valid format
* insert username that already exists
* insert not matching passwords

####  Login Form
* insert wrong username/password

#### Profile form
* insert avatar that has a non supported format
* insert avatar that doesn't match size requirements

#### Checkout
* insert non valid card number
* insert a past date for card expiry date
* insert non valid cvc

### Password recovery via mail
[Mailtrap](https://mailtrap.io/) -  Inspect and debug your email samples before delivering them to your customers. Used to test emails used for password recovery


## Version Control
Git is used for version control.  Commits made at any significant change

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


## Credits

> This Project has solely educational purpose

Inspired from
[1] [GitLab](https://gitlab.com/gitlab-com)
