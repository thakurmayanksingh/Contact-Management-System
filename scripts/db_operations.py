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

    # Update All Fields
    def update_All_field(contact_id, new_name, new_phone, new_email, new_address):
        conn = sql.connect(directory)
        cur = conn.cursor()
        cur.execute('''
            UPDATE contacts
            SET name=?, phone=?, email=?, address=?
            WHERE id=?
        ''', (new_name, new_phone, new_email, new_address, contact_id))
        conn.commit()
        conn.close()

    # Update Particular Field
    def update_particular_field(contact_id, new_name=None, new_phone=None, new_email=None, new_address=None):
        conn = sql.connect(directory)
        cur = conn.cursor()

        fields = []
        values = []

        if new_name is not None:
            fields.append("name = ?")
            values.append(new_name)
        if new_phone is not None:
            fields.append("phone = ?")
            values.append(new_phone)
        if new_email is not None:
            fields.append("email = ?")
            values.append(new_email)
        if new_address is not None:
            fields.append("address = ?")
            values.append(new_address)
        if not fields:
            print("No fields to update.")
            return

        values.append(contact_id)

        query = f'''
            UPDATE contacts
            SET {", ".join(fields)}
            WHERE id = ?
        '''
        cur.execute(query, values)
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
update_particular_field(contact_id=18, new_name='Ishita')
update_All_field()    

# contacts = view_all_contact()
# for contact in contacts:
#     print(contact)
# print()

# print(search_contact(""))
# delete_contact("Kriti Singh")
# update_contact(16, "Ishita Singh Modi", "7983138050", "ishitamodi@gmail.com", "Firozabad")
