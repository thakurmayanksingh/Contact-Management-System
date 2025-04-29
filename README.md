
# 📇 Contact Management System

Welcome to our simple and beginner-friendly **Contact Management System** — a Python project to help you manage your personal or professional contacts easily using a local database.

Whether you're storing friends’ numbers or keeping track of clients, this tool has your back!

---

## ✨ What You Can Do

- 📥 Add new contacts (name, phone, email, address)
- 👀 View all saved contacts
- 🔍 Search contacts by name or phone
- 🗑️ Delete contacts by keyword
- ✏️ Update existing contact information
- ✅ Check if a contact already exists

---

## 🧰 Built With

- 🐍 **Python 3.x**
- 🗃️ **SQLite3** (no setup needed — it's built into Python!)

---

## 🗂️ Folder Overview

```
Contact-Management-System/
├── database/
│   └── contacts.db     # Where all contact data is stored
├── main.py             # The heart of the app — all logic lives here
└── README.md           # You're reading it :)
```

---

## 🚀 How to Run It

1. **Clone this repo**:

```bash
git clone https://github.com/your-username/Contact-Management-System.git
cd Contact-Management-System
```

2. **Run the app**:

Make sure you have Python installed, then:

```bash
python main.py
```

---

## 🧪 Sample Usage

Here’s how you'd use a few functions in `main.py`:

```python
# Add a contact
add_contact("Ishita", "7983138050", "ishitamodi0gmai.com", "Firozabad")

# Delete a contact
delete_contact("Ishita")
```

Want to view contacts?

```python
contacts = view_all_contact()
for contact in contacts:
    print(contact)
```

---

## ⚙️ Functions in a Nutshell

| Function Name       | What It Does                          |
|---------------------|----------------------------------------|
| `add_contact()`     | Adds a contact                        |
| `view_all_contact()`| Shows all contacts                    |
| `search_contact()`  | Searches by name or phone             |
| `delete_contact()`  | Deletes a contact                     |
| `update_contact()`  | Updates contact info by ID            |
| `contact_exists()`  | Checks if a contact is already there  |

---

## 💡 Good to Know

- No internet needed — your contacts are stored locally.
- The database is created automatically the first time you run the program.
- Everything is wrapped safely to avoid breaking anything.

---

## 👥 Authors

- Mayank Singh  
- Ishita Modi

We both contributed to building this simple, helpful tool. Hope it makes your life easier!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
