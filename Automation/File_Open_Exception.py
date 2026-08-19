def main():
    try:
        open("Demo.txt","r")
        print("File gets opend")

    except FileNotFoundError as fobj:
        print("File is not found in the current directory")

if __name__ == "__main__":
    main()