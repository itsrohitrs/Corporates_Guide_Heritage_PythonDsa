# ==========================================================
# Question 1: Dictionary Operations
# ==========================================================

print("=" * 60)
print("Question 1: Dictionary Operations")
print("=" * 60)

# Create a Dictionary
student = {
    "Name": "Rohit",
    "Age": 21,
    "Course": "B.Tech"
}

# Print all details
print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)

# Access a value
print("\nAccessing Values:")
print("Name :", student["Name"])
print("Course :", student["Course"])

# Add a new key-value pair
student["City"] = "Kolkata"

print("\nAfter Adding City:")
print(student)

# Update an existing value
student["Age"] = 22

print("\nAfter Updating Age:")
print(student)

# Delete a key
del student["Course"]

print("\nAfter Deleting Course:")
print(student)


# ==========================================================
# Question 2: Phone Book Management System
# ==========================================================

phone_book = {}

while True:

    print("\n" + "=" * 60)
    print("PHONE BOOK MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    # ==================================================
    # 1. Add Contact
    # ==================================================

    if choice == 1:

        name = input("Enter Contact Name: ")
        phone = input("Enter Phone Number: ")

        phone_book[name] = phone

        print("Contact Added Successfully!")

    # ==================================================
    # 2. Search Contact
    # ==================================================

    elif choice == 2:

        name = input("Enter Contact Name: ")

        if name in phone_book:
            print("Phone Number:", phone_book[name])
        else:
            print("Contact Not Found!")

    # ==================================================
    # 3. Update Contact
    # ==================================================

    elif choice == 3:

        name = input("Enter Contact Name: ")

        if name in phone_book:

            new_phone = input("Enter New Phone Number: ")

            phone_book[name] = new_phone

            print("Contact Updated Successfully!")

        else:
            print("Contact Not Found!")

    # ==================================================
    # 4. Delete Contact
    # ==================================================

    elif choice == 4:

        name = input("Enter Contact Name: ")

        if name in phone_book:

            del phone_book[name]

            print("Contact Deleted Successfully!")

        else:
            print("Contact Not Found!")

    # ==================================================
    # 5. Display All Contacts
    # ==================================================

    elif choice == 5:

        if len(phone_book) == 0:

            print("Phone Book is Empty!")

        else:

            print("\nAll Contacts:")

            for name, phone in phone_book.items():
                print(name, ":", phone)

    # ==================================================
    # 6. Exit
    # ==================================================

    elif choice == 6:

        print("\nThank You! Exiting Phone Book...")
        break

    # ==================================================
    # Invalid Choice
    # ==================================================

    else:

        print("Invalid Choice! Please Try Again.")