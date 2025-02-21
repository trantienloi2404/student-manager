import logging
from student_manager import StudentManager

# Configure logging (logs are appended to app.log)
logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Application started.")
    manager = StudentManager()
    while True:
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. Delete a student")
        print("3. Update a student")
        print("4. Search for a student")
        print("5. List all students")
        print("6. Export data to CSV")
        print("7. Import data from CSV")
        print("8. Export data to JSON")
        print("9. Import data from JSON")
        print("10. Manage Faculties")
        print("11. Manage Student Statuses")
        print("12. Manage Programs")
        print("13. Exit")
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
            manager.save_to_csv()  # Export to CSV
        elif choice == "7":
            manager.load_from_csv()  # Import from CSV
        elif choice == "8":
            manager.export_to_json()  # Export to JSON
        elif choice == "9":
            manager.import_from_json()  # Import from JSON
        elif choice == "10":
            manager.manage_faculties()
        elif choice == "11":
            manager.manage_statuses()
        elif choice == "12":
            manager.manage_programs()
        elif choice == "13":
            logging.info("Application exited by user.")
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    logging.info("Application terminated.")

if __name__ == "__main__":
    main()
