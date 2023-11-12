# AirBnB CLONE PROJECT
![AirBnB](./airbnb.png)

## Description
This is the first part of Airbnb clone project. This focuses on the backend implementation. Here, we created a command-line interface for creating and objects Objects such as users, states, cities, places, amenities, and reviews.from the console

## Command Interpreter
The command interpreter allows us to:
- Create a new object (e.g., a new User or a new Place)
- Retrieve an object from a file
- Perform operations on objects e.g count
- Update attributes of an object
- Destroy an object

## How to Start

### Prerequisite
- Have `python3` installed
- Have cloned this repository in your local machine
--------------------------------------------------

To start the command interpreter, cd into the project root directory and run the following command:
```bash
$ ./console.py
```

## How to use it

```bash
$ ./console.py
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) destroy BaseModel 1234-1234-1234
(hbnb) all
(hbnb) update BaseModel 1234-1234-1234 name "New Name"
(hbnb) quit
```

## Examples

```bash
prisca@Priscas-MacBook-Air AirBnB_clone % ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all

        Print the string representation of all instances based on class name.
        Usage: all [optional: <class name>]

(hbnb) create User
f8e91841-4c1b-426f-9b7a-0499b3f8af68

(hbnb) show User f8e91841-4c1b-426f-9b7a-0499b3f8af68
[User] (f8e91841-4c1b-426f-9b7a-0499b3f8af68) {'id': 'f8e91841-4c1b-426f-9b7a-0499b3f8af68', 'updated_at': datetime.datetime(2023, 11, 12, 18, 32, 22, 985272), 'created_at': datetime.datetime(2023, 11, 12, 18, 32, 22, 985316)}

(hbnb) update User f8e91841-4c1b-426f-9b7a-0499b3f8af68 first_name "Paul"

(hbnb) show User f8e91841-4c1b-426f-9b7a-0499b3f8af68
[User] (f8e91841-4c1b-426f-9b7a-0499b3f8af68) {'id': 'f8e91841-4c1b-426f-9b7a-0499b3f8af68', 'updated_at': datetime.datetime(2023, 11, 12, 18, 32, 22, 985272), 'created_at': datetime.datetime(2023, 11, 12, 18, 32, 22, 985316), 'first_name': 'Paul'}

(hbnb) create BaseModel
b0a8d455-9426-41d0-b1ee-c8c8af3ca86f

(hbnb) all
["[User] (f8e91841-4c1b-426f-9b7a-0499b3f8af68) {'id': 'f8e91841-4c1b-426f-9b7a-0499b3f8af68', 'updated_at': datetime.datetime(2023, 11, 12, 18, 32, 22, 985272), 'created_at': datetime.datetime(2023, 11, 12, 18, 32, 22, 985316), 'first_name': 'Paul'}", "[BaseModel] (b0a8d455-9426-41d0-b1ee-c8c8af3ca86f) {'id': 'b0a8d455-9426-41d0-b1ee-c8c8af3ca86f', 'updated_at': datetime.datetime(2023, 11, 12, 18, 33, 19, 318278), 'created_at': datetime.datetime(2023, 11, 12, 18, 33, 19, 318286)}"]

(hbnb) User.count()
1

(hbnb) destroy User f8e91841-4c1b-426f-9b7a-0499b3f8af68
(hbnb) User.count()
0
(hbnb) quit
prisca@Priscas-MacBook-Air AirBnB_clone %

```
