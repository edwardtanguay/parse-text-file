import argparse
import os
import json
import re

class BlogEntry:
    def __init__(self, date, title, body):
        self.date = date
        self.title = title
        self.body = body

    def to_dict(self):
        return {
            "date": self.date,
            "title": self.title,
            "body": self.body
        }

class BlogParser:
    @staticmethod
    def parse_file(file_path):
        entries = []
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        entry_date, entry_title, entry_body = None, None, []
        date_pattern = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

        for line in lines:
            line = line.strip()

            if date_pattern.search(line) and ';' in line:  # Date and title line
                if entry_date and entry_title and entry_body:  # Save the previous entry
                    entries.append(BlogEntry(entry_date, entry_title, ' '.join(entry_body)))

                entry_date = date_pattern.search(line).group()
                entry_title = line.split(';', 1)[1].strip()
                entry_body = []

            elif line.startswith('---'):  # Separator lines
                continue

            else:  # Body lines
                entry_body.append(line)

        # Save the last entry
        if entry_date and entry_title and entry_body:
            entries.append(BlogEntry(entry_date, entry_title, ' '.join(entry_body)))

        return entries

    @staticmethod
    def write_to_json(entries, output_file):
        with open(output_file, 'w') as file:
            json.dump([entry.to_dict() for entry in entries], file, indent=4)

def main():
    parser = argparse.ArgumentParser(
        description="Parse a file into an array of tasks."
    )
    args = parser.parse_args()
    file_path = "./data.txt"

    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        print(lines)
    except Exception as e:
        print(f"Error reading the file: {e}")

if __name__ == "__main__":
    main()