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

### Landing paginate

# Technologies Used 

* HTML
* CSS
* Django  
* Python


# Deployment 

I hosted the site on Heroku. To deploy my code, Heroku provided me with a straightforward process to faciliate this. 

** Pagination ** 

Settled on a view based function as opposed to class based pagination function.

https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html


** Bootstrap Comment Example ** 

https://bootsnipp.com/snippets/exz9y

## base.html layout

https://getbootstrap.com/docs/4.1/examples/sticky-footer-navbar/

https://stackoverflow.com/questions/11916297/django-detect-admin-login-in-view-or-template/11916391

On this StackOverflow post I found the logic for is_superuser


Django Forms 

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

Django messages template example: 

https://stackoverflow.com/questions/16711917/django-message-template-tag-checking