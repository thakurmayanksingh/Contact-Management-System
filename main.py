from scripts import db_operations
from scripts import initialize_db

if __name__ == '__main__':
    print("Welcome to Contact Management System!!!")
    initialize_db.main()
    while True:
        print('''1. Add Contact
2. Delete Contact
3. Update Contact
4. Search Contact
5. View Contact
6. Exit''')
        inp = int(input("-> "))
        try:
            if inp == 1:
                print("Fill the below fields to add a contact. (* means it is mandatory field)")
                inp_name = str(input("Enter Name (*Required): "))
                inp_phone = str(input("Enter Phone (*Required): "))
                inp_email = str(input("Enter Email: "))
                inp_address = str(input("Enter Address: "))
                db_operations.add_contact(inp_name, inp_phone, inp_email, inp_address)
            elif inp == 2:
                keyword = str(input("Enter Keyword for deleting (Name or Phone Number): "))
                db_operations.delete_contact(keyword)
            elif inp == 3:
                print("Fill the below fields to update a contact. (* means it is mandatory field)")
                inp_contact_id = str(input("Enter Contact ID (id to update if you don't know then search nd get it.): "))
                inp_name = str(input("Enter New Name (*Required): "))
                inp_phone = str(input("Enter New Phone (*Required): "))
                inp_email = str(input("Enter New Email: "))
                inp_address = str(input("Enter New Address: "))
                db_operations.update_contact(inp_contact_id, inp_name, inp_phone, inp_email, inp_address)
            elif inp == 4:
                keyword = str(input("Enter Keyword (Name or Phone Number): "))
                searched_contacts = db_operations.search_contact(keyword)
                for contact in searched_contacts:
                    print(contact)
            elif inp == 5:
                contacts_names = db_operations.view_all_contact()
                # for contact in contacts_names:
                #     print(contact)
                print(contacts_names)
                print()
            elif inp == 6:
                print("Thank You for using the app.!")
                break
            else:
                print("Wrong Input! Enter Value between (1-5)\n")
        except Exception as e:
            print(f"Error: {e}")