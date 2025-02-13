# Bulk File Renamer

## Description

This script allows you to bulk rename files in a specified folder with a specific extension. You can provide a new base name for the files and optionally add prefixes and suffixes to the new file names.

## Features

- Rename all files with a given extension in a specified folder.
- Customize the new base name for the files.
- Optionally add prefixes and suffixes to the new file names.
- Log the renaming process and handle errors gracefully.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository or download the script.**

2. **Run the script**:
   ```sh
   python bulk_rename_files.py
   ```

3. **Input the required data** when prompted:
   - Enter the file extension (e.g., .txt, .jpg): 
   - Enter the folder path: 
   - Enter the new base name for the files: 
   - Enter a prefix (optional): 
   - Enter a suffix (optional): 

4. **Example**:
   ```
   Enter the file extension (e.g., .txt, .jpg): .txt
   Enter the folder path: C:\Users\YourUsername\Documents\sample_files
   Enter the new base name for the files: document
   Enter a prefix (optional): old_
   Enter a suffix (optional): _archive
   ```

5. **The script will rename all files** in the specified folder with the specified extension, using the provided new base name, prefix, and suffix.

## Notes

- Ensure you have the necessary permissions to rename files in the specified folder.
- Use caution when running the script, as it will rename all matching files in the folder.
- Consider creating backups of your files before running the script.
