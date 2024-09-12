import os
import hashlib

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.hec', '.zip', '.rar', '.tgz', 
    '.tar.gz', '.run', '.bz2', '.gz', '.msi', '.rpm', '.deb', '.7z', 
    '.pdf', '.heif'
}

def calculate_hash(file_path, hash_algorithm=hashlib.md5):
    """Calculate the hash value of a file."""
    hash_obj = hash_algorithm()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read the file in 8KB chunks
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def find_duplicate_files(directory):
    """Find and list duplicate files in the specified directory and subdirectories, 
    skipping hidden directories and only processing allowed file types."""
    hash_dict = {}
    duplicates = []

    # Walk through all files in the directory and subdirectories
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Get the file extension
            _, extension = os.path.splitext(file_name)

            # Check if the file has an allowed extension and is not hidden
            if extension.lower() in ALLOWED_EXTENSIONS and not file_name.startswith('.'):
                # Check if the path is a file, not a directory
                if os.path.isfile(file_path):
                    file_hash = calculate_hash(file_path)

                    if file_hash in hash_dict:
                        # If the hash value already exists, mark this file as a duplicate
                        duplicates.append(file_path)
                    else:
                        # Store the hash value and file path
                        hash_dict[file_hash] = file_path
                else:
                    print(f"Skipping non-file path: {file_path}")
            else:
                print(f"Skipping file with unsupported extension or hidden file: {file_path}")

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
directory = '/home/diabetlum/D_Disk/'
duplicates = find_duplicate_files(directory)

if duplicates:
    print(f"Found duplicates: {duplicates}")
    delete_duplicates(duplicates)
else:
    print("No duplicates found.")
