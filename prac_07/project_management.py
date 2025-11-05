from project import Project
from datetime import datetime

FILENAME = "projects.txt"

MENU = """
    - (L)oad projects
    - (S)ave projects
    - (D)isplay projects
    - (F)ilter projects by date
    - (A)dd new project
    - (U)pdate project
    - (Q)uit"""

def main():
    projects = load_projects(FILENAME)
    choice = ""
    while choice != "q":
        print(MENU)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(projects, filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            pass
        elif choice == "a":
            pass
        elif choice == "u":
            pass
        elif choice == "q":
            # Add code to ask user to save file
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice. Please try again.")

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
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    # Filter projects starting on or after the specified date
    filtered_projects = [project for project in projects if project.get_start_date() >= filter_date]
    # Sort the filtered projects by start date
    filtered_projects.sort(key=Project.get_start_date)
    # Display each filtered project
    for project in filtered_projects:
        print(project)


if __name__ == "__main__":
    main()