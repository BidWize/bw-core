# Get started

## Running the application

### Tips before starting
1. Ensure WSL is working with VSCode
2. Ensure Docker is installed 
3. Clone Repo
4. Rename "sample.env" to ".env"

### Contributing
1. Create your own branch
2. Create commits with prefix (fix:, feat:, lint:, etc) and then information 
3. Create a pull request to push your work to main
4. ???
5. Profit

### In a virtual environment

1. Install python (im using 3.10.12)
2. Create a virtual environment

    ```sh
    python3 -m venv .venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On Linux/Mac:
        ```sh
        source .venv/bin/activate
        ```
4. Install the requirements:
    ```sh
    pip install -r requirements.txt
    ```
5. Run the app locally with Uvicorn:
    ```sh
    uvicorn app.main:app --reload
    ```

### Running in a Docker container

1. Change directories into the `docker` folder:
    ```sh
    cd docker
    ```
2. Run the Docker container:
    ```sh
    docker compose up --build
    ```

## Running Tests

1. Ensure the virtual environment is activated.
2. Install the dev requirements:
    ```sh
    pip install -r requirements-dev.txt
    ```
3. Run the tests with pytest:
    ```sh
    pytest --cov=./ --cov-report=html --cov-fail-under=50
    ```
4. View the coverage report by opening `htmlcov/index.html` in a browser.

## Accessing the Application

-   The application will be available at `http://localhost:8000`.

## API Documentation

-   FastAPI automatically generates interactive API documentation:
    -   Swagger UI: `http://localhost:8000/docs`
    -   ReDoc: `http://localhost:8000/redoc`

# Layout best practices

https://fastapi.tiangolo.com/tutorial/bigger-applications/
