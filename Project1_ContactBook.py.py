contacts = []

while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("\nAdd Contact")

    elif choice == 2:
        print("\nView Contacts")

    elif choice == 3:
        print("\nSearch Contact")

    elif choice == 4:
        print("\nDelete Contact")

    elif choice == 5:
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")
        
    if choice == 1:
        name = input("Enter Name: ")
        phone =int(input("Enter Phone Number: "))

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

        print("Contact Added Successfully!")
        
        
    elif choice == 2:
        if len(contacts) == 0:
            print("No Contacts Found!")

        else:
            print("\n--- Contact List ---")

            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("------------------")
                
                
    elif choice == 3:
        search_name = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

                found = True
                break

        if found == False:
            print("Contact Not Found!")
            
            
    elif choice == 4:
        delete_name = input("Enter name to delete: ")

        found = False

        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
                print("Contact Deleted Successfully!")

                found = True
                break

        if found == False:
            print("Contact Not Found!")
            
    
    else:
        print("Invalid Choice!")        
    