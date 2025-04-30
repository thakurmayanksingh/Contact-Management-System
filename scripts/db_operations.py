import sqlite3 as sql
import csv

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
        conn=sql.connect(directory)
        cur=conn.cursor()
        cur.execute('''
            DELETE FROM contacts WHERE name like ? OR phone like ?;        
        ''', (f"%{keyword}", f"%{keyword}"))
        conn.commit()
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

    def export_to_csv(filename="contacts_export.csv"):
        try:
            conn = sql.connect(directory)
            cur = conn.cursor()
            cur.execute('''
                SELECT * FROM contacts;
            ''')
            rows = cur.fetchall()
            conn.close()
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Name', 'Phone', 'Email', 'Address'])
                writer.writerows(rows)
            print(f"Contacts Exported Successfully to {filename}\n'")
        except Exception as e:
            print(f"Contacts Failed to Export.\nError: {e}")

except Exception as e:
    print(f"Error: {e}")

# contacts = view_all_contact()
# for contact in contacts:
#     print(contact)
# print()

# print(search_contact(""))
# delete_contact("Kriti Singh")
# update_contact(16, "Ishita Singh Modi", "7983138050", "ishitamodi@gmail.com", "Firozabad")
