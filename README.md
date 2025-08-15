# Phonebook Application

A simple command-line **Phonebook Application** built with Python.  
It supports **CRUD operations** — Add, Search, Delete, and List Contacts — with data stored persistently in a text file.

## Features
- 📇 **Add New Contact** – Save a person's name and phone number.
- 🔍 **Search Contact** – Find a contact by name.
- ❌ **Delete Contact** – Remove a contact from the phonebook.
- 📜 **List All Contacts** – View all saved contacts.
- 💾 **Persistent Storage** – Contacts are stored in a text file (`phonebook.txt`) so data is retained between sessions.

## Technologies Used
- Python 3
- File Handling (`open`, `read`, `write`)
- Basic I/O operations

## How It Works
The program uses a dictionary to store contacts in memory and a `.txt` file for permanent storage.

**File structure:**
```
phonebook.py        # Main Python program
phonebook.txt       # Contact storage file
```

**Data format in `phonebook.txt`:**
```
Name,PhoneNumber
John Doe,9876543210
Jane Smith,9123456789
```

## How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/phonebook-app.git
   cd phonebook-app
   ```

2. **Run the program**:
   ```bash
   python phonebook.py
   ```

3. **Follow the menu options**:
   ```
   === Phonebook Menu ===
   1. Add New Contact
   2. Search for Contact
   3. Delete Contact
   4. List All Contacts
   5. Exit
   ```

## Example Usage
```
Enter your choice (1-5): 1
Enter contact name: Alice
Enter phone number: 9876543210
Contact 'Alice' added successfully.

Enter your choice (1-5): 4
--- All Contacts ---
Alice: 9876543210
```

## Future Improvements
- Add email address support
- Import/export contacts to CSV
- GUI version using Tkinter

---

**Author:** [Your Name]  
📧 Contact: your.email@example.com
