import os

def bulk_rename_files(extension, folder_path, new_name, prefix="", suffix=""):
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith(extension)]
        if not files:
            print(f"No files with extension {extension} found in {folder_path}")
            return
        
        for index, filename in enumerate(files):
            new_file_name = f"{prefix}{new_name}_{index + 1}{suffix}{extension}"
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_file_name)
            os.rename(src, dst)
            print(f"Renamed {filename} to {new_file_name}")
        
        print(f"All {extension} files in {folder_path} have been renamed to {prefix}{new_name}_#{suffix}.{extension} format.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extension = input("Enter the file extension (e.g., .txt, .jpg): ")
    folder_path = input("Enter the folder path: ")
    new_name = input("Enter the new base name for the files: ")
    prefix = input("Enter a prefix (optional): ")
    suffix = input("Enter a suffix (optional): ")
    bulk_rename_files(extension, folder_path, new_name, prefix, suffix)
