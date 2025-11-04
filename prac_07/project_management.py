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
    """Load projects from a file and return them in a list."""
    load_projects()
    print(MENU)


def load_projects():
    """Load projects from file."""
    projects = []
    try:
        with open(FILENAME, "r") as file:
            next(file)  # skip header
            for line in file:
                parts = line.strip().split("\t")
                name = parts[0]
                start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion = int(parts[4])
                project = Project(name, start_date, priority, cost_estimate, completion)
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {FILENAME}")
    except FileNotFoundError:
        print(f"{FILENAME} not found")
    return projects


if __name__ == main():
    main()




