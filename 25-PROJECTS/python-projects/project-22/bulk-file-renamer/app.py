import os

def bulk_rename_files(directory, prefix="", suffix="", replace_text=None, new_text=None, to_lowercase=False, to_uppercase=False):
    """
    Renames all files in the specified directory based on the given rules.

    :param directory: Path to the directory containing the files.
    :param prefix: Text to add at the beginning of each filename.
    :param suffix: Text to add at the end of each filename (before the extension).
    :param replace_text: Text to replace in the filename.
    :param new_text: New text to replace the `replace_text`.
    :param to_lowercase: Convert filename to lowercase.
    :param to_uppercase: Convert filename to uppercase.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print("No files found in the directory.")
        return

    print(f"Found {len(files)} files in '{directory}'.")

    # Rename each file
    for filename in files:
        # Split filename and extension
        name, ext = os.path.splitext(filename)

        # Apply renaming rules
        if replace_text and new_text:
            name = name.replace(replace_text, new_text)

        if to_lowercase:
            name = name.lower()
        elif to_uppercase:
            name = name.upper()

        new_name = f"{prefix}{name}{suffix}{ext}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # Rename the file
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        else:
            print(f"Skipped: {filename} (File with new name already exists)")

    print("Renaming completed!")


# Main program
if __name__ == "__main__":
    # Input directory path
    directory = input("Enter the directory path: ")

    # Input renaming options
    prefix = input("Enter prefix (leave blank for none): ")
    suffix = input("Enter suffix (leave blank for none): ")
    replace_text = input("Enter text to replace (leave blank for none): ")
    new_text = input("Enter new text (leave blank for none): ")
    to_lowercase = input("Convert filenames to lowercase? (y/n): ").lower() == "y"
    to_uppercase = input("Convert filenames to uppercase? (y/n): ").lower() == "y"

    # Call the bulk rename function
    bulk_rename_files(
        directory=directory,
        prefix=prefix,
        suffix=suffix,
        replace_text=replace_text if replace_text else None,
        new_text=new_text if new_text else None,
        to_lowercase=to_lowercase,
        to_uppercase=to_uppercase
    )