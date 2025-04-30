# Contact Management System

Welcome!  
This is a beginner-friendly **Contact Management System** built in Python that helps you manage contacts locally using a simple SQLite database.

Whether you're storing friends’ numbers or managing a professional network, this lightweight app helps keep everything organized — without needing an internet connection or complex setup.

---

## Features

- Add new contacts with name, phone number, email, and address
- View all saved contacts in one go
- Search contacts by name or phone number
- Update existing contact details
- Delete contacts using keywords
- Check if a contact already exists

Simple. Functional. Efficient.

---

## Tech Stack

- **Python 3.x** – Clean and modular script-based application  
- **SQLite3** – Built-in lightweight database (no installation required)

---

## Project Structure

```
Contact-Management-System/
├── database/
│   └── contacts.db       # SQLite database storing all contact information
│
├── main.py               # Core application logic and CLI interface
│                         # Includes all functions: add, view, update, delete, search
│
└── README.md             # This documentation file explaining the project
```

> The `contacts.db` file is auto-generated the first time you run the program.

---

## Getting Started

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/Contact-Management-System.git
cd Contact-Management-System
```

2. **Run the application**:

Ensure Python is installed, then launch the app with:

```bash
python main.py
```

The app will create a `contacts.db` file inside the `database/` folder if it doesn’t already exist.

---

## Sample Code Usage

Here's how you might use functions directly within `main.py`:

```python
# Adding a new contact
add_contact("Ishita", "7983138050", "ishitamodi0@gmail.com", "Firozabad")

# Viewing all contacts
for contact in view_all_contact():
    print(contact)

# Updating a contact (using contact ID)
update_contact(1, "Ishita Modi", "9999999999", "ishita@example.com", "Agra")

# Deleting a contact
delete_contact("Ishita")

# Searching for a contact
search_contact("Ishita")
```

---

## Function Reference

| Function             | Description                                |
|----------------------|--------------------------------------------|
| `add_contact()`      | Adds a new contact to the database          |
| `view_all_contact()` | Displays a list of all contacts             |
| `search_contact()`   | Searches by name or phone number            |
| `delete_contact()`   | Deletes contact(s) matching the keyword     |
| `update_contact()`   | Updates contact information based on ID     |
| `contact_exists()`   | Checks if a contact is already stored       |

---

## Why This Project?

This project was designed to be a simple and practical way to explore:

- How Python works with local databases
- Structuring CLI-based apps
- Writing reusable and maintainable code
- Handling basic user operations and edge cases

It’s great for beginners learning Python or anyone who wants a functional offline tool.

---

## Authors

- **Mayank Singh** — [LinkedIn](https://www.linkedin.com/in/mayank-singh-367572246/) • [GitHub](https://github.com/thakurmayanksingh)
- **Ishita Modi** — [LinkedIn](https://www.linkedin.com/in/ishita-modi-155676341/) • [GitHub](https://github.com/ishita230105)

We collaborated on this project to improve our development skills and to build something helpful for the community.
---

*Thanks for checking it out! Contributions and suggestions are always welcome.*
