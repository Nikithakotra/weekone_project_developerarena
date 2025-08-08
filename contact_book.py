# contact_book.py

def add_contact(filename):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    
    with open(filename, 'a') as file:
        file.write(f"Name: {name}, Phone: {phone}, Email: {email}\n")
    print("Contact added successfully!\n")

def view_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.\n")
                return
            print("\n--- Contact List ---")
            for contact in contacts:
                print(contact.strip())
            print()
    except FileNotFoundError:
        print("No contacts file found.\n")

def search_contact(filename):
    search_name = input("Enter the name to search: ").lower()
    found = False
    try:
        with open(filename, 'r') as file:
            for contact in file:
                if search_name in contact.lower():
                    print("\nContact Found:")
                    print(contact.strip())
                    found = True
        if not found:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts file found.\n")

def main():
    filename = "contacts.txt"
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact(filename)
        elif choice == '2':
            view_contacts(filename)
        elif choice == '3':
            search_contact(filename)
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")

if __name__ == "__main__":
    main()
