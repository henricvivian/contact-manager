contacts = {}  # Initialize an empty dictionary to store contacts

def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print("Name: ", name)
        print("Phone: ", contacts[name]["phone"])
        print("Email: ", contacts[name]["email"])
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name in contacts:
            print("Name: ", name)
            print("Phone: ", contacts[name]["phone"])
            print("Email: ", contacts[name]["email"])
            print("")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n********** Contact Manager **********")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Display all contacts")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you for using Contact Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
