# Installation:

Clone this git repository:

`git clone https://github.com/njmarti9/pizza.git`

Create a python virtual enviroment for python3 and activate it.

`pip install --user pipenv`

Go to the project folder:

`cd pizza`

Install the requirements:

`pip install -r requirements.txt`

Run the migrations:

`python manage.py migrate`

Start the server:

`python manage.py runserver`

# Testing functionality of site

When the server is deployed append '/admin' to the end of the url provided.

To access the site, use the different accounts for the various functions.

Chef Account:
Username: chef
Password: Whatever123

Owner Account:
Username: Owner
Password: Whatever123

The Chef can construct various specialty pizzas with the toppings the owner has made available.

If you would like to test all the functionality without logging in and out of various accounts you can use the account below.

Admin Account:
Username: admin
Password: 1234

# Improvements that I would make

I haven't been able to dedicate nearly as much time as I would have liked to working on this project due to personal reasons, but if I were to spend more time on this project it would be to address the following areas:

1. I would spend more time trying to figure out a way to make the specialty pizzas be unique based off of name and off of toppings. Right now it only has the capability of denying duplicates based off of the names. This fix would require reworking the models that are currently in use. Currently manytomany fields is being used for the toppings attached to the Pizza models, and I have not found a way to have that list of toppings be unique between pizzas since the unique modifier does not function with manytomany models.

2. I would make a dedicated template for the webpage instead of relying on the admin page to display all of the functionality itself. While the admin page allows for all the functionality to be demonstrated, a custom template would have provided a better user experience that could've been tailored to a more fitting aesthetic for the concept.

3. I would have deployed the application using AWS so there could be additional security and would have satisfied the third requirement for the project. I attempted to integrate Elastic Beanstalk into the project to connect everything to AWS, however, the versions of python and the other dependencies kept causing errors. If I could've done the project over again I would have created the AWS project first and then started developing the django part of the application.