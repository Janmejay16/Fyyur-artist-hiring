import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
database_name = 'REPLACE_WITH_YOUR_DATABASE_NAME'

SQLALCHEMY_DATABASE_URI = 'postgresql://{your_username}:{your_password}@localhost:5432/{database_name}'.format(your_username=YOUR_USERNAME,your_password=YOUR_PASSWORD,database_name=database_name)

# remove console warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

