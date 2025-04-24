import os

def bulk_rename(directory, prefix='', suffix='', new_extension=None):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("The directory does not exist.")
        return

    # Get the list of files in the directory
    files = os.listdir(directory)

    for file in files:
        # Get the full file path
        old_file = os.path.join(directory, file)

        # Check if it's a file (not a directory)
        if os.path.isfile(old_file):
            # Split the filename and extension
            filename, file_extension = os.path.splitext(file)

            # Build the new filename with prefix, suffix, and extension
            new_filename = f"{prefix}{filename}{suffix}"

            # If a new extension is specified, replace the old extension
            if new_extension:
                new_filename = f"{new_filename}{new_extension}"
            else:
                new_filename = f"{new_filename}{file_extension}"

            # Get the full new file path
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {file} -> {new_filename}")

def main():
    # Ask the user for the directory and renaming preferences
    directory = input("Enter the directory path: ")
    prefix = input("Enter the prefix (leave blank if none): ")
    suffix = input("Enter the suffix (leave blank if none): ")
    new_extension = input("Enter the new extension (leave blank if none): ")

    if new_extension:
        # Ensure the extension starts with a dot
        if not new_extension.startswith('.'):
            new_extension = '.' + new_extension

    # Call the bulk_rename function to rename the files
    bulk_rename(directory, prefix, suffix, new_extension)

if __name__ == '__main__':
    main()
