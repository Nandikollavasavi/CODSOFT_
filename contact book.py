# Contact Book Application in Python

contacts = []

def show_menu():
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = [c for c in contacts if keyword.lower() in c["name"].lower() or keyword in c["phone"]]
    if found:
        print("\nSearch Results:")
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contact found.")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave blank to keep current value.")
            name = input(f"Enter new name ({contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"Enter new phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"Enter new email ({contacts[index]['email']}): ") or contacts[index]['email']
            address = input(f"Enter new address ({contacts[index]['address']}): ") or contacts[index]['address']
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"Contact '{deleted['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
