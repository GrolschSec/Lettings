Deployment
==========

For continuous deployment of the application, we use a GitHub Actions workflow that performs several steps:

Compilation, Testing, and Test Coverage
---------------------------------------

The workflow verifies that the code compiles correctly, runs all tests, and checks the test coverage.

Containerization and Upload to DockerHub
----------------------------------------

The application is containerized and the Docker image is uploaded to DockerHub (only on the main branch).

Deployment to Azure
-------------------

The application is deployed to an Azure server, but only if the containerization step is successful.

GitHub Configuration
--------------------

To ensure the workflow functions correctly, several variables and secrets are configured in the GitHub repository:

Secrets (Repository settings > Secrets and variables > Actions > Secrets)
-------------------------------------------------------------------------

- **AZURE_WEBAPP_PUBLISH_PROFILE**: The content of the file downloaded from Azure that allows us to authenticate.
- **DOCKERHUB_USERNAME**: DockerHub username to push the Docker image.
- **DOCKERHUB_PASSWORD**: Password used to connect to DockerHub to push the Docker image.

Variables (Repository settings > Secrets and variables > Actions > Variables)
-----------------------------------------------------------------------------

- **DOCKERHUB_REPO**: The name of the DockerHub repository to push the Docker image.

Azure Configuration
-------------------

After creating a new web app on Azure and configuring it for container deployment from DockerHub using GitHub Actions, we set the necessary environment variables for the application. These are optional but required for full functionality:

- **SENTRY_DSN** and **DJANGO_SECRET**: Refer to the local development section to see how to obtain these variables.

To set these environment variables in Azure:

1. Go to the Azure portal and navigate to your App Service.
2. Go to **Settings > Configuration > Application settings**.
3. Add the required environment variables (**SENTRY_DSN** and **DJANGO_SECRET**).

Once these configurations are done, the next push to the main branch will automatically trigger the deployment process. If you need to, you can also manually trigger the CI/CD pipeline from the GitHub interface by navigating to the "Actions" tab, selecting the desired workflow, and clicking on the "Run workflow" button.
