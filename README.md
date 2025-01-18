# Overview

This python program is a to-do list app that interacts with a cloud database stored in the google firebase platform. The app contains a user authentication feature that allows users to sign up and/or log in, and once logged in, they can create, add, update, and delete tasks. These tasks are linked to each user, so that they can interact privately with them.

Once you run the program, the console output will display a menu with options. Select the option and press enter. You will see a message to confirm your action once you're finished.

The purpose of this program is to demonstrate an easy way to interact with a cloud database in real time.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

Google Firestore database

The project is using a database with a single table containing the necessary tasks data: name, description, and user_id. The primary key is the task id, which is used for all CRUD interactions.

# Development Environment

Google Firestore Database
Email/Password Built-in Authentication
VS Code 2
Python
firebase_admin
pyrebase

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Firebase documentation](https://firebase.google.com/docs)
- [python Documentation](https://docs.python.org/3/)

# Future Work

- Web UI
- Relational tables
- Updates notifications
