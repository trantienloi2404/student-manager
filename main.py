from student_manager import StudentManager


def main():
    manager = StudentManager()
    while True:
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. Delete a student")
        print("3. Update a student")
        print("4. Search for a student")
        print("5. List all students")
        print("6. Save data to CSV")
        print("7. Manage Faculties")
        print("8. Manage Student Statuses")
        print("9. Manage Programs")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.delete_student()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.search_student()
        elif choice == "5":
            manager.list_students()
        elif choice == "6":
            manager.save_to_csv()
        elif choice == "7":
            manager.manage_faculties()
        elif choice == "8":
            manager.manage_statuses()
        elif choice == "9":
            manager.manage_programs()
        elif choice == "10":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
