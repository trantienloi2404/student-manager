import os
import datetime
import logging
from student_manager import StudentManager

# Application version and dynamic build date
APP_VERSION = "2.0.0"
BUILD_DATE = datetime.datetime.fromtimestamp(os.path.getmtime(__file__)).strftime(
    "%Y-%m-%d"
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def print_header():
    # Display the school logo or name at the top of each screen
    print("=================================")
    print("TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN")
    print("=================================\n")


def show_version():
    """Display the application version and dynamic build date."""
    print(f"Application Version: {APP_VERSION}")
    print(f"Build Date: {BUILD_DATE}")
    logging.info("Displayed application version and build date.")


def main():
    logging.info("Application started.")
    manager = StudentManager()
    while True:
        print_header()
        print("\nStudent Management System - Version 2.0")
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
        print("13. Export Confirmation Letter")
        print(
            "14. Toggle Deletion Restriction (currently: {})".format(
                "ON" if manager.deletion_restriction_enabled else "OFF"
            )
        )
        print("15. Show Version and Build Date")
        print("16. Exit")
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
            manager.load_from_csv()
        elif choice == "8":
            manager.export_to_json()
        elif choice == "9":
            manager.import_from_json()
        elif choice == "10":
            manager.manage_faculties()
        elif choice == "11":
            manager.manage_statuses()
        elif choice == "12":
            manager.manage_programs()
        elif choice == "13":
            manager.export_confirmation_letter()
        elif choice == "14":
            # Toggle deletion restriction
            manager.deletion_restriction_enabled = (
                not manager.deletion_restriction_enabled
            )
            print(
                "Deletion restriction is now",
                "ON" if manager.deletion_restriction_enabled else "OFF",
            )
            logging.info(
                "Toggled deletion restriction to %s",
                manager.deletion_restriction_enabled,
            )
        elif choice == "15":
            show_version()
        elif choice == "16":
            logging.info("Application exited by user.")
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    logging.info("Application terminated.")


if __name__ == "__main__":
    main()
