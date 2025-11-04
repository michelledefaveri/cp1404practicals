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
    projects = load_projects(FILENAME)  # store returned projects
    choice = ""
    while choice != "q":
        print(MENU)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            pass
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            pass  # implement filter_projects_by_date later
        elif choice == "a":
            pass  # implement add_new_project later
        elif choice == "u":
            pass  # implement update_project later
        elif choice == "q":
            save = input("Would you like to save to {}? ".format(FILENAME)).lower()
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice. Please try again.")

def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)  # skip header
            for line in file:
                if line.strip() == "":
                    continue  # skip empty lines
                parts = line.strip().split("\t")  # tab-delimited
                name = parts[0]
                start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion = int(parts[4])
                project = Project(name, start_date, priority, cost_estimate, completion)
                projects.append(project)
        print("Loaded", len(projects), "projects from", filename)
    except FileNotFoundError:
        print(filename, "not found")
    return projects

def display_projects(projects):
    """ Display complete and incomplete projects."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    completed_projects = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(" ", project)

    print("Completed projects:")
    for project in completed_projects:
        print(" ", project)


if __name__ == "__main__":
    main()
