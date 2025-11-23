# Student Management System 

This is a small project I built for the VIT Build Your Own Project requirement.  
It’s a simple command-line tool that helps manage basic information about students and teachers.  
The idea was to keep everything easy to use and organised, so the system mainly focuses on storing, updating, deleting and viewing records.

## Features

### Student Section
- Add a new student  
- View all students  
- Update an existing student  
- Delete a student  

### Teacher Section
- Add a new teacher  
- View teachers  
- Update teacher details  
- Delete a teacher  

## Technologies Used
- Python 3  
- SQLite (comes built-in with Python)  
- Basic object-oriented concepts  
- Simple modular structure with separate files  

## Project Structure

The project is divided into a few files to keep things neat:

Main.py -> main program + menus
database.py -> all the database queries (CRUD)
models.py -> Student and Teacher classes
school_management.db -> database file (created automatically)

## How to Run

1. Make sure Python 3 is installed.  
2. Open the project folder in a terminal.  
3. Run:
python Main.py
The database file (`school_management.db`) will be created when you run the project for the first time.
## Testing Tips

You can test each option by using the menu in the terminal.  
Try things like:

- Adding a student/teacher  
- Updating the details  
- Viewing the list  
- Trying wrong inputs (to see how the program responds)  
- Entering duplicate IDs  

## Screenshots

(These can be added later once the program is running.)

Suggested screenshots:
- Main menu  
- Adding a student  
- Viewing all students  
- Updating a teacher  
- Deleting a record  

## Author

This project was created as part of the BYOP evaluation at VIT University.  
I built the core logic using Python and used SQLite for storing the records in a simple way.
