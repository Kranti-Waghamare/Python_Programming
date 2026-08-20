import os

def main():
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        print("Folder name is : ",FolderName)

        for subf in SubFolder:
            print("SubFolder name is : ",subf)

        for fname in FileName:
            print("FileName name is : ",fname)

if __name__ == "__main__":
    main()