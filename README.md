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
* Carousel displayed for both type of users as registered users may not have yet purchase the product this may be a reminder and a prompt why they should
* Any action can be finalized in less than two steps
* Feedback is given at the end of important events through alert messages
* Navigation throughout the website is simple and intuitive
* Colour palette is meant to make content easily readable and eye pleasing, providing good contrast between text and background

### Wireframes
Initial wireframes are slightly different from the actual design. Some parts of the initial layout were 
improved or modified following the final goal of ensuring a better user experience:

* [Landing Page - Logged Users](https://irinas-issue-tracker.s3-eu-west-1.amazonaws.com/static/wireframes/dashboard_for_logged_users.png) :
    From the beginning it was thought to have a unique landing page.
    The initial design is now used to display information for logged users.
* During development it was decided to differentiate between logged and non logged users. 
Users that were not logged in would also have ad type cards with all the benefits and call to action on their
 [Homepage](https://irinas-issue-tracker.s3-eu-west-1.amazonaws.com/static/wireframes/landingpage.png)      
*[Navigation Bar](https://irinas-issue-tracker.s3-eu-west-1.amazonaws.com/static/wireframes/headers.png) : 
This sections was planned to have a design that will differ for logged and non logged users.
The actual design has more elements compared to the wireframe, it also displays user avatar and a cart.
* [Registration & Authentication](https://irinas-issue-tracker.s3-eu-west-1.amazonaws.com/static/wireframes/registrationauthentication.png)

    The following section are accessible only by *registered* users

    * [Add Ticket](https://irinas-issue-tracker.s3-eu-west-1.amazonaws.com/static/wireframes/addticket.png) 
    * [Ticket List](https://irinas-issue-tracker.s3-eu-west-1.amazonaws.com/static/wireframes/ticketslist.png)
    * [Ticket Details](https://irinas-issue-tracker.s3-eu-west-1.amazonaws.com/static/wireframes/ticketdetails.png)
    * [Checkout](https://s3.console.aws.amazon.com/s3/object/irinas-issue-tracker/static/wireframes/checkout.png?region=us-east-2&tab=overview)
    
There are also a number of pages that are similar to the previous those mentioned above:
* Form for password recovery. Has similar structure to login/registration form.
* Thank you page. A page that is loaded when a user successfully purchases the App. Contains an image with a link
to download app. This page wasn't initially included in the design. I decided to add it to the checkout process
in order to ensure a clear step by step experience.    


### Colour Palette
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
[Pillow](https://pypi.org/project/Pillow/) - Imaging Library for Python

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

`SQLite3` database, that comes with Django, was used in development environment and ` Heroku Postgres` in deployment.
More detailed information is provided in the *Deploying - Database Setup* section of this file 

[Database Schema](https://dbdiagram.io/d/5ced18341f6a891a6a657c0a) 


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

### Prerequisites
* Heroku account. If you don't have one, go [here](https://signup.heroku.com/) and create it
* Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Deploying
* Create a Heroku application for the current project: 
    * You can create one from `Heroku CLI`. More info [here](https://devcenter.heroku.com/articles/creating-apps)
    * Or you can do it directly from your `Heroku Account`
* Add all your environmental variables to `configuration variables` in Heroku. You can access those form your
`App's Dashboard` in `Settings`
* Create a `requirements.txt` file `pip freeze > requirements.txt` it could also be 
`pip3 freeze > requirements.txt` depending on the `Python` version
* Create a `Procfile`. It serves as an instruction to Heroku as which file should be used as 
an entry point for our Project. In our case `Procfile` content looks like this `web: gunicorn issue_tracker.wsgi:application`
    
> Note: The `Procfile` and `requirements.txt` must be in the project's root directory

It is also possible to configure GitHub integration for a Heroku app, Heroku can automatically build and release (if the build is successful) pushes to the specified GitHub repo.
[Read more here](https://devcenter.heroku.com/articles/github-integration)

#### Serving Static & Media files
For this project static and media files are served using Amazon Web Services - S3. 

> Why? If we only had to serve static files for our project, using `Whitenoise` would have serve our purpose. **BUT**
there is an issue when it comes to serving **MEDIA FILES**, Heroku dynos have limited life span, and when they die and 
get replaced, the files within them are lost.

##### Prerequisites

* The Heroku CLI . More information on how to do it here [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
* A Heroku application for the current project;
> Note: If you followed the Deployment step described above this requisites should be already met
* Django does not support serving static files in production. However, [Whitenoise](https://pypi.org/project/whitenoise/) 
was designed to help us with this. Install it with this command:
    * `pip install whitenoise`
    * You should also add it to the projects `MIDDLEWARE` section in `setting.py`:
    
    ```python
    MIDDLEWARE = [
        ...,
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
    ```
* As mentioned above we have to set up Django media handler to put the files somewhere permanent. For this purpose
 two Python packages were used: [Django Storages](https://django-storages.readthedocs.io/en/latest/) 
 and [Boto3](https://pypi.org/project/boto3/). 
     * Run the following command to install:
    `pip install django-storages boto3`
     * In `settings.py` add `storages` to the `INSTALLED_APPS`:
     ```python
     INSTALLED_APPS = (
      ...,
      'storages',
      )
     ```
           
* An AWS S3 bucket has been created. In order to do this:
    * Create an [AWS Account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
    * Create a [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

##### Setup in Heroku

* Add AWS credential as configuration variables in Heroku. You need to set up the following variables: 
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

##### Settings.py

* If you want, this is optional, add this to your common settings:
    ```python
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'
    }

    ```
    This will tell boto3 that when it uploads files to S3, it should set properties on them so that when S3 serves them,
    it'll include some HTTP headers in the response. 
    Those HTTP headers, in turn, will tell browsers that they can cache these files for a very long time.

* Add this code to your settings, changing the first four values accordingly:

    ```python
    AWS_STORAGE_BUCKET_NAME = 'BUCKET_NAME'
    AWS_S3_REGION_NAME = 'REGION_NAME'  # e.g. us-east-2
    AWS_ACCESS_KEY_ID = 'xxxxxxxxxxxxxxxxxxxx'
    AWS_SECRET_ACCESS_KEY = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
    
    # Tell django-storages the domain to use to refer to static files.
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'customstorages.StaticStorage'
    
    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'customstorages.MediaStorage'
    
    ```
    Add `customstorages.py` to the project's root directory with the following code: 
   
    ```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    
    # Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
    # you run `collectstatic`).
    
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION

    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION

    ```
*  Now upload your static files to S3 using `collectstatic` command:
`python manage.py collectstatic`

    #### Database Setup
* You also need to setup your database. You can use `sqlite3`that comes with django for development and `Postgres` in
production. In order to setup `Postgress` in Heroku you should:
    * Access your app and go to `Resources Tab` and look for `Heroku Postgres` in `add-ons`
    * You need to setup your `settings.py` accordingly. In this case:
    
    ```python
    if "DATABASE_URL" in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    else:
    print('Postgress URL not found, using sqlite instead')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```
> Remember to add your `database url` to Heroku `config variables` with all the other environmental variables

* After linking our `Postgres` database we need to migrate everything `python3 manage.py migrate` and because this
 database is totally new we need to create a superuser `python3 manage.py createsuperuser` from `Heroku CLI`
 
* Normally you would also need to install `dj-database-url`,a package that allows us to connect to a database url,
 and `psycopg2` but these packages should be alreay installed
 after the `requirements.txt` installation

## Install Locally

### Prerequisites
* An IDE. I used [Pycharm](https://www.jetbrains.com/pycharm/) but any other IDE will work fine
* You should also have installed the following:
    * PIP
    * Python 3. I also used [Pyenv](https://github.com/pyenv/pyenv) for Python versioning
    * Django. The version I used is 1.11
    * Git
* CD to the directory of your choice on your local machine and clone the repository from the terminal:
    `git clone https://github.com/irinanita/issue-tracker.git`    
    **OR** You can save a copy of the github repository located  [here](https://github.com/irinanita/issue-tracker)
     by clicking the `download zip` button at the top of the page and extracting the zip file to your chosen folder.
* CD to the directory were you are planning to run the project. You need to create a virtual environment. I used
[Virtualenv](https://virtualenv.pypa.io/en/latest/):
    * `pip3 install virtualenv`
    > Note that you might have `pip` in the command
    * `virtualenv venv` where `venv` is a name of your choice for the directory where the virtual environment will be 
    created
* Install all the requirements `pip install -r requirements.txt`
* Create a file named `env.py` were you will store all the environmental variables
* Run project `python3 manage.py runserver localhost:PORT`. Remember to add your `HOST` to the `ALLOWED_HOSTS` in
`settimgs.py`

> Ensure that env.py is also added to .gitignore as you don't want this information to be public 
    
## Credits

> This Project has solely educational purpose

Inspired from
[1] [GitLab](https://gitlab.com/gitlab-com)
