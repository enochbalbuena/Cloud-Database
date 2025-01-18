import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

# Firebase Configuration
firebase_config = {
    "apiKey": "AIzaSyDiAkZAb8W0hLLZQbeveq9mL1gQ_Q_I5DU",
    "authDomain": "to-do-list-4134f.firebaseapp.com",
    "projectId": "to-do-list-4134f",
    "storageBucket": "to-do-list-4134f.appspot.com",
    "messagingSenderId": "510141356196",
    "appId": "1:510141356196:web:1a80a9641d3041fa58ae31",
    "databaseURL": ""
}

# Initialize user authentication
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Initialize Firebase Admin SDK
cred = credentials.Certificate("to-do-list-4134f-firebase-adminsdk-fbsvc-1b6e42dc01.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Firestore collection name
COLLECTION_NAME = "tasks"

# Authentication Functions
def sign_up(email, password):
    """Sign up a new user."""
    try:
        auth.create_user_with_email_and_password(email, password)
        print("User signed up successfully!")
    except Exception as e:
        print("Error signing up:", e)

def log_in(email, password):
    """Log in an existing user."""
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("User logged in successfully!")
        return user["idToken"]
    except Exception as e:
        print("Error logging in:", e)
        return None

# To-Do List Functions
def add_task(user_id, task_name, task_description):
    """Add a new task to Firestore."""
    doc_ref = db.collection(COLLECTION_NAME).document()
    doc_ref.set({
        "user_id": user_id,
        "name": task_name,
        "description": task_description,
        "completed": False
    })
    print(f"Task '{task_name}' added successfully!")

def get_tasks(user_id):
    """Retrieve all tasks for the logged-in user from Firestore."""
    tasks = db.collection(COLLECTION_NAME).where("user_id", "==", user_id).stream()
    print("\nTasks:")
    for task in tasks:
        data = task.to_dict()
        print(f"- {task.id}: {data['name']} (Completed: {data['completed']})")

def update_task(task_id, new_name=None, new_description=None, completed=None):
    """Update a task's details in Firestore."""
    task_ref = db.collection(COLLECTION_NAME).document(task_id)
    updates = {}
    if new_name:
        updates["name"] = new_name
    if new_description:
        updates["description"] = new_description
    if completed is not None:
        updates["completed"] = completed

    task_ref.update(updates)
    print(f"Task '{task_id}' updated successfully!")

def delete_task(task_id):
    """Delete a task from Firestore."""
    db.collection(COLLECTION_NAME).document(task_id).delete()
    print(f"Task '{task_id}' deleted successfully!")

def main():
    print("Welcome to the To-Do List App")
    print("1. Sign Up")
    print("2. Log In")
    choice = input("Enter your choice: ")

    if choice == "1":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        sign_up(email, password)
        return

    elif choice == "2":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        token = log_in(email, password)
        if not token:
            return

        user_id = auth.get_account_info(token)["users"][0]["localId"]

        while True:
            print("\nTo-Do List Options:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                add_task(user_id, name, description)
            elif choice == "2":
                get_tasks(user_id)
            elif choice == "3":
                task_id = input("Enter task ID to update: ")
                name = input("Enter new name (leave blank to skip): ") or None
                description = input("Enter new description (leave blank to skip): ") or None
                completed = input("Mark as completed? (yes/no/leave blank): ").lower()
                completed = True if completed == "yes" else False if completed == "no" else None
                update_task(task_id, name, description, completed)
            elif choice == "4":
                task_id = input("Enter task ID to delete: ")
                delete_task(task_id)
            elif choice == "5":
                print("Exiting To-Do List app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
