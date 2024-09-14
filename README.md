# AirBnB Clone

## Overview

Welcome to the AirBnB Clone project! This is a command-line interface (CLI) application for managing AirBnB-like objects. This project lays the foundation for a complete web application by implementing a basic model management system and a command interpreter.

## Project Structure

- **`models/`**: Contains the model classes and base model.
  - `base_model.py`: Defines the `BaseModel` class with common attributes and methods.
  - `user.py`: Defines the `User` class, inheriting from `BaseModel`.
  - `state.py`: Defines the `State` class, inheriting from `BaseModel`.
  - `city.py`: Defines the `City` class, inheriting from `BaseModel`.
  - `place.py`: Defines the `Place` class, inheriting from `BaseModel`.
- **`console.py`**: Implements the command interpreter using the `cmd` module.
- **`models/file_storage.py`**: Handles saving and loading objects from a JSON file.
- **`tests/`**: Contains unit tests for your models and storage.
  - `test_base_model.py`: Tests for the `BaseModel` class.
  - `test_user.py`: Tests for the `User` class.
  - `test_state.py`: Tests for the `State` class.
  - `test_city.py`: Tests for the `City` class.
  - `test_place.py`: Tests for the `Place` class.

# Usage

## Running the Command Interpreter

To start the command interpreter in interactive mode:

```
$ ./console.py
```

You will see the (hbnb) prompt, where you can enter commands.

## Commands

`create <class_name>`: Creates a new instance of the class.
`show <class_name> <id>`: Displays the instance with the specified ID.
`destroy <class_name> <id>`: Deletes the instance with the specified ID.
`all <class_name>`: Lists all instances of the specified class.
`update <class_name> <id> <attribute_name> <attribute_value>`: Updates an attribute of the instance with the specified ID.
`quit`: Exits the command interpreter.
`EOF`: Exits the command interpreter when using input redirection.

## Examples

### Create a New User

```
(hbnb) create User
1234-5678
```

### Show User

```
(hbnb) show User 1234-5678
[User] (1234-5678) {'id': '1234-5678', 'created_at': '2024-09-13T00:00:00', 'updated_at': '2024-09-13T00:00:00', 'email': '', 'password': ''}
```

### Update User

```
(hbnb) update User 1234-5678 email "user@example.com"
```

### List all Users

```
(hbnb) all User
```

### Destroy user

```
(hbnb) destroy User 1234-5678
```

# Testing

To run the unut tests:

```
python3 -m unittest discover tests
```
