elif inp == 4:
                        keyword = str(input("Enter Keyword (Name or Phone Number): "))
                        searched_contacts = db_operations.search_contact(keyword)

                        if not searched_contacts:
                            print("No Contact Found")
                        else:
                            for contact in searched_contacts:
                                print(contact)