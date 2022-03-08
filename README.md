# Currency exchange project

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

Currency exchange project.

----
Project structure:

currency_exchange_project/

    mysite/
        manage.py
        mysite/
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py
        quote/
            migrations/
                __init__.py
            apps.py
            models.py
            serializers.py
            urls.py
            views.py


The `settings.py` file controls how Django inter-acts with your system and manages your project.
The `urls.py` file tells Django which pages to build in response to browser requests.
The `wsgi.py` file helps Django serve the files it creates.

###Creating and activating the Virtual Environment
A virtual environment is a place on your system where you can install packages and isolate them from
all other Python packages. To set up virtual environment, go to your project folder and type command
`py -m venv your_env`. After creating your virtual environment activate it with following command
`your_env\Scripts\activate.bat`

###Creating database
Django stores most of the information for a project in a database. To create the database enter 
the following command `python manage.py migrate`. Any time we modify a database, we say we’re
migrating the database.

###Running the project
Enter the following command to run your project `py manage.py runserver`.

###Activating models
To use our models, `quote.apps.QuoteConfig` should be included in the INSTALLED_APPS list in
`mysite/settings.py` file.

Next, we need to tell Django to modify the database so it can store information related to the model
Quote. From the terminal, run the follow-ing command: `python manage.py makemigrations quote`.
This migration will create a table for the model Quote in the database. Now we’ll apply this migration
and have Django modify the database for us `python manage.py migrate`.

###Web pages with Django
Making web pages with Django consists of three stages: defining URLs, writing views, and writing templates.
First describe the URL pattern in `quote/urls.py`.The URLS also should be registered to `mysite/urls.py`.
Each URL then maps to a particular view. The view function retrieves and processes the data needed for that
page. The view function often renders the page using a template, which contains the overall structure
of the page.






