"""
Estimated time: 45 minutes
Actual time: 39 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Load, process data, and display results."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def load_records(filename):
    """Read the file and return a list of records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Count champion wins and collect countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        country = record[1]
        champion = record[2]
        countries.add(country)
        # Add or update champion's win count
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1

    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Print champions and the associated countries."""
    print("Wimbledon Champions:")
    # Find the length of the longest champion name for alignment
    max_name_length = max(len(name) for name in champion_to_count)
    # Print champions
    for name, count in sorted(champion_to_count.items()):
        print(f"{name:{max_name_length}}  {count}")
    # Display the countries that have won Wimbledon
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()

