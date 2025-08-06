import os
import shutil

def specify_files():
    files = []
    print("enter the file path to back up(or (exit): ")
    while True:
        file_path = input("files: ")
        if file_path.lower() == "done":
            break
        if os.path.exists(file_path):
            files.append(file_path)
        else:
            print("files",file_path,"not found")
    return files

def backup_files(files,backup_location):
    if not os.path.exists(backup_location):
        os.makedirs(backup_location)

    for file in files:
        try:
            shutil.copy(file,backup_location)
            print("copied",file,"to",backup_location)
        except Exception as e:
            print("error copying",file,":",e)

def main():
    files = specify_files()
    if not files:
        print("No files specified for backup")
        return
    
    backup_location = input("enter the backup location: ")
    backup_files(files,backup_location)

if __name__ == "__main__":
    main()