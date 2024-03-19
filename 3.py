phone_book = {}
while True:
    print("Phone Book: ")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Delete contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name= input("Enter contact name: ")
        number = input("Enter contact number: ")
        phone_book[name] = number
        print("\nContact added successfully.")

    elif choice == '2':
        name = input("Enter contact name: ")
        print(f"{name}'s phone number is {number}")

    elif choice == '3':
        name = input("Enter contact name: ")
        print("Contact deleted successfully.")

