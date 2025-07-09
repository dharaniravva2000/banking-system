🏦 Python Bank System

A simple command-line banking system built with Python. This system allows admin users to manage customer accounts, transfer money, perform CRUD operations on customers, and save/load data using JSON.

📂 Project Structure

bash

Copy

Edit
.

├── bank_system.py            # Main bank system logic

├── customer_account.py       # Customer class (not shown here)

├── admin.py                  # Admin class (not shown here)

├── bank_data.json            # (Optional) Data persistence file

└── README.md                 # This file

🧠 Features

Admin login system

Create and manage customer accounts

Money transfers between accounts

Save and load data from .json files

Admin profile management

Generate management reports (to be implemented)

CLI-based interaction

🔧 Prerequisites

Python 3.x installed on your system

▶️ Getting Started

Clone the repository

bash

Copy

Edit

git clone <(https://github.com/dharaniravva2000/banking-system/)>

cd <banking-system>

Ensure the following files exist

bank_system.py

customer_account.py

admin.py

Run the application

bash

Copy

Edit

python bank_system.py

👤 Admin Access

If no bank_data.json is found, two default admin accounts will be created:

Username	Password

id1188	1441

id3313	2442

📦 Data Persistence

All customer and admin data can be saved into a .json file using the Admin Menu → Save to File option.

You can load data from an existing file via Admin Menu → Load from File.

📘 Functional Overview

Admin Menu Options

Transfer Money between customers

Access customer profile and account options

Delete a customer

Print all customers’ details

Update admin profile

Create new customer

Generate management report (TBD)

Save to JSON file

Load from JSON file

Sign out

📈 Sample Default Customers

If no data file is found, these customers are added:

Adam Smith – Current account

David White – Savings account

Alice Churchil – Premium Savings account

Ali Abdallah – Basic account

🧩 To Do / Enhancements

Implement customer login and authentication

Implement GUI using Tkinter or web-based UI

Export reports (PDF, Excel)

Add interest calculation and transaction history

🧑‍💻 Contributors

Dharani Ravva

🛡️ License

This project is licensed under the MIT License – feel free to use, modify, and share!

