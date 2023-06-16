# Django-Rest-Frame-work-API

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:
2. Navigate to the project directory:
3. Create a virtual environment: "python -m venv venv"
4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

## Usage

1. Start the development server:

   ```shell
   python manage.py runserver
   ```

2. Access the API endpoints by visiting `http://localhost:8000/admin` in your browser and login as "brij" and passwork is "admin"

## API Endpoints

| Method | Endpoint      | Description            |
| ------ | ------------- | ---------------------- |
| GET    | /api/endpoint | Get all items          |
| POST   | /api/endpoint | Create a new item      |
| GET    | /api/endpoint/{id} | Get a specific item |
| PUT    | /api/endpoint/{id} | Update a specific item |
| DELETE | /api/endpoint/{id} | Delete a specific item |


