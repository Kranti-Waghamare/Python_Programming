import os

def main():
    if os.path.exists("Demo.txt"):
        print("File Present in the current directory")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()