import sqlite3 as sql

directory = "database/contacts.db"

try:
    # Add Contact Function
    def add_contact(name, phone, email, address):
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO contacts (name, phone, email, address)
            VALUES (?, ?, ?, ?);
            ''', (name, phone, email, address))
        conn.commit()
        conn.close()

    # View Contact
    def view_all_contact():
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            SELECT name, phone, email, address FROM contacts;
        ''')
        rows = cur.fetchall()
        conn.close()
        return rows

    # Search Contact
    def search_contact(keyword):
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM contacts 
            WHERE name LIKE ? OR phone LIKE ?;
        ''', (f"%{keyword}", f"%{keyword}"))
        rows = cur.fetchall()
        conn.close()
        if rows:
            return rows
        else:
            return "No Contact Found"

    # Delete Contact
    def delete_contact(keyword):
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?;
        ''', (f"%{keyword}%", f"%{keyword}%"))
        matches = cur.fetchall()

        if not matches:
            print("No contact found matching that keyword.")
        elif len(matches) == 1:
            contact = matches[0]
            cur.execute('DELETE FROM contacts WHERE id = ?', (contact[0],))
            conn.commit()
            print(f"Deleted contact: {contact}")
        else:
            print("Multiple contacts found:")
            for idx, contact in enumerate(matches, 1):
                print(f"{idx}. Name: {contact[1]}, Phone: {contact[2]}")

            try:
                choice = int(input("Enter the number of the contact you want to delete: "))
                if 1 <= choice <= len(matches):
                    selected_contact = matches[choice - 1]
                    cur.execute('DELETE FROM contacts WHERE id = ?', (selected_contact[0],))
                    conn.commit()
                    print("Contact deleted.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Deletion cancelled.")

        conn.close()


    # Update Contact
    def update_contact(contact_id, new_name, new_phone, new_email, new_address):
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            UPDATE contacts
            SET name=?, phone=?, email=?, address=?
            WHERE id=?
        ''', (new_name, new_phone, new_email, new_address, contact_id))
        conn.commit()
        conn.close()

    def contact_exists(name, phone):
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM contacts WHERE name = ? AND phone = ?
        ''', (name, phone))
        result = cur.fetchone()
        conn.close()
        return result is not None

except Exception as e:
    print(f"Error: {e}")
add_contact("shruti", "7967488576", "ishitamodi0gmai.com", "fzd")
# contacts = view_all_contact()
# for contact in contacts:
#     print(contact)
# print()

# print(search_contact(""))
# delete_contact("ishita")
# update_contact(16, "Ishita Singh Modi", "7983138050", "ishitamodi@gmail.com", "Firozabad")
