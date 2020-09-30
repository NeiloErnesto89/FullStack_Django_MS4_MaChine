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

My aim was pure simplicity. I wanted an aesthetically pleasing and functional site. I wanted to put into practice what I had learned throughout the course, focusing on the Pythonic backend functionality.

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
* As a user, I want to comment and interact with the site/application
* As a user, I want to see the other posts from other members of the community 

#### Admin

* As an admin, I would like to be able to edit and delete posts I see as unfit.
* As an admin, I would like to access the sites back office to remove any users who are not abiding by the sites rules


# Design 

#### Colour Scheme

I wanted to keep the colour schematic similar to my other projects, which all used the colour green heavily. I like the contrast it gives to the lighter elements of the page and in my opinion lends itself to aesthetically pleasing site, and therefore, easier on the eye for the user.

### **Wireframes**

Landing Home Page Wireframe - [View](https://github.com/)


# **Features**

## **Existing features**

The following features are divided up by page, detailing the logic behind each:

* Landing Page: 

* Cart App:
    For the cart section of the site, we utilise a contexts.py file. This file contains a function which dictate the logic of the cart section and this also ensures that the cart contents are available when rendering
    every page on the site. The cart items also don't go into the database. Cart items are stored in session when the use is logged in. A standard feature on e-commerce sites but an interesting adaptation nevertheless. It may also lend itself to reminding users that they have something in their basket that perhaps they want to purchase. However, when the user logs out, all the carts contents are lost. 


## **Features Left to Implement** 

Due to a mix up, I had less time than anticapted to finish up my project and so I feel there are plenty more features, both backend and frontend, that could be incorporated. 



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

### Landing paginate

** Pagination ** 

Settled on a view based function as opposed to class based pagination function.

https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html


- Bootstrap Comment Example 

https://bootsnipp.com/snippets/exz9y

## base.html layout

https://getbootstrap.com/docs/4.1/examples/sticky-footer-navbar/

https://stackoverflow.com/questions/11916297/django-detect-admin-login-in-view-or-template/11916391

On this StackOverflow post I found the logic for is_superuser

#### Humanize Numbers

[Humanize](https://simpleisbetterthancomplex.com/tips/2016/05/09/django-tip-2-humanize.html) is a really simple way to give data a bit of a 'human touch', so instead of `18 Sep 2020 20:54:31` into `2 days ago` using the template filter `| naturaltime` .

### Profile Page

The inspiration for the profile card style profile came from this [site](https://www.bootdey.com/snippets/view/about-me-profile#html) 

I also closely followed Corey Schafer's excellent [videos](https://www.youtube.com/watch?v=FdVuKt_iuSI&t=2s&ab_channel=CoreySchafer) and his code snippets came in [handy](https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/08-Profile-And-Images/django_project/users/views.py)   

I also used this to extend the User model by adding a [Profile model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)

#### Django Forms 

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

Django messages template example: 

https://stackoverflow.com/questions/16711917/django-message-template-tag-checking

#### AWS S3 Bucket Logic

[This article](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) helped me navigate the storage process on Amazon S3 for the Django Static and Media Files.

Also [this](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)


### Javascript/Bootstrap Carousel 

I got my inspiration and code snippet for my landing page carousel [here](https://mdbootstrap.com/docs/jquery/javascript/carousel/). I loved the imagery and even though they are landscape as opposed to machine/electronics, I enjoy the juxtaposition of nature and electronics.