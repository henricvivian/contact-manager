class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter the name of the contact: ")
        phone = input("Enter the phone number of the contact: ")
        email = input("Enter the email address of the contact: ")
        self.contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully.")

    def search_contact(self):
        name = input("Enter the name of the contact to search: ")
        contact = self.contacts.get(name)
        if contact:
            print("Name:", name)
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
        else:
            print("Contact not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, contact in self.contacts.items():
                print("Name:", name)
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print()

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            print("\n********** Contact Manager **********")
            print("1. Add contact")
            print("2. Search contact")
            print("3. Display all contacts")
            print("4. Delete contact")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.search_contact()
            elif choice == "3":
                self.display_contacts()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                print("Thank you for using Contact Manager!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.run()
