## Summary

Orange County Lettings' Website

## Local development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the documentation on local development, it is assumed that the python command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

### macOS / Linux

#### Cloner le repository
```bash
    cd /path/to/put/project/in
    git clone https://github.com/GrolschSec/oc_lettings_site.git
```
#### Create the virtual environment

```bash
    cd oc_lettings_site/
    python3 -m venv venv
    source venv/bin/activate
```

### Install the dependencies

```bash
    pip install -r requirements.txt
```

### Setting up Sentry

**What is Sentry?**
Sentry is an error tracking and monitoring tool that helps developers identify and fix issues in real-time. It provides detailed reports about errors and performance issues, allowing you to understand and resolve them quickly. Sentry supports a wide range of programming languages and frameworks, making it a versatile choice for application monitoring.

**How to Get the Sentry DSN**

1. **Sign Up and Log In:**
   - Go to [Sentry's website](https://sentry.io/) and sign up for an account if you don't have one. If you already have an account, log in.

2. **Create a Project:**
   - Once logged in, you need to create a new project. Navigate to the Projects section and select "Create Project".
   - Choose the platform that matches your application (e.g., Python for a Django application).

3. **Get the DSN (Data Source Name):**
   - After creating the project, Sentry will provide you with a DSN. This DSN is a URL that allows your application to communicate with Sentry.
   - Copy the DSN, as you will need it to configure Sentry in your application.

4. **Configure Sentry in Your Application:**
    Before running the application, you can set the Sentry DSN in the same terminal session. This allows the application to read the DSN frometting  an environment variable and use it in the Django settings.
    ```bash
        export SENTRY_DSN="your dsn here"
    ```

By following these steps, you will have set up Sentry for your application, allowing you to track and monitor errors effectively.

### Setting up Django Secret Key

**What is the Django Secret Key ?**
The Django secret key is a critical part of your application's security. It is used for various cryptographic signing operations. For security reasons, it's best to set this key via an environment variable.

**How to set the Django Secret Key**

1. **Create a new random secret key:**
    - You can create a secret key using the django shell:
    ```bash
        python manage.py shell -c "from secrets import token_hex; print(token_hex(24));"
    ```

2. **Set the Django Secret Key Environment Variable:**
   - You can set the `DJANGO_SECRET` environment variable in your terminal session before running the application:

    ```bash
        export DJANGO_SECRET="your_secret_key_here"
    ```

Then your Django app's secret key is well configured, however, if you don't set one, a secret is generated automatically. It is always better to have control over your secret.

#### Running the site

- Run the server:
    ```bash
        python manage.py runserver
    ```
- Open your web browser and navigate to http://127.0.0.1:8000 to view the site.

#### Linting
Proper linting helps maintain code quality and consistency across the project.
To check the linting in the project run (from the venv):
```bash
    flake8
```

#### Unit testing
The project includes some tests using Django's testing framework (unittest). To run the tests, use:
```bash
    python manage.py test
```

#### Database

This project uses SQLite as its database. SQLite is a lightweight, disk-based database that doesn’t require a separate server process, making it ideal for local development and small-scale applications.

To interact with the SQLite database, you can use the `sqlite3` command-line tool. For more information on how to use SQLite, including commands for querying and managing the database, refer to the [SQLite Documentation](https://www.sqlite.org/docs.html).

### Administration Panel

To access the administration panel, follow these steps:

1. **Change the Admin Password:**
   - Use the `manage.py changepassword` command to change the admin password:
     ```bash
    python manage.py changepassword admin
     ```

2. **Access the Admin Panel:**
   - Go to [http://localhost:8000/admin](http://localhost:8000/admin) in your web browser.
   - Log in with the username `admin` and the password you set.

This will allow you to access the Django administration panel to manage your site's data.

### Windows

Using PowerShell, follow the steps above with the following differences:

- To activate the virtual environment, use:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```

- Replace `which <my-command>` with:
  ```bash
  (Get-Command <my-command>).Path
  ```

## Deployment

For continuous deployment of the application, we use a GitHub Actions workflow that performs several steps:

1. **Compilation, Testing, and Test Coverage:**
   - The workflow verifies that the code compiles correctly, runs all tests, and checks the test coverage.

2. **Containerization and Upload to DockerHub:**
   - The application is containerized and the Docker image is uploaded to DockerHub (only on the `main` branch).

3. **Deployment to Azure:**
   - The application is deployed to an Azure server, but only if the containerization step is successful.

### GitHub Configuration

To ensure the workflow functions correctly, several variables and secrets are configured in the GitHub repository:

- **Secrets (Repository settings > Secrets and variables > Actions > Secrets):**
  - `AZURE_WEBAPP_PUBLISH_PROFILE`: The content of the file downloaded from Azure that allows us to authenticate.
  - `DOCKERHUB_USERNAME`: DockerHub username to push the Docker image.
  - `DOCKERHUB_PASSWORD`: Password used to connect to DockerHub to push the Docker image.

- **Variables (Repository settings > Secrets and variables > Actions > Variables):**
  - `DOCKERHUB_REPO`: The name of the DockerHub repository to push the Docker image.

### Azure Configuration

After creating a new web app on Azure and configuring it for container deployment from DockerHub using GitHub Actions, we set the necessary environment variables for the application. These are optional but required for full functionality:

- `SENTRY_DSN` and `DJANGO_SECRET`: Refer to the local development section to see how to obtain these variables.

To set these environment variables in Azure:

1. Go to the Azure portal and navigate to your App Service.
2. Go to **Settings** > **Configuration** > **Application settings**.
3. Add the required environment variables (`SENTRY_DSN` and `DJANGO_SECRET`).

Once these configurations are done, the next push to the `main` branch will automatically trigger the deployment process. If you need to, you can also manually trigger the CI/CD pipeline from the GitHub interface by navigating to the "Actions" tab, selecting the desired workflow, and clicking on the "Run workflow" button.

By following these steps, you will ensure that your application is properly deployed and running smoothly on Azure.