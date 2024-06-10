import os

def list_files_in_folder(folderpath):
    try:
        files = os.listdir(folderpath)
        return files, None
    except FileNotFoundError:
        return None, "File Not Found"
    except PermissionError:
        return None, "Permission Denied"

def main():
    folderpaths = input("insert the folderpath you looking for:")
    
    for folderpath in folderpaths:
        files, error_message = list_files_in_folder(folderpath)
        if files:
             print(f'Files in folder {folderpath}')
             for file in files:
                 print(file)

        else:
            print(f'Files not found in {folderpath}:{error_message}')
    

if __name__ == "__main__":
    main()