from scripts import db_operations
from scripts import initialize_db
import re


def authenticate_user():
    print('''
LOGIN
1. Admin (Includes Delete and Update Operation)
2. Guest (All Operations except Delete and Update)''')
    try:
        role = input("Select Role (1-Admin, 2-Guest): ").strip()
        if role == "1" or role.lower() == 'admin':
            password = input("Enter Password (Admin Login): ").strip()
            if password == "admin":
                print("Access Granted! Logging In as Administrator.")
                return 'admin'
            else:
                print("Wrong Password! Switching to Guest mode.")
                return 'guest'

        elif role == '2' or role.lower() == 'guest':
            print("Logged In as Guest")
            return 'guest'

        else:
            print("Invalid Input! Defaulting to guest mode.")
            return 'guest'
    except Exception as e:
        print(f"Error Faced in Login: {e}")


if __name__ == '__main__':
    print("Welcome to Contact Management System!!!")
    initialize_db.main()
    role = authenticate_user()
    while True:
        try:
            if role == 'admin':
                print('''1. Add Contact
2. Delete Contact
3. Update Contact
4. Search Contact
5. View Contact
6. Export to CSV
7. Exit''')

                inp = int(input("-> "))
                try:
                    if inp == 1:
                        print("Fill the below fields to add a contact. (* means it is mandatory field)")

                        inp_name = str(input("Enter Name (*Required): "))
                        if not inp_name.strip() or inp_name[0].isdigit():
                            print("Error: Name is required and cannot be blank or start with a digit.")
                            continue

                        inp_phone = str(input("Enter Phone (*Required (enter phone number only no code and space..)): "))
                        if not inp_phone.isdigit() or len(inp_phone) != 10:
                            print("Error: Phone number must be 10 digits.")
                            continue

                        if db_operations.contact_exists(inp_name.strip(), inp_phone.strip()):
                            print("Error! Contact with this name and phone already exists.\n")
                            continue

                        inp_email = str(input("Enter Email: "))
                        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
                        if inp_email and not re.match(email_regex, inp_email):
                            print("Error: Invalid email format.")
                            continue

                        inp_address = str(input("Enter Address: "))
                        if len(inp_address) > 150:
                            print("Warning: Address too long. Limit it to 150 characters.")
                            continue

                        db_operations.add_contact(inp_name, inp_phone, inp_email, inp_address)

                    elif inp == 2:
                        keyword = str(input("Enter Keyword for deleting (Name or Phone Number): "))
                        db_operations.delete_contact(keyword)

                    elif inp == 3:
                        print("You can choose to update all fields or just specific ones.")
                        update_choice = input("Do you want to update all fields? (yes/no): ").strip().lower()

                        contact_id = input("Enter Contact ID (if you don't know it, search for it first): ").strip()

                        if update_choice == 'yes':
                            name = input("Enter New Name (*Required): ").strip()
                            phone = input("Enter New Phone (*Required): ").strip()
                            email = input("Enter New Email: ").strip()
                            address = input("Enter New Address: ").strip()

                            db_operations.update_All_field(contact_id, name, phone, email, address)
                            print("Contact updated successfully.")

                        elif update_choice == 'no':
                            print("Leave blank to skip any field.")
                            name = input("New Name: ").strip() or None
                            phone = input("New Phone: ").strip() or None
                            email = input("New Email: ").strip() or None
                            address = input("New Address: ").strip() or None

                            db_operations.update_particular_field(
                                contact_id,
                                new_name=name,
                                new_phone=phone,
                                new_email=email,
                                new_address=address
                            )
                            print("Contact updated successfully.")
                        else:
                            print("Invalid input! Returning to menu.")


                    elif inp == 4:
                        keyword = str(input("Enter Keyword (Name or Phone Number): "))
                        searched_contacts = db_operations.search_contact(keyword)

                        if not searched_contacts:
                            print("No Contact Found")
                        else:
                            for contact in searched_contacts:
                                print(contact)


                    elif inp == 5:
                        contacts_names = db_operations.view_all_contact()
                        for i, contact in enumerate(contacts_names, start=1):
                            print(f"{i}. {contact}")
                        print()

                    elif inp == 6:
                        filename = str(input("Enter CSV filename to export. (default: contacts_export.csv): ")).strip()
                        if not filename:
                            filename = "contacts_export.csv"
                        db_operations.export_to_csv(filename)

                    elif inp == 7:
                        print("Thank You for using the app.!")
                        break

                    else:
                        print("Wrong Input! Enter Value between (1-7)\n")

                except Exception as e:
                    print(f"Error: {e}")

            elif role == 'guest':
                print('''1. Add Contact
2. Search Contact
3. View Contact
4. Export to CSV
5. Exit''')

                inp = int(input("-> "))
                try:
                    if inp == 1:
                        print("Fill the below fields to add a contact. (* means it is mandatory field)")

                        inp_name = str(input("Enter Name (*Required): "))
                        if not inp_name.strip() or inp_name[0].isdigit():
                            print("Error: Name is required and cannot be blank or start with a digit.")
                            continue

                        inp_phone = str(
                            input("Enter Phone (*Required (enter phone number only no code and space..)): "))
                        if not inp_phone.isdigit() or len(inp_phone) != 10:
                            print("Error: Phone number must be 10 digits.")
                            continue

                        if db_operations.contact_exists(inp_name.strip(), inp_phone.strip()):
                            print("Error! Contact with this name and phone already exists.\n")
                            continue

                        inp_email = str(input("Enter Email: "))
                        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
                        if inp_email and not re.match(email_regex, inp_email):
                            print("Error: Invalid email format.")
                            continue

                        inp_address = str(input("Enter Address: "))
                        if len(inp_address) > 150:
                            print("Warning: Address too long. Limit it to 150 characters.")
                            continue

                        db_operations.add_contact(inp_name, inp_phone, inp_email, inp_address)

                    elif inp == 2:
                        keyword = str(input("Enter Keyword (Name or Phone Number): "))
                        searched_contacts = db_operations.search_contact(keyword)
                        for contact in searched_contacts:
                            print(contact)

                    elif inp == 3:
                        contacts_names = db_operations.view_all_contact()
                        for i, contact in enumerate(contacts_names, start=1):
                            print(f"{i}. {contact}")
                        print()

                    elif inp == 4:
                        filename = str(input("Enter CSV filename to export. (default: contacts_export.csv): ")).strip()
                        if not filename:
                            filename = "contacts_export.csv"
                        db_operations.export_to_csv(filename)

                    elif inp == 5:
                        print("Thank You for using the app.!")
                        break

                    else:
                        print("Wrong Input! Enter Value between (1-5)\n")

                except Exception as e:
                    print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")