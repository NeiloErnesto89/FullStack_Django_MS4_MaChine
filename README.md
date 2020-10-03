[![Build Status](https://travis-ci.com/NeiloErnesto89/FullStack_Django_MS4_MaChine.svg?branch=master)](https://travis-ci.com/NeiloErnesto89/FullStack_Django_MS4_MaChine)


<h1 align="center">Full Stack Frameworks with Django Milestone 4 Project</h1>  

[The project is live on this link.](https://machine-ms4-app.herokuapp.com/)

*For the **Code Institute testing purposes**, I suggest (at some stage) logging into the site as the **Admin**, using the following details*: 
- Username: **_test_**   
- Password: **_test_** 

*For the sake of testing, please all use **4242_4242_4242_4242** when entering credit card details when paying for products using [Stripe](https://stripe.com/en-ie)

# **Machine**

## Project Scope

### *Title: **Machine** - an electronics e-Commerce website and community*

This is a site aimed at electronics enthusiasts looking to interact with fellow members of the community, to write blog posts and potentially purchase some products.

### Technical Introduction 

The site is built using the [Django](https://www.djangoproject.com/) Framework. It is deployed via [Heroku](https://dashboard.heroku.com/) cloud hosting platform. Media and Static files are hosted via the [AWS S3 platform](https://aws.amazon.com/s3/). 

# **Table of Contents**

- [**Machine**](#machine)
- [**Project Scope**](#project-scope)
- [**UX**](#ux)
- [**Design**](#design)
- [**Wireframes**](#wireframes)
- [**Features**](#features)
	- [Existing features](#existing-features)
	- [Features left to implement](#features-left-to-implement)
- [**Site Layout**](#site-layout)	        
- [**Technologies used**](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Other Programs Used](libraries-and-other-programs-used])
- [**Testing**](#testing)	
    - [Validation](#validation)
- [**Bugs**](bugs)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
	- [Content](#content)
	- [Media](#media)
	- [Acknowledgements](#acknowledgements)


## **UX** 

My aim was offer the user a smooth and logical experience, focusing on  simplicity. I wanted an aesthetically pleasing and functional site. I aimed to put into practice what I had learned throughout the course, focusing on the Pythonic backend functionality, as well as cultivating my code.

### **User Stories**

The following section details the type of user experiences I wanted the users of the site to have:

#### First Time User

* As a first time user, I am want to navigate around the site easily
* As a first time user, if I am interested to do so, I would like to sign up for an account in a smooth and simple fashion
* * As a first time user, I want to access the site via any device

#### Returning User

* As a user, I am interested in electronics
* As a user, I want a smooth browsing experience 
* As a user, I want to access the application via any device I have access to (e.g. ipad, mobile phone. laptop (desktop))
* As a user, I want to comment, like and interact with the site/application
* As a user, I want to add my own posts and see the other posts from other members of the community 

#### Admin

* As an admin, I would like to be able to edit and delete posts I see as unfit.
* As an admin, I would like to access the sites back office to remove any users who are not abiding by the sites rules


# Design 

#### Colour Scheme

I wanted to keep the colour schematic simple, but a bit different compared to my other milestone projects, which all used the colour green heavily. This site I went for a grey tone to match the sort of mechanical colouring associated with machines and electronics. But I also dotted the site with red, blue, yellow and green (among others) - which can be considered a subtle ode to rainbow coloured electrical wiring. 



Over all, I like the contrast the dark grey colour it gives to the lighter elements of the page and in my opinion lends itself to aesthetically pleasing site, and therefore, easier on the eye for the user.

### **Wireframes**

Landing Home Page Wireframe - [View](https://github.com/)

I used the app [Balsamiq](https://balsamiq.com/) to build my wireframes. I find it to be a really intuitive and user friendly application, which allows a user to build, simply and efficiently, a wireframe. This allowed me to clearly visualize the structure and design of my project.

Here is my original desktop landing page wireframe. I wanted a really simple, efficient and clean design whereby the user can navigate easily: 


#### Wireframe 1

![home page](https://github.com/NeiloErnesto89/FullStack_Django_MS4_MaChine/tree/master/media/ReadMe_Docs/wireframe_desktop_landing1.png "Index.html Wireframe" )

*Figure 1. Index.html*


# **Features**

## **Existing features**

The following features are divided up by page, detailing the logic behind each:

**Landing Page:** 

**Cart App**:

- For the cart section of the site, we utilise a contexts.py file. This file contains a function which dictate the logic of the cart section and this also ensures that the cart contents are available when rendering
every page on the site. 

    The cart items also don't go into the database. Cart items are stored in session when the use is logged in. A standard feature on e-commerce sites but an interesting adaptation nevertheless. It may also lend itself to reminding users that they have something in their basket that perhaps they want to purchase. However, when the user logs out, all the carts contents are lost. 

**User Posts (Individual Posts):**

- I followed this tutorial to add the [like button functionality](https://www.youtube.com/watch?v=PXqRPqDjDgc&ab_channel=Codemy.com) and I feel it works quite smoothly and adds to the feel of a community. I could have also added the *dislike* button but I wanted to avoid any negative connotations on the site. 

    If the user has written the post themselves, they have the option to edit/update and/delete. If the user is on a post from another user, they do not have the option to edit or delete a post. The Admin reserves the write to edit and/delete any post they so choose. This is an important tenet of CRUD (Create, Read, Update and Delete) from the ux perspective as well as a site management point of view. The admin can remove or edit a post they feel is unsuitable or against the site regulations, for example.


## **Features Left to Implement** 

Due to a mix up, I had less time than anticapted to finish up my project and so I feel there are plenty more features, both backend and frontend, that could be incorporated. I focused more on the backend logic and making sure that the users could perform a variety of actions but here are some features that can be added in the future:

- I could have also added a user comment section/forum for each post, which would cultivate an interactive community (for example, on [StackOverflow](https://stackoverflow.com/), if a user is struggling on a topic or justs wants to know more about something, they could pose a question to the forum, hoping for a robust response). 

- 



# **Site Layout**

## Django Framework Logic 

I mainly followed the MVT (Model-View-Template) concept of Django as I found it to be the most clean and logical approach for my needs. [Check out more info on MVT here](https://medium.com/@jaychaturvedi18/a-brief-introduction-to-django-mvt-framework-8ef46cc321ab)

* Models 
 - The model creation is extremely important as it's the information going into the database. Which will be all the information we require from a user, for example, the Checkout app model. Each time we create a new model, we must migrate the data to ensure that [Model Definitions and the Database Schema are in Sync](https://realpython.com/django-migrations-a-primer/#:~:text=Without%20migrations%2C%20you%20will%20have,in%20sync%20with%20your%20models.)



# **Technologies Used** 

### **Languages**

-   [Python](https://www.python.org/)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://www.javascript.com/)


### **Frameworks**

-   [Django](https://www.djangoproject.com/)  

### **Libraries and Other Programs Used**

-   [Balsamiq](https://balsamiq.com/) was used to create my wireframes


# **Testing**

I tested the site in a number of ways, always attempting to incorporate a defensvie programming mindset. A good quote that summarise's this point, comes from this [blog](https://medium.com/swlh/2-defensive-coding-techniques-you-should-use-today-4225cacc1c29), which states:

> Defensive coding allows our software to behave in a correct manner, despite incorrect input

I tested the platform on a number of devices (ipad, iphone, android, laptop). And I always aim to *disrupt* the flow of the creature of project. I referred to the ever trusty [Real Python](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#types-of-tests) to guide me through some of the tests at the later stage of the project, when I had no access to the course content.



### **Validation**

-   [PEP8](http://pep8online.com/)
-   [JSHint](https://jshint.com/)
-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input+with_options) 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

## Analysing User Experiences 

Analysing User Experiences versus (expected) User Goals [from UX Section](UX)

## **Bugs**

I had a number of interesting and challenges bugs throughout the project. [Stack Overflow](https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete) as always proved very helpful with this error. I actually entered the `collectstatic` command in the terminal incorrectly (something like `collecstatic`) however the console returned an intriguing error: 
`product = models.ForeignKey(Product, null=False) TypeError: __init__() missing 1 required positional argument: 'on_delete'`. The fix proved to be simple however I thought it curious as the incorrect command gave feedback on a missing `arg` when using `ForeignKey` in the models.

Some reccuring bugs that had really simple fixes initally had me scratching my head, such as this Django error `AttributeError at /accounts/edit-profile/ 'str' object has no attribute 'fields'`. This was resolved from [this](https://stackoverflow.com/questions/25615753/attributeerror-str-object-has-no-attribute-fields-using-django-non-rel-on-g) discussion on Stack Overflow and it was simply a typo in the end, whereby I called the incorrect form name on the template (correction was `{{ profile_form | as_bootstrap }}` for example), however honing in on why and what's going wrong is critial. 

This error in fact lead to another, more [troubling error](https://stackoverflow.com/questions/56274132/exception-in-thread-django-main-thread)`Exception in thread django-main-thread:`. I have a little bit of experience with firing threads in my work and this error gave me a bit more trouble. I began by spot fixing the error feedback, which stated `ImportError: No module named 'django.core.urlresolvers'` so I removed the `reverse lazy` library and simplified it with `from django.urls import reverse` [following this discussion of Stack Overflow](https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers). However this lead to a game of cat and mouse, as with each change I got a new error relating to some import incompatiblity. However, through a bit more research I realised (and this is why Github version control is so important) that my Django version had been updated when I installed some new libraries, namely the `django-storages==1.10.1`, was the version that cause the error, thus resulting in a string of incompatiblities. So I simplied reinstalled an older version of `Django==1.11.29`and `django-storages==1.9.1`. Following that, I ran my runserver command in the terminal and it worked. 

*Amazon S3*:
- Plenty of minor bugs and issues stemmed from using the [Amazon S3 Buckets](https://aws.amazon.com/s3/). One interesting bug in particular was that, for testing, I was using an older bucket I created for the Django ecommerce app. As that app was uploaded to Heroku, despite the fact I had deleted the old contents, my new project was simultanelously runnings with 2 `style.css` files. It took me a while to figure out and rectify (by deleting the older, unused Heroku app). Frustrating but interesting nevertheless as Heroku had manage to maintain the deleted css file and simultanelously run it on my new app.

# Deployment 

Deploying the project is vital as it demonstrates the steps one needs to pass to get a functional site live>

### AWS S3 Bucket

#### Setting up the S3 Bucket

1. Go to [AWS](https://aws.amazon.com) and sign up for an account
2. Go to your profile and select [S3](https://aws.amazon.com/s3/) and create a bucket, giving it a title of your choice
3. Go to the *properties* tab and and select *static web hosting*
4. Go to the *permissions* tab and change the *CORS Config* (CORS = Cross Origin Resource String) to the following (snippet):
    ```
       <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```
5. Also in *permissions* section, change the *bucket policy* to the following (snippet) - making sure to add personal *bucket name*:
    ```
     {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<bucket-name>/*"
            }
        ]
    }
    ```
6. Click on **IAM** (Identity & Access Management i.e. how a user manages access), create a new *group*  and add your bucket to it.
7. Create a *new policy* (in the *group IAM*), to the JSON section and click *import managed policy*, choose "AmazonS3FullAccess" and select import. Make sure to replace the resource string **'*'**.
8. Click *review policy* and click *create policy*
9. Now add *policy* to *group*
10. Create a *user*, give *programmatic access*, choose a *group* and click *create*
11. Finally, make sure to download CSV file with the *access keys* and other important details.

### Adding AWS S3 to Django

This step enables the *Django* project to have access to the *S3 Bucket*. Public and Private keys must be added to the `settings.py` via the `env.py` so the static files can be moved to S3.

1. Install the necessary libraries and correct versions (depending on Django project version):

    ```
    sudo pip3 install django-storages==1.9.1
    sudo pip3 install boto3==1.12.31
    ```
2. To the `settings.py` file, add `storages` to **INSTALLED_APPS** section.

3. Then add the following  S3 bucket details to the `settings.py`:
    
    ```python
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'
    }
    
    AWS_STORAGE_BUCKET_NAME = '<bucket-name>'
    AWS_S3_REGION_NAME = '<region-name>'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_ACL = None # removes boto warning
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    ```

#### Adding the Media to AWS S3

1. Create a `custom_storages.py` with 2 classes for both Static and Media (files) locations. Underneath is the code snippet:

    ```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION

    ```
2. Next, you must go to the `settings.py` to configure the static and media files `location` and `storage`
    ``python
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    ```
3. Finally, in your Command Line Terminal, run the following command to push the static files to the S3 Bucket - `python3 manage.py collectstatic` 

### Heroku

I hosted the site on Heroku. To deploy my code, Heroku provided me with a straightforward process to faciliate this. 


### Deploy on Heroku


[Heroku](https://dashboard.heroku.com/apps) is a cloud platform that allows for *deploying, managing and scaling applications*. The aim of Heroku is the ease at which developers can 'get their apps to market'. 
The project is deployed via the master branch and hosted on Heroku. 

The following steps were taken to successfully deploy the project on the Heroku:

1. Create a New Application:

	- Very simply logging into my (already created Heroku account) and creating a new application on my Heroku profile - I named it *machine-ms4-app*
	- Some configuration is necessary, so going to the *resources* section, searching in the *add-ons* section for the **Heroku Postgres** DB, selecting the *hobby level*
	- Returning to *Gitpod*, in my `settings.py` file, I added my app `['machine-ms4-app.herokuapp.com']` to the `ALLOWED_HOSTS` list (which also contains my `['localhost']`)

2. Installing Heroku and the Application Dependencies:

	- In the Command Line Terminal in Gitpod (as it's online/virtual dev environment , I don't need to `cd` (change directory) to any particular path. For my terminal command line, 
	- I entered the following command > `sudo pip3 install --classic heroku`
	- After the download, a user can log in to their Heroku account with the following command > `heroku login` , followed by their user details
	- Next, I installed some libraries/dependencies - the first command I entered was `sudo pip3 install gunicorn==20.0.4`. `Guincorn` is a [Python WSGI HTTP Server](https://gunicorn.org/) used to connect servers and apps.
	- After, I installed > `sudo pip3 installpsycopg2==2.7.3.2`. [Psycopg ](https://pypi.org/project/psycopg2/) which is a Postgres SQL DB adaptor for python

3. Create Requirements.txt, add Libraries/Dependencies and Procfile:

	- The **requirements.txt** file is necessary to run the installed dependencies (above). The following command was used to create and commit these libraries > `$ sudo pip3 freeze --local > requirements.txt`. This command also updates the file, for example, if any other libraries were added.
	- A **Procfile** is necessary to direct the Heroku app to the file(s) that it needs to execute and run. I used the command > `echo web: python > Procfile` in the terminal to install the file a
	- This was followed by a simple command in the terminal to run the web process: `heroku ps:scale web=1` and the resulting Procfile file is populated with the code `web: gunicorn machine.wsgi:application` 
	- Also, as I was using [Amazon S3 Buckets](https://aws.amazon.com/s3/) to store and host my static and media files, I needed to add the key-value pair `DISABLE_COLLECTSTATIC=1` to my Heroku *config vars* 
	- And as I didn't want [Heroku running my `collectstatic` command on my behalf](https://devcenter.heroku.com/articles/django-assets), I used the command `heroku config:set DISABLE_COLLECTSTATIC=1` to disable the `collectstaic` section of the build.

4. Connecting the PostgresSQL Database to Heroku:
	
	- I ran the command > `sudo pip3 install dj_database_url` to install this package. This important as [dj_database_url](https://pypi.org/project/dj-database-url/) *"returns the Django database connection dictionary, populated with all the data specified in your URL"*
	- Then I updated my requirements.txt file, with the command > `sudo pip3 freeze > requirements.txt`
	- I added my `DATABASE_URL` value to to my `env.py` (along with all my other keys). It's important not pushed the `env.py` file to Heroku or Github so it's added to a `.gitignore` file. This is to avoid any security issues.
	- The next step is to `import dj_database_url` in my `settings.py` file. I also added the following (`if-else`) logic to ensure a DB connection (if my *PostgreSQL* Database was available for whatever reason, there's a fallback default Django Database *sqlite3*):
    
	```python
    	if "DATABASE_URL" in os.environ:
        	DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
    	else:
        	print("Database URL not found. Using SQLite instead")
        	DATABASES = {
            	'default': {
                	'ENGINE': 'django.db.backends.sqlite3',
                	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            	}
    	}

 	```

5.  Migrate Models and Create a SuperUser:

	- It's necessary to migrate all models to Heroku's PostgreSQL so I run, in the following order, these commands > 1: `python3 manage.py makemigrations` > 2: `ython3 manage.py migrate`
	- Then I ran the `createsuperuser` command to create an admin/super-user for the PostgreSQL database and my Django app.

6. Config Vars on Heroku:

	- Returning to Heroku platform, going into my app, I select the **Reveal Config Vars** section and add the necessary key-value pairs.
	- These values are stored on the `env.py` file but as they are not pushed to Heroku or Github, I needed to manually configure them in this section.
	- `env.py` file contains these values, as follows:
	
	    ```python
    		import os

    		os.environ.setdefault("SECRET_KEY", "<app-secret-key")
    		os.environ.setdefault("EMAIL_ADDRESS", "<admin-email-address>")
    		os.environ.setdefault("EMAIL_PASSWORD", "<admin-email-password>")
    		os.environ.setdefault("EMAIL_HOST_PASS", "<gmail-host-pass>")
    		os.environ.setdefault("DATABASE_URL", "<heroku-db-url>")
    		os.environ.setdefault("AWS_ACCESS_KEY_ID", "<aws-access-key-id>")
    		os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "<aws-secret-access-key>")
    		os.environ.setdefault("STRIPE_PUBLISHABLE", "<stripe-publishable>")
    		os.environ.setdefault("STRIPE_SECRET", "<stripe-secret>")
    	   ```

	- And same details were configured in the Heroku **Config Vars** section as below:
	![alt text](https://https://github.com/NeiloErnesto89/FullStack_Django_MS4_MaChine/blob/master/media/readme_img/heroku_vars.png "Config Vars")
		
7. Deployment:
	
	-  Finally, back on the Heroku page, I go to the *deploy* section, adding *GitHub* to deploy my heroku app to the Github repo
	- The final step is to enable *automatic deploys*, so that each time I push to GitHub, the updated version of the app is deployed to Heroku (except, as mentioned above, not the `collectstatic` command)

Sidenote: After configuring all of this, after any big changes or advancements on my code etc. I would push my code to the Heroku app (via GitPod) to check if it was functioning.  

# Credits

### Content

At the beginning of my project I had access to the course material, which guided me crafting the bones of the project. However, due to an unforeseen mix up, I was left to complete the course with 3 weeks less than I had originally planned for and no course material to refer to. This is not to bemoan this outcome, I am in fact, quite happy with the end result as I felt I managed to produce a piece of work that I can call my own, without leaning too much on the course material or any one source (bar [Stack Overflow](https://stackoverflow.com/) of course) :grinning: . The course material was, of course, a big help but it's more the satisfaction I derived from working on, and producing, something that feels very much like my own doing. 

That being said, the internet is an endless wealth of material, content, inspiration and snippets for a would-be developer to avail from, so here are all the points of reference I had for building my project: 


**Pagination** 

Settled on a view based function as opposed to class based pagination function.
[This blog](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) guided me very smoothly through this process. 


- This Bootstrap style [comment example](https://bootsnipp.com/snippets/exz9y) was used as the base for my user posts/comments but I did adapt it quite a bit in the end.

**base.html layout**

[footer example](https://getbootstrap.com/docs/4.1/examples/sticky-footer-navbar/)

- For my modals, I took some snippets from [this site](https://mdbootstrap.com/docs/jquery/modals/customization/) as I thought they looked really sleek and worked very well.


On this StackOverflow post I found the [logic](https://stackoverflow.com/questions/11916297/django-detect-admin-login-in-view-or-template/11916391) for the `is_superuser` templating 

**Humanize (Numbers):**

[Humanize](https://simpleisbetterthancomplex.com/tips/2016/05/09/django-tip-2-humanize.html) is a really simple way to give data a bit of a 'human touch', so instead of `18 Sep 2020 20:54:31` into `2 days ago` using the template filter `| naturaltime` .

**Profile Page:**

The inspiration for the profile card style profile came from this [site](https://www.bootdey.com/snippets/view/about-me-profile#html) 

I also closely followed Corey Schafer's excellent [videos](https://www.youtube.com/watch?v=FdVuKt_iuSI&t=2s&ab_channel=CoreySchafer) and his code snippets came in [handy](https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/08-Profile-And-Images/django_project/users/views.py)   

I also used this to extend the User model by adding a [Profile model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)


I refered quite often to the **[Django docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)** (here is the section on forms)

Another StackOverflow discussion resulting in a [Django messages template example](https://stackoverflow.com/questions/16711917/django-message-template-tag-checking)

**AWS S3 Bucket Logic:**

- [This article](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) helped me navigate the storage process on Amazon S3 for the Django Static and Media Files.

- Also, [this](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html) blog came in extremely handy more than once (in this case for Amazon S3)


**Javascript/Bootstrap Carousel:** 
- I got my inspiration and code snippet for my landing page carousel [here](https://mdbootstrap.com/docs/jquery/javascript/carousel/). I loved the imagery and even though they are landscape as opposed to machine/electronics, I enjoy the juxtaposition of nature and electronics.


**Delete Functions/Views:**

- some of the logic that I used for the delete user and delete (user) posts methods was adapted from this [StackOverflow post](https://stackoverflow.com/questions/33715879/how-to-delete-user-in-django)

**Acknowledgements**

A fellow Code Institute Student was a huge source of inspiration as their project was of such high quality. I referred to it at times when I was entertaining some ideas and looking for some solid logic. The size, scale and professionalism of this [project](https://github.com/JBroks/unicornattractor_issue_tracker) is really impressive. Excellent work!

## Media

## Acknowledgements