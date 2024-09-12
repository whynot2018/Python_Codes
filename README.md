# Python Codes


 ## 1-) Duplicate File Finder and Remover

This Python script helps you find and remove duplicate files in a specified directory and its subdirectories. It identifies duplicates by calculating the hash of each file and comparing them. The script works only for specific file extensions and skips hidden directories and files.

### Features

- Identifies duplicate files based on their hash values.
- Skips hidden directories and files.
- Considers only specific file extensions:
  - `.jpg`, `.jpeg`, `.png`, `.gif`, `.hec`
  - `.zip`, `.rar`, `.tgz`, `.tar.gz`
  - `.run`, `.bz2`, `.gz`, `.msi`, `.rpm`, `.deb`, `.7z`
  - `.pdf`, `.heif`
- Deletes duplicate files after identifying them.

### Requirements

- Python 3.x
- `hashlib` (built-in Python library)
- `os` (built-in Python library)

### How It Works

1. The script walks through the specified directory and all its subdirectories.
2. It calculates the hash (MD5 by default) for each file with an allowed extension.
3. It compares the hash values to detect duplicates.
4. The script lists and deletes any duplicate files, keeping only one instance of each file.

### Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/faymaz/Python_Codes.git
   ```

2. Navigate to the cloned repository:

   ```bash
   cd duplicate-file-finder-and-remover
   ```

3. Edit the `directory` variable in the script to point to the folder where you want to search for duplicate files. For example:

   ```python
   directory = '/path/to/your/photo/directory'
   ```

4. Run the script:

   ```bash
   python remove_duplicates.py
   ```

   The script will:
   - Skip hidden directories and files.
   - Only process files with the allowed extensions.
   - Identify and remove duplicates.

### Example

If you want to search for duplicate images in `/home/user/photos/`, set the `directory` variable in the script like this:

```python
directory = '/home/user/photos'
```

Then, run the script. It will find all the duplicates in this folder and subfolders and delete them, keeping only one copy of each.

### File Extensions Considered

The script currently checks files with the following extensions:

- Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.hec`, `.heif`
- Archives: `.zip`, `.rar`, `.tgz`, `.tar.gz`, `.7z`
- Other: `.run`, `.bz2`, `.gz`, `.msi`, `.rpm`, `.deb`, `.pdf`

### Customizing the Script

You can customize the script to add more file types or change the behavior. For example:
- Add more extensions by updating the `ALLOWED_EXTENSIONS` set.
- Modify the hash algorithm used by changing `hashlib.md5` to `hashlib.sha256` (or another algorithm).



## 2-) File Type Lister

This Python script searches through a specified directory (and its subdirectories) and lists all unique file types based on their extensions, such as `.zip`, `.mp3`, `.txt`, `.doc`, etc. The script is useful for identifying what types of files are present in large directories.

### Features

- Recursively searches a directory and its subdirectories.
- Identifies and lists unique file types based on file extensions.
- Ignores case sensitivity in extensions (e.g., `.TXT` and `.txt` are considered the same).
- Outputs the list of file types in sorted order.

### Requirements

- Python 3.x
- `os` (built-in Python library)

### How It Works

1. The script traverses the directory and all its subdirectories.
2. It collects all file extensions and stores them in a set to ensure each type is listed only once.
3. The result is a sorted list of file extensions found in the directory.

### Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/pettypavlow/file-type-lister.git
   ```

2. Navigate to the cloned repository:

   ```bash
   cd file-type-lister
   ```

3. Edit the `directory` variable in the script to point to the folder you want to search. For example:

   ```python
   directory = '/path/to/your/directory'
   ```

4. Run the script:

   ```bash
   python list_file_types.py
   ```

   The script will list all unique file types (extensions) in the specified directory and its subdirectories.

## Example

If you want to search for unique file types in `/home/kerim`, set the `directory` variable like this:

```python
directory = '/home/pettypavlow'
```

Then run the script. The output might look like this:

```bash
Found file types in /home/pettypavlow:
/.doc
/jpeg
/jpg
/mp3
/pdf
/png
/zip
```

## Customizing the Script

You can customize the script by:
- Modifying the directory path to target specific directories.
- Adding functionality to skip certain file types or directories if needed.


### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
