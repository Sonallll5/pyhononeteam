choice = 0
contacts = {'Name': [], 'Phone': []}

while choice != 6:
    print(''' 
    1 - Add Contact
    2 - Delete a Contact
    3 - Edit a Contact
    4 - Search a Contact
    5 - List Contacts
    6 - Exit
    ''')
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        contacts['Name'].append(name)
        contacts['Phone'].append(phone)
        print("Contact added successfully.")
    
    elif choice == 2:
        name = input("Enter the name to delete: ")
        if name in contacts['Name']:
            index = contacts['Name'].index(name)
            contacts['Name'].pop(index)
            contacts['Phone'].pop(index)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    
    elif choice == 3:
        name = input("Enter the name of the contact to edit: ")
        if name in contacts['Name']:
            index = contacts['Name'].index(name)
            new_name = input("Enter new name : ")
            new_phone = input("Enter new phone number : ")
            if new_name:
                contacts['Name'][index] = new_name
            if new_phone:
                contacts['Phone'][index] = new_phone
            print("Contact edited successfully.")
        else:
            print("Contact not found.")
    
    elif choice == 4:
        name = input("Enter the name to search: ")
        if name in contacts['Name']:
            index = contacts['Name'].index(name)
            print(f"Name: {contacts['Name'][index]}, Phone: {contacts['Phone'][index]}")
        else:
            print("Contact not found.")
    
    elif choice == 5:
        if contacts['Name']:
            print("Contacts list:")
            for name, phone in zip(contacts['Name'], contacts['Phone']):
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts available.")
    
    elif choice == 6:
        print("Exiting the contact book. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
