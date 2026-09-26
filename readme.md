PERSONAL TASK MANAGEMENT SYSTEM

A web-based Personal Task Management System developed using Python, Flask, HTML, CSS, and JavaScript. The system allows users to create, manage, organize, search, filter, update, and complete personal tasks through a simple and user-friendly dashboard.


PROJECT OVERVIEW

The Personal Task Management System is designed to help users organize their daily tasks and keep track of their work efficiently.

The application provides a centralized dashboard where users can add tasks with details such as title, description, category, priority, status, and due date.

Users can search, filter, edit, complete, and delete tasks according to their requirements.

This project was developed as a 5th Semester BCA academic project to demonstrate practical implementation of web development concepts, Flask-based backend development, frontend design, database operations, and CRUD functionality.


FEATURES

• Add new tasks
• Edit existing tasks
• Delete tasks
• Mark tasks as completed
• Set task priority
• Assign categories to tasks
• Set task due dates
• Search tasks
• Filter tasks by status
• Filter tasks by priority
• Filter tasks by category
• View task statistics
• Identify overdue tasks
• Responsive user interface
• Flask-based backend
• SQLite database


TECHNOLOGIES USED

Frontend:
HTML5
CSS3
JavaScript

Backend:
Python
Flask

Database:
SQLite

Development Tools:
Visual Studio Code
Git
GitHub
Python Virtual Environment


PROJECT STRUCTURE

Personal-Task-Management-System/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── edit.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── screenshots/
│   ├── dashboard.png
│   ├── add-task.png
│   ├── edit-task.png
│   ├── filter.png
│   └── task-management.png
│
├── .gitignore
├── README.md
└── requirements.txt


APPLICATION WORKFLOW

User
  ↓
Dashboard
  ↓
Add Task
  ↓
View Tasks
  ↓
Search / Filter
  ↓
Edit / Complete / Delete Task
  ↓
Database


TASK MANAGEMENT

Each task can contain the following information:

• Task Title
• Description
• Category
• Priority
• Status
• Due Date

Tasks can be organized according to their priority and current status.


TASK PRIORITY

The system supports three priority levels:

• High
• Medium
• Low

Priority levels help users identify which tasks require more attention.


TASK STATUS

Tasks can have different statuses:

• Pending
• In Progress
• Completed

The status allows users to track the progress of their tasks.


SEARCH AND FILTERING

The application provides search and filtering functionality to make it easier to find specific tasks.

Users can search and filter tasks based on:

• Task title
• Status
• Priority
• Category


DASHBOARD

The dashboard provides an overview of the user's tasks and displays task-related statistics.

The dashboard helps users view:

• Total number of tasks
• Pending tasks
• Tasks in progress
• Completed tasks
• Other task-related information


INSTALLATION AND SETUP

1. Clone the repository

git clone https://github.com/arefa-khokhar/Personal-Task-Management-System.git


2. Navigate to the project folder

cd Personal-Task-Management-System


3. Create a virtual environment

python -m venv venv


4. Activate the virtual environment

For Windows:

venv\Scripts\activate


5. Install the required packages

pip install -r requirements.txt


6. Run the Flask application

python app.py


7. Open the application

Open a web browser and visit:

http://127.0.0.1:5000

SCREENSHOTS
![Dashboard](Dashboard.png)
![Task](<Add Task.png>)
![Task Management](<Task Management.png>)
![Task Editting](<Task Edit.png>)
![Searching and Filtering](search&filter.png)

DATABASE

The application uses SQLite for storing task information.

The database is used to store task details and perform operations such as:

• Creating tasks
• Reading tasks
• Updating tasks
• Deleting tasks


CRUD OPERATIONS

Create:
Add a new task to the system.

Read:
View existing tasks.

Update:
Edit task information.

Delete:
Remove a task from the system.


FLASK BACKEND

Flask is used to handle the server-side functionality of the application.

The Flask backend manages:

• Web page routing
• Form submissions
• Task creation
• Task updates
• Task deletion
• Task completion
• Searching and filtering
• Database communication


FRONTEND

The frontend is developed using HTML, CSS, and JavaScript.

HTML is used to create the structure of the application including forms, task cards, dashboard sections, buttons, filters, and input fields.

CSS is used for layout, colors, typography, buttons, cards, forms, responsive design, and visual styling.

JavaScript is used to provide client-side functionality and improve user interaction.


GITHUB

The project is maintained using Git and hosted on GitHub.

GitHub Repository:
https://github.com/arefa-khokhar/personal-task-management-system

Git is used to track changes and maintain different versions of the project during development.


FUTURE ENHANCEMENTS

The project can be further improved by adding:

• User registration and login
• User-specific task management
• Task reminders
• Email notifications
• Calendar integration
• Task sorting
• Dark mode
• Task completion charts
• Export tasks to PDF or CSV
• Cloud database integration


LEARNING OUTCOMES

This project helped in understanding and implementing:

• Python programming
• Flask web framework
• HTML5
• CSS3
• JavaScript
• SQLite database
• CRUD operations
• Form handling
• Server-side rendering
• Web application structure
• Git and GitHub
• Responsive web design


PROJECT PURPOSE

This project was developed for educational, academic, internship, and portfolio purposes.

It demonstrates the practical application of Python Flask web development, frontend development, database management, CRUD operations, and version control using Git and GitHub.


LICENSE

This project is intended for educational, academic, internship, and portfolio purposes.
