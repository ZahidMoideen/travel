# Django Destination Management Application

This Django application provides APIs for managing destinations and user authentication.

## Features

- CRUD operations for destinations
- User registration and authentication
- Token-based authentication for API access

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework 3.x

## Installation

1. Clone the repository:



2. Install the required dependencies:


3. Run migrations to create the necessary database tables:


4. Start the development server:


## API Endpoints

- `/destinations/`: List and create destinations
- `/destinations/<int:pk>/`: Retrieve, update, and delete a specific destination
- `/api/token/`: Obtain authentication token (POST request with username and password)
- `/login/`: User login (POST request with username and password)
- `/register/`: User registration (POST request with user details)
- `/logout/`: User logout (POST request with authentication token)

## Usage

1. Register a new user using the `/register/` endpoint.
2. Log in with the registered user credentials using the `/login/` endpoint to obtain an authentication token.
3. Use the obtained token to access protected endpoints like `/destinations/`.
4. Log out using the `/logout/` endpoint to invalidate the token.

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.




## API Documentation

### Base URL

http://localhost:8000/

### Authentication

1. **Obtain Authentication Token**:
   - **Endpoint:** `/api/token/`
   - **Method:** `POST`
   - **Request Body:** `{"username": "example_user", "password": "example_password"}`
   - **Response:** `{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "user_id": 5}`

2. **User Login**:
   - **Endpoint:** `/login/`
   - **Method:** `POST`
   - **Request Body:** `{"username": "example_user", "password": "example_password"}`
   - **Response:** `{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "user_id": 5}`

3. **User Registration**:
   - **Endpoint:** `/register/`
   - **Method:** `POST`
   - **Request Body:** `{"username": "new_user", "password": "new_password", "email": "new_user@example.com"}`
   - **Response:** `{"id": 6, "username": "new_user", "email": "new_user@example.com"}`

4. **User Logout**:
   - **Endpoint:** `/logout/`
   - **Method:** `POST`
   - **Headers:** `Authorization: Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
   - **Response:** `{"detail": "Logout successful"}`

### Destinations

1. **List Destinations**:
   - **Endpoint:** `/destinations/`
   - **Method:** `GET`
   - **Headers:** `Authorization: Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
   - **Response:** `[{"id": 1, "name": "Example Destination 1", "description": "Description of Example Destination 1", "location": "Example Location 1"}, {"id": 2, "name": "Example Destination 2", "description": "Description of Example Destination 2", "location": "Example Location 2"}]`

2. **Create Destination**:
   - **Endpoint:** `/destinations/`
   - **Method:** `POST`
   - **Headers:** `Authorization: Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
   - **Request Body:** `{"name": "New Destination", "description": "Description of New Destination", "location": "New Location"}`
   - **Response:** `{"id": 3, "name": "New Destination", "description": "Description of New Destination", "location": "New Location"}`

3. **Retrieve Destination**:
   - **Endpoint:** `/destinations/<int:pk>/`
   - **Method:** `GET`
   - **Headers:** `Authorization: Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
   - **Response:** `{"id": 1, "name": "Example Destination 1", "description": "Description of Example Destination 1", "location": "Example Location 1"}`
