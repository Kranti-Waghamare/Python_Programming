import sys

def main():
    print("----------------------------------------------------------")
    print("--------------- Marvellous Automation Script -------------")
    print("----------------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Automation script used to travel the directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python Filename.py DirectoryName")
            print("Directory name should be absolute path")

        else:
            DirectoryName = sys.argv[1]
            print("Directory name is : ", DirectoryName)

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for information")

    print("----------------------------------------------------------")
    print("------ Thank you for using python automation script ------")
    print("----------------------------------------------------------")

if __name__ == "__main__":
    main()