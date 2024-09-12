import os

def list_file_types(directory):
    """Searches the directory recursively and lists all unique file types (extensions) once."""
    file_types = set()

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file_name in files:
            # Get the file extension
            _, extension = os.path.splitext(file_name)
            if extension:  # If there is an extension
                file_types.add(extension.lower())  # Add the extension to the set (converted to lowercase)

    # Return all unique file types
    return sorted(file_types)

# Example usage
directory = '/home/pettypavlow'
file_types = list_file_types(directory)

print(f"Found file types in {directory}:")
for file_type in file_types:
    print(file_type)
