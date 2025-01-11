import argparse
import os

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