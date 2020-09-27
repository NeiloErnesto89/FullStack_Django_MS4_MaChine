[![Build Status](https://travis-ci.com/NeiloErnesto89/FullStack_Django_MS4_MaChine.svg?branch=master)](https://travis-ci.com/NeiloErnesto89/FullStack_Django_MS4_MaChine)


<h1 align="center">Full Stack Frameworks with Django Milestone 4 Project</h1>  

[The project is live on this link.](https://machine-ms4-app.herokuapp.com/)

# Project Introduction

## Title: MaChine - electronics E-Commerce site and community

This is a site aimed at electronics enthusiasts looking to interact with fellow members of the community, to write blog posts and potentially purchase some products.


## UX 

My aim was pure simplicity. I wanted an aesthetically pleasing and functional site. I wanted to put into practice what I had learned throughout the course, focusing on the Pythonic backend functionality.

### User Stories

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


- # Design 

    - #### Colour Scheme

        - I wanted to keep the schematic 

### Wireframes

    -   Landing Home Page Wireframe - [View](https://github.com/)


## Features

* Landing Page: 

* Cart App:
    For the cart section of the site, we utilise a contexts.py file. This file contains a function which dictate the logic of the cart section and this also ensures that the cart contents are available when rendering
    every page on the site. The cart items also don't go into the database. Cart items are stored in session when the use is logged in. A standard feature on e-commerce sites but an interesting adaptation nevertheless. It may also lend itself to reminding users that they have something in their basket that perhaps they want to purchase. However, when the user logs out, all the carts contents are lost. 


## Features Left to Implement 

Due to a mix up, I had less time than anticapted to finish up my project and so I feel there are plenty more features, both backend and frontend, that could be incorporated. 



# Site Layout 

# Django Framework Logic 

I mainly followed the MVT (Model-View-Template) concept of Django as I found it to be the most clean and logical approach for my needs. [Check out more info on MVT here](https://medium.com/@jaychaturvedi18/a-brief-introduction-to-django-mvt-framework-8ef46cc321ab)

* Models 
 - The model creation is extremely important as it's the information going into the database. Which will be all the information we require from a user, for example, the Checkout app model. Each time we create a new model, we must migrate the data to ensure that [Model Definitions and the Database Schema are in Sync](https://realpython.com/django-migrations-a-primer/#:~:text=Without%20migrations%2C%20you%20will%20have,in%20sync%20with%20your%20models.)



# Technologies Used 

### Languages Used

-   [Python](https://www.python.org/)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://www.javascript.com/)
- 
### Frameworks

-   [Django](https://www.djangoproject.com/)  

### Libraries and Other Programs Used

-   [Balsamiq](https://balsamiq.com/) was used to create my wireframes


## Testing

#### Validators 

-   [PEP8](http://pep8online.com/)
-   [JSHint](https://jshint.com/)
-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input+with_options) 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

# Analysing User Experiences versus (expected) User Goals [from UX Section](UX)

# Bugs

I had a number of interesting and challenges bugs throughout the project. [Stack Overflow](https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete) as always proved very helpful with this error. I actually entered the `collectstatic` command in the terminal incorrectly (something like `collecstatic`) however the console returned an intriguing error: 
`product = models.ForeignKey(Product, null=False) TypeError: __init__() missing 1 required positional argument: 'on_delete'`. The fix proved to be simple however I thought it curious as the incorrect command gave feedback on a missing `arg` when using `ForeignKey` in the models.

This error in fact lead to another, more [troubling error](https://stackoverflow.com/questions/56274132/exception-in-thread-django-main-thread)`Exception in thread django-main-thread:`. I have a little bit of experience with firing threads in my work and this error gave me a bit more trouble. I began by spot fixing the error feedback, which stated `ImportError: No module named 'django.core.urlresolvers'` so I removed the `reverse lazy` library and simplified it with `from django.urls import reverse` [following this discussion of Stack Overflow](https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers). However this lead to a game of cat and mouse, as with each change I got a new error relating to some import incompatiblity. However, through a bit more research I realised (and this is why Github version control is so important) that my Django version had been updated when I installed some new libraries, namely the `django-storages==1.10.1`, was the version that cause the error, thus resulting in a string of incompatiblities. So I simplied reinstalled an older version of `Django==1.11.29`and `django-storages==1.9.1`. Following that, I ran my runserver command in the terminal and it worked. 

# Deployment 

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


#### Django Forms 

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

Django messages template example: 

https://stackoverflow.com/questions/16711917/django-message-template-tag-checking

#### AWS S3 Bucket Logic

[This article](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) helped me navigate the storage process on Amazon S3 for the Django Static and Media Files.

Also [this](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)