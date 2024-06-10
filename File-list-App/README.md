
# File List App

## Purpose

The File List App is designed to provide a simple command-line utility to list all files in a specified directory. This tool is particularly useful for quickly reviewing the contents of a folder without having to navigate through a file explorer. It also includes error handling to manage scenarios where the directory might not be found or access is denied.

## Features

- **Directory Listing:** Accepts a folder path as input and lists all files within that directory.
- **Error Handling:** Provides clear messages for cases where the folder is not found or permission is denied.

## Algorithm

The script follows these steps:

1. **Import the `os` Module:**
   - The `os` module is imported to interact with the operating system and perform directory operations.

2. **Define the `list_files_in_folder` Function:**
   - This function takes a folder path as input and attempts to list the files in that directory.
   - **Error Handling:** 
     - If the folder is not found, it returns an error message "File Not Found".
     - If there is a permission error, it returns an error message "Permission Denied".

3. **Main Function:**
   - Prompts the user to enter the folder path they want to list files for.
   - Calls the `list_files_in_folder` function with the provided folder path.
   - If files are found, it prints the list of files.
   - If an error occurs (e.g., folder not found or permission denied), it prints the appropriate error message.

## Usage

To use this script, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/File-List-App.git
   ```
2. **Navigate to the Project Directory:**
   ```sh
   cd File-List-App
   ```
3. **Run the Script:**
   ```sh
   python file_list.py
   ```
4. **Input the Folder Path:**
   - When prompted, enter the full path of the folder you want to list the files for.

## Example

```sh
$ python file_list.py
Insert the folderpath you are looking for: /path/to/your/folder
Files in folder /path/to/your/folder:
file1.txt
file2.txt
file3.txt
...
```

If the folder does not exist or you do not have permission to access it, you will see an appropriate error message:

```sh
Files not found in /path/to/your/folder: File Not Found
```

or

```sh
Files not found in /path/to/your/folder: Permission Denied
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
