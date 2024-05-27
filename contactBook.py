import sqlite3

#Ibukun Adenuga
#Contact Book
#5/17/24


# Function to create a database and contacts table
def create_database():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new contact
def add_contact(name, address, phone, email):
    if len(phone) != 11 or not phone.isdigit():
        print("Phone number must be 11 digits long and contain only digits.")
        return
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, address, phone, email) VALUES (?, ?, ?, ?)",
              (name, address, phone, email))
    conn.commit()
    conn.close()

# Function to list all contacts
def list_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    for contact in contacts:
        print(contact)
    conn.close()

# Function to find a contact by name
def find_contact(name):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE name=?", (name,))
    contact = c.fetchone()
    if contact:
        print(contact)
    else:
        print("Contact not found")
    conn.close()

# Function to delete a contact by name
def delete_contact(name):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()
    conn.close()

# Main function to interact with the user
def main():
    create_database()
    while True:
        print("\n1. Add Contact\n2. List Contacts\n3. Find Contact\n4. Delete Contact\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, address, phone, email)
            print("Contact added successfully!")
        elif choice == '2':
            print("\nList of Contacts:")
            list_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            find_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
            print("Contact deleted successfully!")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()