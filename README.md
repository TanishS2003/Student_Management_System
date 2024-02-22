The Student Management System is a Python application built using the Tkinter library for creating a graphical user interface (GUI). It is designed to manage student information, allowing 
users to perform operations such as adding, updating, deleting, and searching for student records.


Features:
1. Add Student: Enter student details including Roll No., Name, Email, Gender, Contact, Date of Birth, and Address.
2. Update Student: Modify existing student information.
3. Delete Student: Remove a student from the system.
4. Search Student: Search for students based on Roll No., Name, or Contact.
5. Display All Students: View a list of all registered students.
6. Data Validation: Ensure that all required fields are filled before performing operations.
7. Database Integration: Utilize a MySQL database to store and retrieve student records.


Prerequisites:
Before running the program, ensure the following dependencies are installed:
pip install tk tkcalendar pymysql


Usage:
1. Add Student:
Fill in the required information.
Click the "Add" button.

2. Update Student:
Select a student from the displayed list.
Modify the information.
Click the "Update" button.

3. Delete Student:
Select a student from the displayed list.
Click the "Delete" button.

4. Search Student:
Choose the search criteria (Roll No., Name, Contact).
Enter the search text.
Click the "Search" button.

5. Display All Students:
Click the "Show All" button.


Database Configuration:
Update the database connection details in the pymysql.connect() function inside the methods (add_students, fetch_data, update, delete, search_data) to match your MySQL database setup.

Happy coding! 🚀
