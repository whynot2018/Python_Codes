import os
import re
import sys

def search_files(start_directory, pattern):
    """
    Recursively searches for files that match the regex pattern in the specified directory.
    :param start_directory: Directory where the search starts.
    :param pattern: Regex pattern to search for.
    :return: List of matched file paths.
    """
    matched_files = []
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Walk through directories
    for root, _, files in os.walk(start_directory):
        for file in files:
            if regex.search(file):  # If regex pattern matches the file name
                matched_files.append(os.path.join(root, file))
    
    return matched_files

def main():
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 3:
        print("Usage: python searcher.py <start_directory> <regex_pattern>")
        sys.exit(1)

    start_directory = sys.argv[1]
    pattern = sys.argv[2]

    # Check if the directory exists
    if not os.path.isdir(start_directory):
        print(f"Error: The directory {start_directory} does not exist.")
        sys.exit(1)

    # Search for files
    matched_files = search_files(start_directory, pattern)

    # Output the result
    if matched_files:
        print(f"Found {len(matched_files)} file(s):")
        for file in matched_files:
            print(file)
    else:
        print(f"No files matching pattern '{pattern}' found in directory {start_directory}.")

if __name__ == "__main__":
    main()
