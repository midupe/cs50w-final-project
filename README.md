# CS50W Final Project

## Distinctiveness and Complexity

This is my cs50w final project. I developed a URL shortening webapp using Python, JavaScript, HTML, CSS and SQL with the Django framework.
Short url (the name of my webapp) enables users to shorten URLs and receive a shortened URL of their original URL.


To implement the Short url I had in mind that the users may want to use the app without registration but still keep a history of the urls they shortened, so I developed an algorithm that creates a cookie on the client side that is also stored on the backend/Database if the user is not logged in. On the other hand, if the user wants, he can register and will have access to extra features like knowing how many people used the urls they shortened.


I wanted my website to be as dynamic as possible, so I used JavaScript to copy to the clipboard the shortened url automatically and to update the urls list when a new url is shortened. When the user is logged in, he can check the number of views of his urls, this information is updated every 3 seconds, giving the user updates without having to refresh the page.


My webapp is as easy to use as possible with a minimalistic but great design and is mobile-responsive.


The main complexity of my capstone project was to create an algorithm that shortened the url. I used `random` with the ascii lowercase letters to create a unique string that allows the program to identify the original url.

## Files and Directories
- `config`: main application directory (has django settings, ...)
- `cs50wfinal`: Shorten url application
    - `static`: static files
        - `css`: css files - used for styling
        - `js`: js files - scripts used to improve UX
        - `img`: images used on the design
    - `templates`: website html templates
        - `layout.html`: layout used on the index html
        - `index.html`: homepage html file
        - `signin_layout.html`: layout used on the login and register html
        - `login.html`: login html page
        - `register.html`: register html page
    - `models.py`: used to create python classes and migrations that allow to create database tables
    - `urls.py`: used to define the application urls and associate them with a view
    - `views.py`: used to create the logical part of the website
- `db.sqlite3`: database used in the application
- `.gitignre`: ignore files for git
- `manage.py`: python file that manages django application
- `readme.md`: this file
- `requirements.txt`: dependicies to run the app
- `run.bat`: script to run the application on Windows
- `short-url.gif`: Short url gif preview


## How to run?

`python -m venv venv`

`venv\Scripts\activate`

`pip install -r requirements.txt`

`python manage.py runserver`


## Short url
![Preview](short-url.gif)