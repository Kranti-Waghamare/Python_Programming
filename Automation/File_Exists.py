import os

def main():
    ret = os.path.exists("Demo.txt")

    if(ret == True):
        print("File Present in the current directory")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()