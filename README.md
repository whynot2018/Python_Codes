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

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
