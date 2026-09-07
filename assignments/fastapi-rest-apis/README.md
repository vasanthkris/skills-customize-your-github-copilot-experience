# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice HTTP methods, path operations, request validation, response data, and in-memory CRUD operations.

## 📝 Tasks

### 🛠️ Define the API Model

#### Description

Create a FastAPI application for managing a collection of books. Define a Pydantic model that describes the data a client must provide when creating a book.

#### Requirements

Completed program should:

- Create a `FastAPI` application instance.
- Define a `Book` model with fields for `id`, `title`, `author`, and `year`.
- Store several sample books in an in-memory list.
- Run the application with Uvicorn and display the interactive API documentation at `/docs`.

### 🛠️ Implement CRUD Endpoints

#### Description

Add endpoints that allow clients to list, retrieve, create, update, and delete books from the in-memory collection.

#### Requirements

Completed program should:

- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return one book by its ID.
- Implement `POST /books` to create and return a new book.
- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.

### 🛠️ Validate Requests and Handle Errors

#### Description

Make the API predictable for clients by validating request data and returning appropriate HTTP errors when a book cannot be found.

#### Requirements

Completed program should:

- Reject invalid request data through Pydantic validation.
- Return a `404` response when a requested book ID does not exist.
- Return an appropriate success status and response body for each endpoint.
- Test the endpoints using the interactive `/docs` page or an API client such as `curl`.
