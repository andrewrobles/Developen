# Developen

Follow these instructions to setup Developen on your local machine. These instructions are a work in progress so please add to it if you feel it is necessary.

# Setup
These set up instructions are meant for Mac OS.

## Virtual Environment

After cloning the repository to your local machine, you will need to setup a virtual environment. Navigate to your root project directory and do the following.

1. Run `python3 -m virtualenv venv` to create a new virtual environment.
2. Run `source venv/bin/activate` to activate it.
3. Run `pip install -r requirements.txt` in order to install the required dependencies

## Database 

1. Download PostgreSQL (pgAdmin 4 is recommended).
2. Create a new PostgreSQL user with username `postgres` and password `postgres`.
3. Create a new database and give the new user access.
4. From project root directory run python manage.py migrate to create the database tables.

## Admin Account

* Run `python manage.py createsuperuser` and enter a username and password when prompted.