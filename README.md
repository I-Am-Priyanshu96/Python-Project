# Python-Project

#PROJECT 1 

ATM Simulation and Transaction System

A command-line interface (CLI) application written in Python that simulates standard ATM operations. It features secure PIN authentication with limited attempts, balance inquiries, cash transactions, and a printed transaction summary upon exit.

🚀 Features

• Secure Authentication: Restricts access using a 4-digit PIN verification with a maximum of 3 entry attempts before blocking the card.
• Core Banking Operations: Allows users to check account balance, deposit money, and withdraw funds with real-time balance checks.
• Transaction Logging: Dynamically logs all deposits and withdrawals during the session.
• Mini-Statement Output: Prints a chronological history of all performed transactions when the user chooses to exit.

🛠️ Menu Options

1. Balance: View the current available account balance.
2. Deposit: Add a custom monetary amount to the account balance.
3. Withdraw: Deduct funds from the account after validating against the available balance to prevent overdrawing.
4. Exit: Displays a complete summary of deposits and withdrawals, followed by a graceful termination of the application session.

💻 How to Run

1. Ensure you have Python 3.x installed.
2. Save the code to a file named atm_simulation.py.
3. Run the script via your terminal or command prompt:
     python atm_simulation.py

   
#PROJECT 2
Student Grading and Management System

A lightweight, interactive CLI-based Student Management System written in Python. It calculates average marks, assigns grades, tracks the top-performing student, and allows users to add new student data dynamically through a menu-driven interface.

🚀 Features

• Grade Calculation: Automatically computes the average marks across 3 subjects and assigns grades (A, B, C, or F).
• Topper Tracking: Identifies and displays the student with the highest total score.
• Dynamic Data Input: Add new students with validation to ensure marks stay between 0 and 100.
• Menu-Driven Interface: Interactive looping menu to manage data seamlessly.

📊 Grading Criteria


Average Score	Grade
≥ 85	A
≥ 70	B
≥ 50	C
< 50	F


🛠️ Menu Options

1. Add student: Input a new student name and their marks for 3 subjects. Includes duplication checks and out-of-range validation.
2. View all: Display the raw dictionary containing all student names and their respective marks.
3. Show Topper: Recalculates and displays the name of the student with the highest score.
4. Exit: Gracefully terminates the application.

💻 How to Run

1. Ensure you have Python 3.x installed.
2. Save the code code to a file named student_management.py.
3. Run the script via your terminal or command prompt
      python student_management.py
