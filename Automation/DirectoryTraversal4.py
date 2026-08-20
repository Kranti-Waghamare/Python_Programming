import os

def main():
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        for fname in FileName:
            print("FileName name is : ",fname)

if __name__ == "__main__":
    main()