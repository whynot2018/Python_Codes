import os
import hashlib

def calculate_hash(file_path, hash_algorithm=hashlib.md5):
    """Calculate the hash value of a file."""
    hash_obj = hash_algorithm()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read the file in 8KB chunks
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def find_duplicate_files(directory):
    """Find and list duplicate files in the specified directory and subdirectories."""
    hash_dict = {}
    duplicates = []

    # Walk through all files in the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_hash(file_path)

            if file_hash in hash_dict:
                # If the hash value already exists, mark this file as a duplicate
                duplicates.append(file_path)
            else:
                # Store the hash value and file path
                hash_dict[file_hash] = file_path

    return duplicates

def delete_duplicates(duplicate_files):
    """Delete the identified duplicate files."""
    for file_path in duplicate_files:
        try:
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        except OSError as e:
            print(f"Error deleting file {file_path}: {e}")

# Example usage
directory = '/home/whynot/StudioProjects/imgs'
duplicates = find_duplicate_files(directory)

if duplicates:
    print(f"Found duplicates: {duplicates}")
    delete_duplicates(duplicates)
else:
    print("No duplicates found.")
