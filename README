# Job Site

A Django-based web application leveraging Django Rest Framework, Celery for asynchronous task management, Swagger and Redoc for API documentation, Pytest for testing, and Docker Compose for container orchestration. This project uses PostgreSQL as its database and Redis for caching and Celery backend.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Docker
- Docker Compose
- Make

### Installing

To get a local copy up and running follow these simple steps:

1. **Clone the repository**

   ```bash
   git clone git@github.com:YUND4/focun-back.git
   cd focun-back
   ```

2. **Environment Setup**

   Before starting the project, ensure your local environment variables are set up. Copy the `.env.example` file to a new file named `.env` and adjust the variables to match your local setup.

3. **Running the Application**

   To start all services, use the provided Makefile commands:

   ```bash
   make up
   ```

   This command will stop any running containers, start all services in the background, and then show logs for the Django project.

4. **Accessing the Application**

   After starting the services, the web application should be accessible at:

   - Django application: `http://localhost:<port>/`
   - Swagger UI: `http://localhost:<port>/swagger/`
   - Redoc: `http://localhost:<port>/redoc/`

### Useful Commands

- **Starting the project**

  ```bash
  make up
  ```

- **Stopping the project**

  ```bash
  make stop
  ```

- **View running containers**

  ```bash
  make ps
  ```

- **Rebuilding Docker images**

  ```bash
  make rebuild
  ```

- **Resetting the project**

  This will update Docker images and reset local databases.

  ```bash
  make reset
  ```

- **Accessing bash inside the Django container**

  ```bash
  make bash
  ```

- **Running tests**

  ```bash
  make test
  ```

- **Viewing logs**

  For Django project logs:

  ```bash
  make log
  ```

  For all project logs:

  ```bash
  make logs
  ```

### Running Tests

To run tests, use the following command:

```bash
make test
```

This will start the application in a testing environment and execute the test suite.

## Deployment

Add additional notes about how to deploy this on a live system.

## Contributing

Please read [CONTRIBUTING.md](<link-to-contributing-guide>) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```

This README template is structured to provide a comprehensive guide for setting up, developing, and deploying a Django project with Docker Compose, integrating Django Rest Framework, Celery, Swagger, Redoc, Pytest, PostgreSQL, and Redis. You can adjust the details such as the repository URL, project directory, and specific ports as per your project's requirements.