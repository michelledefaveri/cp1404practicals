"""
CP1404 Practical - Project Management
Estimated time = 1 hour
Actual time = 2 hours 35 minutes
"""

from datetime import datetime
from project import Project


DEFAULT_FILENAME = "projects.txt"

MENU = """
    - (L)oad projects
    - (S)ave projects
    - (D)isplay projects
    - (F)ilter projects by date
    - (A)dd new project
    - (U)pdate project
    - (Q)uit"""

def main():
    """Run the project management program and handle user menu choices."""
    current_file = DEFAULT_FILENAME
    projects = load_projects(current_file)
    choice = ""
    while choice != "q":
        print(MENU)
        choice = input(">>> ").lower()
        try:
            if choice == "l":
                filename = input("Filename to load from: ")
                projects = load_projects(filename)
                current_file = filename  # update current file
            elif choice == "s":
                filename = input("Filename to save to: ")
                save_projects(projects, filename)
                current_file = filename  # update current file
            elif choice == "d":
                display_projects(projects)
            elif choice == "f":
                filter_projects_by_date(projects)
            elif choice == "a":
                add_new_project(projects)
            elif choice == "u":
                update_project(projects)
            elif choice == "q":
                save_input = input(f"Would you like to save to {current_file}? (y/n) ").lower()
                if save_input.startswith("y"):
                    save_projects(projects, current_file)
                else:
                    print("Projects not saved.")
                print("Thank you for using custom-built project management software.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter the correct type of value.")


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []  # List to store Project objects
    try:
        with open(filename, "r") as file:  # Open file for reading
            next(file)  # Skip header line
            for line in file:
                if line.strip() == "":  # Skip empty lines
                    continue
                parts = line.strip().split("\t")  # Split line into fields

                # Convert fields to appropriate types
                name = parts[0]
                start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion = int(parts[4])

                project = Project(name, start_date, priority, cost_estimate, completion)
                # Add project to list
                projects.append(project)
        print("Loaded", len(projects), "projects from", filename)
    except FileNotFoundError:
        print(f"{filename} not found")
    return projects

def display_projects(projects):
    """Display complete and incomplete projects."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    completed_projects = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(" ", project)

    print("Completed projects:")
    for project in completed_projects:
        print(" ", project)

def save_projects(projects, filename):
    """Save projects to a tab-delimited file."""
    with open(filename, "w") as file:
        # Write the header line
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            # Write each project's data, formatting the date as dd/mm/yyyy
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion}\n")
    print("Saved", len(projects), "projects to", filename)

def filter_projects_by_date(projects):
    """Display projects starting on or after a user-specified date."""
    # Prompt user for a date and convert input string to a date object
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please enter dd/mm/yyyy.")
        return
    # Filter projects starting on or after the specified date
    filtered_projects = [project for project in projects if project.get_start_date() >= filter_date]
    # Sort the filtered projects by start date
    filtered_projects.sort(key=Project.get_start_date) # Ignore pycharm warning
    # Display each filtered project
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    """Get user to add a new project."""
    print("Let's add a new project")
    # Get project name from the user
    name = input("Name: ")
    try:
        # Get data from user
        start_date = datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))
    except ValueError:
        print("Invalid input. Please enter numbers in the correct format.")
        return
    # Create new project object and add it to the list
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)

def update_project(projects):
    """Allow the user to update the completion and/or priority of a selected project."""

    # Display projects with their index for selection
    for index, project in enumerate(projects):
        print(index, project)

    # Ask user which project to update
    try:
        choice_index = int(input("Project choice: "))
        selected_project = projects[choice_index]
        print(selected_project)
    except (ValueError, IndexError):
        print("Invalid project number. Please try again.")
        return  # exit function if invalid

    # Update completion if a new value is entered
    new_completion_input = input("New Percentage: ")
    while new_completion_input != "":
        try:
            selected_project.update_completion(int(new_completion_input))
            # If valid exit loop
            break
        except ValueError:
            new_completion_input = input("Invalid. Enter a number for completion: ")

    # Update priority if a new value is entered
    new_priority_input = input("New Priority: ")
    while new_priority_input != "":
        try:
            selected_project.update_priority(int(new_priority_input))
            # If valid exit loop
            break
        except ValueError:
            new_priority_input = input("Invalid. Enter a number for priority: ")


if __name__ == "__main__":
    main()
