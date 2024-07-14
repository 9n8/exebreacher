import os
import subprocess

def create_folder():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Define the new folder name
    new_folder = "decompiled_source"

    # Construct the path to the new folder
    new_folder_path = os.path.join(current_dir, new_folder)

    # Create the new folder
    try:
        os.makedirs(new_folder_path, exist_ok=True)
        print(f"Folder '{new_folder}' created successfully at: {new_folder_path}")
    except OSError as e:
        print(f"Error creating folder '{new_folder}': {e}")
        return None

    return new_folder_path

def decompile_pyc(pyc_file, output_dir):
    # Command to decompile .pyc using decompyle3
    command = f"decompyle3 \"{pyc_file}\" -o \"{output_dir}\""

    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error decompiling {pyc_file}: {e}")
        print(e.stderr)

def main():
    print("Drag the .pyc file into the console and press Enter:")
    pyc_file = input().strip()

    # Create new folder
    new_folder_path = create_folder()
    if not new_folder_path:
        return

    # Decompyle .pyc and output to new folder
    decompile_pyc(pyc_file, new_folder_path)

if __name__ == "__main__":
    main()
