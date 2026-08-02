from library import Library

library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Register Member")
    print("4. Display Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.register_member()

    elif choice == "4":
        library.display_members()

    elif choice == "5":
        library.borrow_book()

    elif choice == "6":
        library.return_book()

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")