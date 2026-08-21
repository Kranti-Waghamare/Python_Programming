import sys
import os

def DirectoryScanner(DirectoryPath):

    print("Files from the directory are : ")

    for FolderName, SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            print(fname)

def main():
    Border = "-"*45

    print(Border)
    print("------- Marvellous Automation Script -------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Automation script used to travel the directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python Filename.py DirectoryName")
            print("Directory name should be absolute path")

        else:
            DirectoryScanner(sys.argv[1])
            
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for information")

    print(Border)
    print("Thank you for using python automation script")
    print(Border)

if __name__ == "__main__":
    main()