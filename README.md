
# 📇 Contact Management System

A simple **Contact Management System** built with **Python** and **SQLite**. This program allows users to add, view, search, update, and delete contact information using a local database.

---

## ✅ Features

- Add a new contact (name, phone, email, address)
- View all saved contacts
- Search for contacts by name or phone number
- Delete contacts by keyword (name or phone)
- Update an existing contact by ID
- Check if a contact already exists

---

## 🗃️ Tech Stack

- **Python 3.x**
- **SQLite3** (built-in with Python)
- No external libraries required

---

## 📂 Project Structure

```
Contact-Management-System/
├── database/
│   └── contacts.db     # SQLite database file
├── main.py             # Core logic for contact operations
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Contact-Management-System.git
cd Contact-Management-System
```

### 2. Run the Code

Make sure you have Python 3 installed.

```bash
python main.py
```

---

## 🧠 Example Usage in `main.py`

```python
add_contact("ishita", "7983138050", "ishitamodi0gmai.com", "fzd")
delete_contact("ishita")
```

Uncomment lines to:

- View all contacts:
```python
contacts = view_all_contact()
for contact in contacts:
    print(contact)
```

- Search for a contact:
```python
print(search_contact("ishita"))
```

- Update a contact:
```python
update_contact(1, "New Name", "1234567890", "new@email.com", "New Address")
```

---

## 🛠 Functions Overview

| Function Name       | Description                         |
|---------------------|-------------------------------------|
| `add_contact()`     | Adds a new contact to the database. |
| `view_all_contact()`| Retrieves all contacts.             |
| `search_contact()`  | Finds contacts by keyword.          |
| `delete_contact()`  | Deletes a contact by name/phone.    |
| `update_contact()`  | Updates contact data by ID.         |
| `contact_exists()`  | Checks if a contact already exists. |

---

## 📌 Notes

- The database will be created automatically if it doesn’t exist.
- All functions safely open and close the connection to avoid leaks.
- The database is stored in `database/contacts.db`.

---

## 👤 Author

- Ishita Modi (with contributions from team members)

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
