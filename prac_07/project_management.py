from project import Project
from datetime import datetime

FILENAME = "projects.txt"

def main():
    """Load projects from a file and return them in a list."""
    projects = []

    # Open the file for reading
    with open(FILENAME, "r") as in_file:
        # Skip the header line
        in_file.readline()

        # Loop through each line in the file
        for line in in_file:
            parts = line.strip().split()

            # Get each value from the list and convert it to the correct type
            name = parts[0]
            date_string = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])

            # Change the date from text to a date object
            start_date = datetime.strptime(date_string, "%d/%m/%Y").date()

            # Make a Project from the data and add it to the list
            project = Project(name, start_date, priority, cost_estimate, completion)
            projects.append(project)




