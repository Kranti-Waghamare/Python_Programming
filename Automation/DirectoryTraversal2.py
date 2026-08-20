import os

def main():
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        print("Folder name is : ",FolderName)

        for subf in SubFolder:
            print("SubFolder name is : ",subf)

if __name__ == "__main__":
    main()