[![Build Status](https://travis-ci.com/NeiloErnesto89/FullStack_Django_MS4_MaChine.svg?branch=master)](https://travis-ci.com/NeiloErnesto89/FullStack_Django_MS4_MaChine)


<h1 align="center">Full Stack Frameworks with Django Milestone 4 Project 

<h2 align="center">Machine :robot: </h2>

## **Project Introduction and Brief**

### *Title: **[Machine](https://machine-ms4-app.herokuapp.com/)** - an Electronics e-Commerce website and community*

*Full Stack Frameworks Milestone Project - Django*

This is a site aimed at electronics enthusiasts looking to interact with fellow members of the community, to write blog posts and hopefully purchase some products.

Keeping in line with the CI project requirements as well as CRUD tenets, the site is aiming to incorporate, and expand on, what has been taught in the CI course. 


![Devices View](/media/ReadMe_Docs/Site_Devices_View.png "Site Devices View" )

### *Note for External Tester*

*For the **Code Institute testing purposes**, I suggest (at some stage) logging into the site as the **Admin/SuperUser**, using the following details*: 
- Username: **Neilo**   
- Password: **_test_** 

*Also, for the sake of further testing, please only use the test number **`4242_4242_4242_4242`** when entering credit card number when paying for products using [Stripe](https://stripe.com/en-ie)



# **Table of Contents**

- [**Project Introduction and Brief**](#project-introduction-and-brief)
- [**Demo**](#demo)
- [**Project Purpose and Scope**](#project-purpose-and-scope) 
- [**UX**](#ux)
- [**Design**](#design)
- [**Wireframes**](#wireframes)
- [**Database Schema**](#database-schema)
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


## Demo

[The project is live on this link.](https://machine-ms4-app.herokuapp.com/)

### **Project Purpose and Scope**

According to the *CI Assessment Handbook 2020*, the aim of this project is to:

> *build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service*

I aimed to stick to this overarching goal and the following section summarises what was needed in terms of requirements to complete the project. This excerpt was taken and shorten, from the **CI project requirements** documentation:

> 1.	Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
> 2.	Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
>3.	Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models...
>4.	User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so.
> 5.	User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism)...
> 6.	Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc...
> 7.	Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
> 8.	Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.
> 9.	Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
>10.	Version Control: Use Git & GitHub for version control.
>11.	Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
>12.	Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
>13.	Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.


### **Further Technical Insight** 

The site is built using the [Django](https://www.djangoproject.com/) Framework. Furthermore, the CI project had some more technical requirements to fulfill, including using the follow languages:

* HTML
* CSS
* JavaScript 
* Python (+ Django)

These languages needed to be utilised in tandem with a relational database management system (recommended either [MySQL](https://www.mysql.com/) or [PostgreSQL](https://www.postgresql.org/)). The site is deployed via [Heroku](https://dashboard.heroku.com/) cloud hosting platform. Media and Static files are hosted via the [AWS S3 platform](https://aws.amazon.com/s3/). The site has the [Stripe](https://stripe.com/ie) payment system software fully integrated. As well as numerous additional libraires and API's dotted and employed throughout the site.



# **UX** 

My aim was offer the user a smooth and logical experience, focusing on  simplicity. I wanted an aesthetically pleasing and functional site. I aimed to put into practice what I had learned throughout the course, focusing on the Pythonic backend functionality, as well as cultivating my code.

### UX Target Audience

My target audience would be users who are interested in electronics as a hobby. This is an all-encompassing subject but particularly in my case it's been helpful of my coding journey as I found using a Raspberry Pi (minicomputer) allows the user to learn about electronics and programming in a real fun and intuitive manner. 

### **User Stories**

The following section details the type of user experiences I wanted the users of the site to have:

#### First Time User

* As a first time visitor, I want to navigate around the site easily
* As a first time visitor, I want to learn quickly what the site is about and what benefits a user can avail of
* As a first time visitor, if I am interested to do so, I would like to sign up for an account in a smooth and simple fashion
* As a first time visitor, I want to access the site via any device

#### Returning/Frequent User

* As a frequent user, I am interested in electronics and want to learn a bit more
* As a frequent user, I want a smooth browsing experience, signing up, logging in and, if I can't remember my password, have a smooth exchange to facilitate a password reset (via email)
* As a frequent user, I want to access the application via any device I have access to (e.g. ipad, mobile phone. laptop (desktop)) 
* As a user, I want to build a profile and research products to potentially purchase
* As a frequent user, I want to add my own posts and see the other posts from other members of the community, I would also enjoy a way of interacting with other members.

#### Admin

* As an admin, I would like to be able to edit and delete posts I see as unfit.
* As an admin, I would like to access the sites back office to remove any users who are not abiding by the sites rules



# Design 

#### Font/Typography

In keeping in line with a machine themed site, I chose the Google Font [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono?preview.text=roboto&preview.text_type=custom&query=robot&sidebar.open=true&selection.family=Roboto+Mono#license) which I personally really like and felt it lent itself a lot to the design style I was aiming for.


#### Colour Scheme

I wanted to keep the colour schematic really simple, but a bit different compared to my other milestone projects, which all used the colour green heavily. This site body I went for a very light grey tone `#EEEEEE` ([referred to as *Whisper*](https://www.htmlcsscolor.com/hex/EEEEEE)) to match the sort of mechanical colouring associated with machines and electronics. My navbar colour `#212529` is described as very dark blue [according to this site](https://www.colorhexa.com/212529). However I also dotted the site with red, blue, yellow, a little bit of purple and green (among others) - which can be considered a subtle ode to rainbow coloured electrical wiring. 

For example, I chose  [metallic green](https://encycolorpedia.com/296e01) `#296e01` as the footer colour as once again I liked the juxtaposition between the green, which is associated with nature, and metallic which gives off more of a colder, static machine tone.


Over all, I like the contrast the dark grey colour navbar, the light grey body with the other elements as I feel it illuminates the elements on the page and in my opinion lends itself to aesthetically pleasing site, and therefore, easier on the eye for the user.

#### Imagery 

I actually chose some nature focused images for the site like the main carousel or the empty cart/checkout basket. As mention, I simply liked the colour as well as the contrast it provides. I personally don't think it's confusing for a user to a site to see a range of images that don't directly correlate to the site topic, but that could perhaps be a criticism. However, personally I like it and feel it adds some nice chroma to the site. 

### **Wireframes**

Wireframes are really important for a developer to have an idea of where they want the site to go and flesh out how it will look and function. I used the app [Balsamiq](https://balsamiq.com/) to build my wireframes. I find it to be a really intuitive and user friendly application, which allows a user to build, simply and efficiently, a wireframe. This allowed me to clearly visualize the structure and design of my project.

Here is my original desktop landing page wireframe. I wanted a really simple, efficient and clean design whereby the user can navigate easily: 


#### Wireframe 1 - Desktop View

![home page](/media/ReadMe_Docs/wireframe_desktop_landing1.png "Index.html Desktop Wireframe" )

*Figure 1. Landing Page (Desktop) Index.html*

#### Wireframe 2 - Phone View


![home page](/media/ReadMe_Docs/wireframe_phone1.png "Index.html Phone Wireframe" ) <h2>

*Figure 2. Landing Page (Phone) (Index.html)*


# Database Schema 

## Databases

**SQLite3** 

SQLite is a lightweight relational database management system. It's Django's default database management system, so once you create a Django project, 
a SQLite database is automatically created, which allows the user to store data locally and run tests.
SQLite is embedded on the end-program (Django) as opposed to being a ['client-server' database engine](https://en.wikipedia.org/wiki/SQLite).

**PostgreSQL**

[PostgreSQL](https://www.postgresql.org/) is a relational database that is synced to the live Heroku application and facilitates the data exchange in the site.

Below is a table of my `User_Posts` Model, which I am demonstrating as an example of the database schematic. Please note the variations in Field Type and Validation as the model can be associated with other models, making the database fluid and interchangeable, which is a key tenet when working with data that is constantly changing and adapting. 

For example, the `on_delete=models.CASCADE` method ensures that if a `User` is deleted, the `author` and therefore the post will also be deleted. As mentioned this is extremely important to the structure of the database. As we can see from the `author` item in the table, it utilises the [SQL]() `ForeignKey`, which is, as stated on the [W3 Schools site](https://www.w3schools.com/sql/sql_foreignkey.asp#:~:text=A%20FOREIGN%20KEY%20is%20a,the%20referenced%20or%20parent%20table.),:
> (A `FOREIGN KEY` is) a field (or collection of fields) in one table that refers to the PRIMARY KEY in another table e.g. (`author` :arrow_right: `User`)

#### Database Diagram Structure (*PostgreSQL*)

I had a little bit of trouble extracting the PostgreSQL database from Heroku so I quickly crafted this structure below to mimic my current database. I designed it using the [DB Diagram tool](https://dbdiagram.io/home). I feel the database structure could be improved by adding more `ForeignKey` elements to intertwine more models but as I shall explain in the *bugs* and *features left to implement* section, I had some constraints to execute this. But certainly something I learned a lot about and can improve upon in the future.

![DB Diagram](/media/ReadMe_Docs/db_diagram2.png "DB Diagram" )

**PostgresSQL Database Table (User Posts)**

| **Name** | **Database Primary Key** | **Field Type(s)** | **Validation** |
--- | --- | --- | --- 
 title | title | CharField |  max_length=100, help_text='Enter post title'
 content | content | TextField | null
 created_date | created_date | DateTimeField | auto_now_add=True
 published_date | published_date | DateTimeField | blank=True, null=True, default=timezone.now
 views  | views | IntegerField | default=0
 tag | tag  | CharField | max_length=40, blank=True, null=True
 image  | image | ImageField | upload_to="img", blank=True, null=True
 author  | author | ForeignKey | User, default=None, on_delete=models.CASCADE
 likes  | likes | ManyToManyField | User, related_name="user_likes"

 *Below is how the UserPost Models are constructed in `Python`:*

```python

class User_Posts(models.Model):

    title = models.CharField(max_length=100, help_text='Enter post title')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True) 
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="user_likes")


    def total_likes(self):
        return self.likes.count()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})`
```


# **Features**

## **Existing features**

The following features are divided up by page, detailing the logic behind each:

**1. Landing Page** 
The main site page contains a Carousel with images and some informative text as well as links and buttons helping the user to navigate the site. Navbar adapts depending on whether the user is logged in or not, offering different options. The is a search bar (in both cases) to allow a logged in user and someone who isn't logged in to browse the products (but not purchase unless they are an authenticated user)

**2. Login Page**  
If a user already has registered, they can log into the site to access their profile and the sites benefits. They can enter their `username` and `password` and pressing the `login` button. If a user can't recall their `password`, they can follow the `reset password` logic. 

**3. Register Page**
A visitor on the site would like to sign up for an account, they simple need to provide their `email`, a `username` and a `password` (that needs to be confirmed)

**4. Reset Password Pages**
Functionality to allow a user (who already has registered successfully) to recover a lost password by entering in their email (must be valid to receive an email from the site), follow the link generated on the email to a page to enter in a new password (plus confirmation), so that the user can recover their profile with their bio and comments on it.

**5. User Profile Page:**
    Once a user registers, their profile data is saved and stored on the database (to allow for anytime access). Users can navigate to the profile section of the site and adapt the default information, adding for example, their own profile bio and image. 

- **5.1. Edit/Update Profile**:

    As mentioned above, the user can edit their profile. They can upload a personalised profile image, add a bio and also their location. I didn't allow them to change their email/username to maintain the integrity of each profile. Passwords can only be changed using the process as above, which is only advised in the event of a lost password


- **5.2. Delete Profile** 
 A user can erase their profile and all their data. It cannot be recovered thereafter. A user is met with a modal prompt upon clicking the `Delete` button as an added step as so to ensure that one doesn't permanently delete their user profile from the database by a mistake.  

**6. Products Page**
A user can browse the products page, which shows the electronics products available to purchase on the site. An image and details such as price are given. The use can add an item (currently the maximum to each addition is 999). A user can stay on the products page but browse the products section using the paginate method.

**7. Cart Page**
A user’s cart/basket is a boolean, it can either be empty or have contents. If the the cart is empty, a Jumbotron will display a message to the user and prompts some direction back to the products section to potentially select an item to buy. If the cart has items present, the user can amend the quantity (for example, remove a product completely). The current total is displayed in euros :euro: . Once the user is happy with the contents in their cart, they can click the checkout buy to proceed to the checkout/payment section

**CART APP:**
- For the cart section of the site, we utilise a contexts.py file. This file contains a function which dictates the logic of the cart section and this also ensures that the cart contents are available when rendering every page on the site. 

    The cart items also don't go into the database. Cart items are stored in session when the use is logged in. A standard feature on e-commerce sites but an interesting adaptation nevertheless. It may also lend itself to reminding users that they have something in their basket that perhaps they want to purchase. However, when the user logs out, all the carts contents are lost. 

**8. Checkout (Payment) Page**
The user is once again presented with the total amount (:euro:) currently in their basket (how muc they will spend). The main form on this payment is the payment form where the user will have to fill out correct details (or be prompted with an error message). Once all the details of the payment form have been correctly entered, the user can hit the green `submit payment` button that will give the user a confirmation message that their payment was success (the full payment details are logged on the Stripe end). The user is then redirected back products page. Also below the payment form, is a recap of what's currently in the users basket (for referral)

*Please note, the Stripe payment system is fully active but a test platform (so no products will be sent). Please use the credit card number `4242_4242_4242_4242` for testing purposes*

**9. User Posts Pages (Individual Posts and All Posts)**
A user can browse the User Posts section to see all of what other users have posted about. All users can enter into the User Post details page and `like` a particular post. A user can add, edit and delete their own posts. The admin can add, edit and delete all posts.

**10. Add User Post Page**
- **10.1. Edit/Update Posts** 
If the user was the author of a post (or is the admin), they can simply edit their post and it will be updated.

- **10.2. Delete Posts** 
If the user was the author of a post, (or is the admin), they can also delete their post. They are once again prompt by a modal cause anything that's deleted is removed from the database and therefore can't be recovered.

- **10.3. Like Posts** 
A simple `like` counter that all users can avail from to demonstrate which posts they enjoyed.


**USER POSTS APP - (Individual Posts):**

- I followed this tutorial to add the [like button functionality](https://www.youtube.com/watch?v=PXqRPqDjDgc&ab_channel=Codemy.com) and I feel it works quite smoothly and adds to the feel of a community. I could have also added the *dislike* button but I wanted to avoid any negative connotations on the site. 

    If the user has written the post themselves, they have the option to edit/update and/delete. If the user is on a post from another user, they do not have the option to edit or delete a post. The Admin reserves the right to edit and/delete any post they so choose. This is an important tenet of CRUD (Create, Read, Update and Delete) from the ux perspective as well as a site management point of view. The admin can remove or edit a post they feel is unsuitable or against the site regulations, for example.

**11. Other Site Functions** 

- Navbar
    -  The Navbar is a constant on the site. It allows the user to navigate and on smaller (mobile) displays it adapts to the viewport via Hamburger icon. All the main functionality on the site can be enacted via the navbar and so it provides a stable and reliable aspect to the site layout and logic. On smaller viewports, the dropdown is also condensed to allow for a better UX.

- Button Logic:

    •	Register - Upon clicking this button, the user redirected to the registration page where, upon entering their (correct) details, can avail of an user account and have access to the site.

    •	Login – Upon clicking this button, the user is redirected the login form where they can enter their details (if they have already signed up) to access their account.

    •	Logout - Upon clicking this button, which is placed as a dropdown button on the Navbar and so accessible at all times, the user log out of their account. When a user is logged out, the session is over and they are redirected to the landing page (as a non-logged in user).

    •	Reset-Password – A non-logged in user (if they have an account but cannot access it for whatever reason), can choose to reset their password. This button is found on both the login and register pages. Upon clicking it, a user is brought to main reset password page where they can follow the simple procedure, which will eventually send an email (to the address they registered with) with a link to reassign a new password to their old account. It’s a standard procedure for a lot of sites. Perhaps not the most secure security measures but it adds a layer of protection against hacks.

    •	View Products/Posts/Profile - Upon clicking these buttons, the user can easily navigate to other pages on the site and thus the user experience is improved. An obvious and simple example is a user on the home page, wanting to see their profile can either navigate to the profile via the Navbar option, the aforementioned button or even the url, if they so choose.

    •	Add Products- A vital yet straightforward concept. On the products page, if a user wants to add a product to their cart (to purchase), they would select the quantity and upon clicking the *Add* button (**which via the Django templating language is connected to a function/view, which in turn will update the contents in their cart**). This allows a user to fill their cart up with as little or as many products as they please for later purchase. Upon clicking the button, the user is automatically (if they have selected a `quantity > 0`) redirected to the checkout section
     
    •	Go to Checkout – When a user has arrived in their cart (if there are contents greater than 0), upon evaluating what’s in their cart and, if the user is happy to proceed to the payment section, they can simply click the *Go to Checkout* button to be directed to the Checkout/Payment section. 

    •	Amend Quantity – On the cart page, after a user has selected a product or products to add to their cart. The user can decided to amend the quantity, either increase, decrease and/or remove (by entering 0) products and their cart contents number will be updated automatically (if the cart is empty or full can be seen at all times on the Navbar). Upon clicking the amend button, the user stays on the cart page and can see the adjusted amount of their cart.

    •	`Back-to-Top` – This button is visible on the pages with more content or the pages that are designed to increase/adjust in height (for example if a user selects one of each of all the products of the site to purchase, their cart and checkout page will expand in height). The home page, cart and checkout pages avail of the `back-to-top` button. Once a user scrolls down a page, they can simply click on this button (which is visible as it is fixed to the bottom right hand side on the page and has a `z-index: 1`) and the user to brought back up to the top of the body of the html page. It’s a particularly valuable function on mobile phone devices, as the viewport as content is condensed and it tends to favour a scrolling style, so this option, in my opinion is a nice option for users to avail of to make their experiences a little smoother.

    •	Submit Payment – Once the user has selected products to purchase and confirmed the quantity, the must enter their details correctly on the payment form (which applies Stripe logic) and they can then click the `Submit Payment` button which, as it’s linked to the Stripe backend logic, which confirm their payment, sending the user to the Products page with the message - “You have successfully paid! Your products are on their way!” . If the form details are incorrect, the user will be prompted with a red/warning message specifying which form detail needs to be rectified. 

    •	User Posts Section - If a user arrives on the user posts page, they can navigate (via pagination) the user posts section to see all of the shared comments. A user can click either `View Post in Detail` or `Back to Home`. Viewing a post in detail products the user with a focused view on a particular post (giving them further options) and back to home button simply returns the user to the main home page. 

    •	User Posts in Detail - As mentioned above, a user can select to `View Post in Detail`. This button brings them to a focused User's post (recognized via the id in the URL). The user has a number of options on this page. If they are they author of the post (or the admin), they have the right to edit (brings them to the `edit user post form`) or delete the post entirely. The user can also choose to like a user. A user can like all posts (regardless if they are author) however, it functions on a - one user, one like per post basis. A user can't just add endless likes on a particular user post. If the user is not the author of the post, (nor the admin), they won’t be able to delete or edit a post. They can only view and like (x1) the post. All users can see the total accumulated likes on any posts and also avail of the `Back to Posts` to return to the general User posts section.


    •   Add a New Post - found via a button at the bottom of the user posts page  (and via the Navbar), this button allows users to be redirected to a form where they can upload their own personalised post. 

- Form Logic

    - Login/Register: Enables users to sign in or sign up using their own personalised details. By Registering, users are created in the database

    - Reset Passwords: Allows users, who have an account, to retrieve their account, if it is lost for any reason. This triggers an external email, containing information and a link for the user to reset their password.

    - Edit User Profile: Allows a user to personalise their own user profile, for example, by uploading an image/avatar (as opposed to using the default)

    - Orders/Checkout: A robust form, connected with Stripe, to allow a user (who has added products to their cart) to enter their payment details to confirm a purchase of the products. Will be prompted if information is incorrect and will be redirected with a successful message and order details if the payment was successful.

    - Add/Edit User Post: Allows users to add their own detailed posts, including content and images

- Search bar
    - Found on the right-hand side of the navbar, it allows users and non-logged in site visitors alike to quickly and easily search for products. They are prompted if a product doesn't exist and redirected to the main landing page. If they find a product, for example, a 'Multimeter', they are brought to a page to view the product.

- Page Scroll Button

    - Found on numbers pages (home, checkout, cart, user posts), using this function (when it appears) allows a user, who have scrolled further down the page, to simply click on the fixed button on the bottom right-hand side and instantly and smoothly return to the top of the page.

- Modals

    - Modals are mainly used as a prompt for the user, for example, when undertaking an important action, whereby a second confirmation is necessary (like deleting a profile). On the site, if a user wants to delete a post or delete their user profile, they will be prompt with a modal popup, which will focus solely on the action and allow the user a sort of 2 step process when commiting important actions.

- Pagination:

   - allows for smooth and logical browsing for the user, if there are many products or posts, they user can navigate via the pagination buttons at the bottom of the page. As for example, user comments naturally increase over time, a user can navigate to older comments easily, smoothly and with logic, by maintain uniformity to the page structure.


- Bootstrap Cards and Jumbotron:

    - I used bootstrap cards heavily to display users profiles, posts and products. I found them to give a smooth, simply look to the site and allow for good use of the grid system. I also used a Jumbotron to display to the user when their basket was empty, with a nice image added again for colour and imagery.



        


## **Features Left to Implement** 

Due to a mix up, I had less time than anticipated to finish up my project and so I feel there are plenty more features and logic, both backend and frontend, that could be incorporated. I focused more on the backend logic and making sure that the users could perform a variety of actions but here are some features that can be (and hopefully will be) added in the future:

- I could have also added a user comment section/forum for each post, which would cultivate an interactive community (for example, on [StackOverflow](https://stackoverflow.com/), if a user is struggling on a topic or just wants to know more about something, they could pose a question to the forum, hoping for a robust response). 

- I briefly played with the idea to add an *Order history* to the user profile section, so users could refer to what they have already purchased. The implementation wasn't too difficult however during my efforts I made an error with the `Null=True` and `Blank=True` [model arguments (fields)](https://stackoverflow.com/questions/8609192/differentiate-null-true-blank-true-in-django), and a `makemigrations` command which caused me quite a bit of trouble (which I will explain in the bugs section). So due to this error and simply a lack of time, I chose against this option for the time being. But I feel it would be a very simple, logical piece of code to implement and importantly, give the user a paper trail on the site. 

I feel that there is huge room for improvement in terms of how the models, the site and the database interact. As mentioned above (and below) with the issue I had with `migrations`, were in fact simple fixes. I wanted to add, for example, a default user post photo (as there is a `default img` on the `Profile` model) but again, pushing the project over the line meant not having time to fine tune all of the MVT aspects but really good learning experience in crafting a large project with a professional tilt. With the orders history in tandem, I also felt I could have an automatic email system (like for the reset password form), that confirms a user’s order with a receipt via email.

I would like to improve simple user functionality and add more flow to the site, for example, on the products page, if a user selects a product and clicks the `Add` button (to their cart), they are automatically redirected to the Cart section. This was a choice on my part but it could easily be adapted to simply stay on the Products page (with the user cart amount incrementing to the chosen quantity) to facilitate a multiple product choice buying experience.

Other features to add/improve upon include:

    1. A more robust sign in/sign up system - obtaining more user details
    2. A larger user profile, with previous orders (mentioned), more comments and direct interaction with other users (via a forum for example)
    3. Replace the `img thumbnail` class on user post cards as the height is set to `auto;`, meaning that the image heights are stable and can be bigger or smaller than the default.
    4. The ability to contact the admin, report issues directly etc. 
    5. User updates, if, for example, another user responds to their post. 
    6. The ability to add other users to your group discussion and/or have a private/chat thread with another user.
    7. Change the Stripe  year selection placeholder on the credit detail details from 2019 to current year.

There are endless options with Django, and considering I'm currently using the version `Django==1.11.29`, I hope to have time in the future to update the site and add many more robust functions, models, views, libraries etc. The options are boundless!


## **Site Layout**

### Django Framework Logic 

I mainly followed the MVT (Model-View-Template) concept of Django as I found it to be the most clean and logical approach for my needs. [Check out more info on MVT here](https://medium.com/@jaychaturvedi18/a-brief-introduction-to-django-mvt-framework-8ef46cc321ab)

**Models** 
 - The model creation is extremely important that's collected from the user and that will be going into the database. This will be all the information we require from a user, for example, the `Checkout` app model. Each time we create a new model, we must migrate the data to ensure that [Model Definitions and the Database Schema are in Sync](https://realpython.com/django-migrations-a-primer/#:~:text=Without%20migrations%2C%20you%20will%20have,in%20sync%20with%20your%20models.). Again this something, with time and more experience in the future, I would like to improve upon.


# **Technologies Used** 

### **Languages**

-   [Python](https://www.python.org/) - the main backend programming language used. Python is a [interpreted, object-oriented, high-level programming language](https://www.python.org/doc/essays/blurb/). Python is used in tandem with Django to construct the views and main site logic.
-   [HTML5](https://en.wikipedia.org/wiki/HTML5) I used HTML to define structure and layout of thesite;
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - is used as the stylesheet language for styling and rendering.
-   [Javascript](https://www.javascript.com/) - is the renowned programming scripting language and the main libraries are JS.


### **Frameworks**

-   [Django](https://www.djangoproject.com/) - is a high-level Python Web framework that used the MVT system 

### **Libraries and Other Programs Used**
1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used heavily as the main library to style the site. I availed particular from the grid system and the buttons, among many other functions.
1. [Google Fonts:](https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap)
    - I felt Google Fonts was extremely important to improve the look and UX of the site. I used the `Roboto Mono` font which I found to be perfectly fitted to the technical *machine* styling I was looking for. The first time I switched the font (from the standard default bootstrap font), I was really taken aback by how much the site look and professional feel was improved by the font.
1. [Font Awesome:](https://fontawesome.com/)
    - I used Font Awesome heavily on all pages on my website. I like the sleek icon style and feels it gives a boost to the UX
1. [jQuery:](https://jquery.com/)
    - jQuery CDN library was used to assign functionality to Bootstrap elements 
1. [Git:](https://git-scm.com/)
    - Using Git on the Gitpod IDE for version control, to commit and push code to Github
1. [GitHub:](https://github.com/)
    - Pushing with my git commands, my entire project code is store on Github
1. [Balsamiq](https://balsamiq.com/) 
    - was used to create my wireframes
1.  [django-storages](https://django-storages.readthedocs.io/en/latest/) & [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - were libraries used to connect Django to AWS S3 Buckets to host media. Both found on `requirments.txt`
1. [django-forms-bootstrap ](https://pypi.org/project/django-forms-bootstrap/)
    - a library used to adapt the standard django forms into bootstrap styling. Listed on `requirments.txt`.

- **Databases, Hosting, API’s, Mockups:**

    - [PostgreSQL](https://www.postgresql.org/) - a relational db management system, hosted on Heroku;
    - [SQLite](https://en.wikipedia.org/wiki/SQLite) - a lightweight db management system that runs locally on Django (used mainly for testing)
    - [Heroku](https://dashboard.heroku.com/apps) – The site is hosted on Heroku platform
    - [Stripe API](https://stripe.com/en-ie)  – Used to make secure payments
    - [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) – Used to generate site mockup for different view ports (Mac)
    - [DBDiagram]( https://dbdiagram.io/home) – Diagram tool used to craft the PostgreSQL database as a diagram using the native language


# **Testing**

I tested the site in a number of ways, always attempting to incorporate a defensvie programming mindset. A good quote that summarise's this point, comes from this [blog](https://medium.com/swlh/2-defensive-coding-techniques-you-should-use-today-4225cacc1c29), which states:

> Defensive coding allows our software to behave in a correct manner, despite incorrect input

I tested the platform on a number of devices (ipad, iphone, android, laptop) as well as all the viewports on Chrome Devtools. And I always aim to *disrupt* the flow of the creature of project. I referred to the ever trusty [Real Python](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#types-of-tests) to guide me through some of the tests at the later stage of the project, when I had no access to the course content.



### **Validation**

-   [PEP8](http://pep8online.com/)
     - PEP8 was the tool I tested my Python code on. I recieved plenty warnings such as:
        > `W292	10	44	no newline at end of file`
        > `line too long (80 > 79 characters)` 
        > `trailing whitespace . . `

        I did my best to remove as much of the warnings as possible but my main focus, with a lack of time, was clean code and functionality.

-   [JSHint](https://jshint.com/) 
    - I did not add the Stripe.js file, just the JS static file hosted on AWS. Once I ran my code into JSHint and this was the feedback:
    
        > Metrics- There are 10 functions in this file. Function with the largest signature take 0 arguments, while the median is 0. Largest function has 6 statements in it, while the median is 1. The most complex function has a cyclomatic complexity value of 2 while the median is 1. One undefined variable


-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input+with_options) 
    - The feedback from this code validator wasn't brilliant as I had to ignore the errors from the Jinja templating system. For example, userpostsform.html, returned `1 warning, 3 errors` all due to Jinja. I passed my htmls into the validtor in any case. The main test was seeing the pages rendering via my own tests.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    * I added my css code into the valditor and it stated: 
            > W3C CSS Validator results for TextArea (CSS level 3 + SVG)
    Congratulations! No Error Found.

    * I only added my static css code, which is hosted on AWS.

- [Google Mobile-Friendly Test site](https://search.google.com/test/mobile-friendly)
    - Positive feedback from this site, which stated:
    > Page is mobile friendly. This page is easy to use on a mobile device


## Analysing User Experiences 

Analysing User Experiences versus (expected) User Goals [from UX Section](UX)


### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Goals Recap:

1.	As a First Time Visitor, visitor, I want to navigate around the site easily..
2.	As a First Time Visitor, I want to learn quickly what the site is about and what benefits a user can avail of
3.	As a First Time Visitor, if I am interested to do so, I would like to sign up for an account in a smooth and simple fashion
4.	As a first time visitor, I want to access the site via any device

#### First Time Visitor Goals Results:	

* *Result*: Upon landing on site, users are met with a simple title and carousel gives the user something visual to focus on. Users can navigate via the Navbar and I find that the main landing page, gives plenty of clear indicators, buttons and text for the first timer to interact with, as to where to go to sign up and what to expect from the site. 
* I used minimalist style of text and formatting so allow the user to quickly understand the site’s reason for existence and the benefits for signing up. Clear directions prompt the user to the register section and as mentions in the device testing section, I made sure that the site was robustly tested and user friendly on all devices.



#### Returning/Frequent User Goals Recap

 
1. As a frequent user, I am interested in electronics and want to learn a bit more
2. As a frequent user, I want a smooth browsing experience, signing up, logging in and, if I can't remember my password, have a smooth exchange to facilitate a password reset (via email)
3. As a frequent user, I want to access the application via any device I have access to (e.g. ipad, mobile phone. laptop (desktop))
4. As a user, I want to build a profile and research products to potentially purchase
5. As a frequent user, I want to add my own posts and see the other posts from other members of the community; I would also enjoy a way of interacting with other members.

#### Returning/Frequent User Goals Results:	

* *Result*: If a user has availed of a user account, the different sections on the site allow the user to pique their electronics interested. This area could have been improved for example with blog articles that give the user more reliable content. I tested rigorously the browsing experience particularly for logging in, registering and resetting the password. 
* I feel this section has achieved what I was aiming for. Again, same as the previous section, I tested on many different devices and feel that the site is capable of handling the variations in devices. I am particularly fond of the user profile section as I feel it’s personalised and also users to craft something of their own, for example, with a profile image/avatar. This section can be improved however with more content and a more robust model. Finally, adding posts and viewing others posts I achieved as well as the addition of a like button. There was potentially for much more user interaction but that will be a future project.

#### Admin/SuperUser Goals Recap:
1. As an admin, I would like to be able to edit and delete posts I see as unfit.
2. As an admin, I would like to access the sites back office to remove any users who are not abiding by the sites rules

* *Result*:  I spent most of my time testing as an admin so I felt that I got a really good feel for it. It’s a super option that Django offers and a really clever format. I felt I achieved what are, admittedly, modest goals for the admin to achieve. As mentioned in my future features section, there’s a lot of room for scope here. However, my admin/superuser can indeed edit and delete posts as they see fit from all users. Obviously through the backend the Admin can delete any user but I didn’t manage to incorporate this on the front end side of things as my deadline was approaching a little too fast. However, I felt the admin profile offers a superior UX experience and is fit for purpose.

### Further Testing

Overall, I felt I could have done a lot more on the testing side of my project. It's something I plan on improving on and something that's in fact, quite interesting. I enjoyed the logic and concept behind unit-testing and at every step of my project I focused heavily on functional testing. It was a mentally and physically straining experience but a great learning curve nevertheless.

### Automated - Travis CI - Continuous Integration

The build is currently passing, has some small hiccups early on when I was automating testing with coverage but I resolved the problems as they arose. Again, due to time contraints I would have loved to automate my tesing much more but I was busy focusing on other parts of the project. Coverage caused me some issues as well when I was connected to PostgreSQL (as it only works with SQLite), so I tested on another local environment. 

### Testing Functionality

With each new addition to my project, I tested all new functionality and tried to ensure that everything was working, as I intended, including:

    - Password Reset Email confirmation - private emailing plus following the links
    - Stripe Payment confirmation (and incorrect details prompt)
    - Checking via Devtools (live on Heroku) if AWS media hosting links were functioning
    - User Login, Logout and Registered (check information also on backend)
    - Non-logged in user attempting to access content (refused)
    - All buttons and links tested
    - User editing pages and deleting Pages
    - User editing and deleting profile
    - Users availing of the like button
    - Image uploads tested - large, incorrect format etc. 
    - Forms robustly tested with correct and incorrect detail 

### Device Testing

I used Chrome tools extensively when fixing issues and testing on all the viewports.. I also tested the pages and functionality on other browsers like Firefox, Safari and Microsoft Edge. The Toggle Device Toolbar helps to evaluate all the different viewports, which really enhances the development process. I also enlisted the help of friends to simulate a new User experience testing on their phones mainly but also tablets (iPad) and laptops (desktops). Any issues that were noticed I attempted to resolved with regards to all the viewports.


## **Bugs** 

I had a number of interesting and challenges bugs throughout the project. [Stack Overflow](https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete) as always proved very helpful with this error. I actually entered the `collectstatic` command in the terminal incorrectly (something like `collecstatic`) however the console returned an intriguing error: 
`product = models.ForeignKey(Product, null=False) TypeError: __init__() missing 1 required positional argument: 'on_delete'`. The fix proved to be simple however I thought it curious as the incorrect command gave feedback on a missing `arg` when using `ForeignKey` in the models.

*Django - Exception in djang-main-thread*:
Some reccuring bugs that had really simple fixes initally had me scratching my head, such as this Django error `AttributeError at /accounts/edit-profile/ 'str' object has no attribute 'fields'`. This was resolved from [this](https://stackoverflow.com/questions/25615753/attributeerror-str-object-has-no-attribute-fields-using-django-non-rel-on-g) discussion on Stack Overflow and it was simply a typo in the end, whereby I called the incorrect form name on the template (correction was `{{ profile_form | as_bootstrap }}` for example), however honing in on why and what's going wrong is critial. 

This error, in fact, lead to another, more [troubling error](https://stackoverflow.com/questions/56274132/exception-in-thread-django-main-thread)`Exception in thread django-main-thread:`. I have a little bit of experience with firing threads in my work so I was aware a misfiring concurret thread can cause. And this error did give me a bit of trouble. I began by spot fixing the error feedback, which stated `ImportError: No module named 'django.core.urlresolvers'` so I removed the `reverse lazy` library and simplified it with `from django.urls import reverse` [following this discussion of Stack Overflow](https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers). However this lead to a game of cat and mouse, as with each change I got a new error relating to some import incompatiblity. However, through a bit more research I realised (and this is why Github version control is so important) that my Django version had been updated when I installed some new libraries, namely the `django-storages==1.10.1`, was the version that cause the error, thus resulting in a string of incompatiblities. So I simplied reinstalled an older version of `Django==1.11.29`and `django-storages==1.9.1`. Following that, I ran my runserver command in the terminal and it worked. 

*Amazon S3*:
- Plenty of minor bugs and issues stemmed from using the [Amazon S3 Buckets](https://aws.amazon.com/s3/). One interesting bug in particular was that, for testing, I was using an older bucket I created for the Django ecommerce app. As that app was uploaded to Heroku, despite the fact I had deleted the old contents, my new project was simultanelously runnings with 2 `style.css` files. It took me a while to figure out and rectify (by deleting the older, unused Heroku app). Frustrating but interesting nevertheless as Heroku had manage to maintain the deleted css file and simultanelously run it on my new app.

As usual there were plenty of minor bugs invloing the html/css grid system, I had a particular issue with the search function, if a product was found and it returned a product card, the width, in tandem with the padding was too large, causing the card to flow over the grid, not a good site for the user. 

*Django migrations*:
In an attempt to add an order hitory to my project (a bit late in the day, if I'm honest) and as mentioned above, as I push `makemigrations` command via the Gitpod terminal, I then attempted to `migrate` and began to get a whole host of errors. I needed to refer to the [Django docs](https://docs.djangoproject.com/en/3.1/topics/migrations/) and after some (stress induced) research I ended up having to reverse the model migrations I made - the command being `python3 manage.py migrate checkout zero` - which had reversed all non commited model changes I made (so, luckily I didn't commit). I realised also, after some tests, I arrived at this [step](https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a):

    ```
    You are trying to add a non-nullable field 'user' to slide without a default; we can't do that (the database needs something to populate existing rows).
    ```
I actually believe the fix for this is really straightforward, however, after my inital scare and due to a simple lack of time, I left this function out. It would be a logic step towards a more robust database schema so it's one for the future.

*Javascript*
Whilst testing I also noticed that Javascript was throwing up lots of errors on the Chrome Dev tools and I couldn't figure it out directly. My js code and the id's etc. showed no errors on JSHint. However, after a bit of research I realised, somehow, I managed to use a *slim* version of the Jquery library. [This post](https://stackoverflow.com/questions/43067555/why-is-this-jquery-error-happening-animate-is-not-a-function) was very helpful in explaining that, basically: 
> a slim version of jQuery does not contain all the original jQuery functions
And so for example, the `animate` function on my `back-to-top` scroll button wasn't working very smoothly. This issue was resolved very nicely in the end with a really simply fix.

### Known Bugs

- Stripe payment form has 2019 and as default
- Navbar dropdown is a little aggressive in hamburger format
- `img thumbnail` on the user posts has a height that is set to 'auto' so it change depending on the image upload. 
- like button doesn't tell user if that have already liked a post
- 

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

### Github - Version Control


### Github and Gitpod

My site code is deployed on [Github](https://github.com/NeiloErnesto89/FullStack_Django_MS4_MaChine). This project was built and tested on the [Gitpod IDE.](https://www.gitpod.io/). Which has a base similar to VSCode (which I use for work) so I found it to be suitable and nice to use. I had some issues with the ports not closing and so I had to use some linux commands such as `ps aux` to find the PID port number and then `kill <PID>`. Other than some minor issues it served its purpose well. My code was directly deployed from the master branch. I consistently added, committed and pushed my updates via the Gitpod command terminal as often as possible. I then deployed the site automatically upon receiving the new commits to the master branch/source. The following commands were used in Gitpod to deploy my code to Github:

**In the Gitpod Command Terminal**

- The `git init` to initialise my local repo. command was used  
- Then then `git remote add origin https://github.com/NeiloErnesto89/FullStack_Django_MS4_MaChine.git` command was used to add the new remote repo (taken from Github pages site).  
- Afterward I used the `git push origin master` pushing my code to the master branch.
- And so after my repo was initlaised, I used the commands: `git add . ` (to add all) or `git add ReadMe` (to add a specific file) 
- And then  the command`git commit -m "initial commit"`(and with every commitfollowed by any comments) to `add` and `commit` files to Github. 
- Then, I would use the `git push origin master` command to push my updated code to the remote Github repository.

### Clone Code for Local Use

Steps to clone a repo on Github:

1. Go to my [repo on Github](https://github.com/NeiloErnesto89/FullStack_Django_MS4_MaChine)
2. Click the `Clone or download` button
3. In HTTPS, copy the clone url
4. Return to Gitpod (or chosen IDE)
5. `pwd` to print your working directry and then (if needed) `cd` change directory to the path you want your clone to exist on
6. Command - `git clone <url from above>` and enter to commence local repo
7. You then need to add your own details, perferable via an `env.py` file stored on a `.gitignore` file
8. You need to add a `requirements.txt`(if necessary, you need the file from clone with all the dependencies) - command on Gitpod `pip3 install -r requirements.txt` and to update `pip local > freeze requirments.txt`.
9. To initialise Django, run the `python3 manage.py runserver` in your terminal. In Gitpod for example, you can navigate to the IP host address or open a preview in the terminal or browser.
10. Finally, you need to create a superuser and (in order to build models) run migrations, via the following commands:

        `python3 manage.py makemigrations` (always first)
        then:
        `python3 manage.py migrate`
        *and to create a superuser (followed by details)*
        `python3 manage.py createsuperuser`
`


#### Forking a Github Repo

Forking is simply making a code of the repo, adapting it but not affecting the original:

1. Sign into Gihub and go to your chosen repo (for example, [mine](https://github.com/NeiloErnesto89/FullStack_Django_MS4_MaChine) )
2. Find the `fork` button (like the `clone` button)
3. Now you have your own copy of a repo on your Github account to do with it what you please.

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

	And same details were configured in the Heroku **Config Vars** section as below (with the values removed for obvious reasons :lock: )

	![alt text](/media/ReadMe_Docs/heroku_config_vars.png "Config Vars")
		
7. Deployment:
	
	-  Finally, back on the Heroku page, I go to the *deploy* section, adding *GitHub* to deploy my heroku app to the Github repo
	- The final step is to enable *automatic deploys*, so that each time I push to GitHub, the updated version of the app is deployed to Heroku (except, as mentioned above, not the `collectstatic` command)

Sidenote: After configuring all of this, after any big changes or advancements on my code etc. I would push my code to the Heroku app (via GitPod) to check if it was functioning.  

# Credits

## Credits

At the beginning of my project I had access to the course material, which guided me crafting the bones of the project. However, due to an unforeseen mix up, I was left to complete the course with 3 weeks less than I had originally planned for and no course material to refer to. This is not to bemoan this outcome, I am in fact, quite happy with the end result. I felt I managed to produce a piece of work that I can call my own, without leaning too much on the course material or any one source (bar [Stack Overflow](https://stackoverflow.com/) of course) :grinning: . And I researched and devised a decent part of the later logic myself (paginate, user likes, user image upload (profile/posts) etc.), so I feel that it's definetley a positive iteration in terms of my progress. The course material was, of course, a big help but it's more the satisfaction I derived from working on, and producing, something that feels very much like my own doing. 

All that being said, the internet is an endless wealth of material, content, inspiration and snippets for a would-be developer to avail from, so here are all the points of reference I had for building my project: 


**User Password-Reset Email**

This section is important as it gves the touch of a real and interactive site. I ran into some issues along the way including some of the naming conventions and having to generate an two-factor authentication step for my email account to faciliate the actual email being sent. The bones of the *reset password* logic was crafted using the CI course material, however the final hurdle was aided by the ever reliable:

- [Corey Schafer's Youtube video(s)](https://www.youtube.com/watch?v=-tyBEsHSv7w&t=750s&ab_channel=CoreySchafer) 
- As well as a few ventures onto Stack Overflow including this [query](https://stackoverflow.com/questions/28421887/django-email-with-smtp-gmail-smtpauthenticationerror-534-application-specific-pa) and [this question](https://stackoverflow.com/questions/28074127/django-send-email-shows-success-but-no-email-received)
- And also the [Django documention](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/views/)

**Search Function**

I found a really simple [fix](https://stackoverflow.com/questions/1387727/checking-for-empty-queryset-in-django) for returning a `message` redirecting back to the home page if, when using the search bar, the Django queryset filter was empty, which was this simple built in method `if products.exists():` 


**Featurette Landing Page Style**

I found the base for my [Featurette](https://stackoverflow.com/questions/33626772/line-up-bootstrap-featurette-text-with-the-image-above-it) here

**Pagination** 

Settled on a view based function as opposed to class based pagination function.
[This blog](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) guided me very smoothly through this process. 

**Comment**

This Bootstrap style [comment example](https://bootsnipp.com/snippets/exz9y) was used as the base for my user posts/comments but I did adapt it quite a bit in the end.


**Modals**

For my modals, I took some snippets from [this site](https://mdbootstrap.com/docs/jquery/modals/customization/) as I thought they looked really sleek and worked very well.


On this StackOverflow post I found the [logic](https://stackoverflow.com/questions/11916297/django-detect-admin-login-in-view-or-template/11916391) for the `is_superuser` templating 

**Humanize (Numbers):**

[Humanize](https://simpleisbetterthancomplex.com/tips/2016/05/09/django-tip-2-humanize.html) is a really simple way to give data a bit of a 'human touch', so instead of `18 Sep 2020 20:54:31` into `2 days ago` using the template filter `| naturaltime` .

**Profile Page:**

The inspiration for the profile card style profile came from this [site](https://www.bootdey.com/snippets/view/about-me-profile#html). Furthermore, for the styling of the product, cart and checkout cards, I followed a similar tutorial from this [site](https://mdbootstrap.com/docs/jquery/components/cards/#waves-effect). 

I also closely followed Corey Schafer's excellent [videos](https://www.youtube.com/watch?v=FdVuKt_iuSI&t=2s&ab_channel=CoreySchafer) and his code snippets came in [handy](https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/08-Profile-And-Images/django_project/users/views.py)   

I also used this to extend the User model by adding a [Profile model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)

[CSS return to top button](https://codepen.io/michalwyrwa/pen/GBaPPj)


I refered quite often to the **[Django docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)** (here is the section on forms)

Another StackOverflow discussion resulting in a [Django messages template example](https://stackoverflow.com/questions/16711917/django-message-template-tag-checking)

**AWS S3 Bucket Logic:**

- [This article](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) helped me navigate the storage process on Amazon S3 for the Django Static and Media Files.

- Also, [this](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html) blog came in extremely handy more than once (in this case for Amazon S3)


**Javascript/Bootstrap Carousel:** 
- I got my inspiration and code snippet for my landing page carousel [here](https://mdbootstrap.com/docs/jquery/javascript/carousel/). I loved the imagery and even though they are landscape as opposed to machine/electronics, I enjoy the juxtaposition of nature and electronics.

**Landing Page SVG Icons** 

I used some svg icons from the [bootsrap icons library here](https://icons.getbootstrap.com/icons/lightning/). I used them only on the main landing page. I found the SVG format to be a bit clunky but it did give me some nice inline styling, sizing and positioning options I didn't have with Fontawesome.

**Delete Functions/Views:**

- some of the logic that I used for the delete user and delete (user) posts methods was adapted from this [StackOverflow post](https://stackoverflow.com/questions/33715879/how-to-delete-user-in-django)

**Acknowledgements**

A fellow Code Institute Student whose [project](https://github.com/JBroks/unicornattractor_issue_tracker) was a huge source of inspiration as their project was of such high quality. I referred to it at times when I was entertaining some ideas and looking for some solid logic. The size, scale and professionalism of this project is really impressive. No direct code snippets were used (mainly due to different techniques implemented), so it was more of a guide, but excellent and inspiring work nevertheless!

## Media



## Acknowledgements

* My Mentor Maranatha Ilesanmi, for his helpful and constructive insights 

* Thanks to Code Institute Support team, my fellow students/alumni (via Slack), to my family and my partner for everything 	:smiley:

> NOTE: This project was created for educational purposes. **Machine** is a fictious site. 