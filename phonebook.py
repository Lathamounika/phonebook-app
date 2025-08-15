import os

# File where contacts will be stored
PHONEBOOK_FILE = "phonebook.txt"

# Step 2: Initialize phonebook dictionary
phonebook = {}

# Load contacts from file
def load_contacts():
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, "r") as file:
            for line in file:
                name, phone = line.strip().split(",", 1)
                phonebook[name] = phone

# Save contacts to file
def save_contacts():
    with open(PHONEBOOK_FILE, "w") as file:
        for name, phone in phonebook.items():
            file.write(f"{name},{phone}\n")

# Function to display menu
def show_menu():
    print("\n=== Phonebook Menu ===")
    print("1. Add New Contact")
    print("2. Search for Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Exit")

# CRUD Operations

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in phonebook:
        print(f"Contact '{name}' already exists.")
    else:
        phone = input("Enter phone number: ").strip()
        phonebook[name] = phone
        save_contacts()
        print(f"Contact '{name}' added successfully.")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        save_contacts()
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def list_contacts():
    if phonebook:
        print("\n--- All Contacts ---")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phonebook is empty.")

# Step 3: Main loop
load_contacts()  # Load existing contacts at start

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        list_contacts()
    elif choice == "5":
        print("Exiting Phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
