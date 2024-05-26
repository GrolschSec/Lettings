Installation
============

To install the application locally, follow these steps:

1. Clone the repository:

    ```
    $ git clone https://github.com/GrolschSec/oc_lettings_site.git
    ```

2. Change to the project directory:

    ```
    $ cd your-repo
    ```

3. Create a virtual environment:

    ```
    $ python3 -m venv venv
    ```

4. Activate the virtual environment:

    ```
    $ source venv/bin/activate
    ```

6. Install the dependencies:

    ```
    $ pip install -r requirements.txt
    ```

Run the application
-------------------

1. Set the environment variables:

    ```
    $ export DJANGO_SECRET="your-django-secret-key"
    $ export SENTRY_DSN="your-sentry-dsn"
    ```

    (Refer to the github repo to view how to get the DJANGO_SECRET and SENTRY_DSN keys)

2. Set up the database:

    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

3. Start the development server:

    ```
    $ python manage.py runserver
    ```

Now you should be able to access the application locally at `http://localhost:8000`.