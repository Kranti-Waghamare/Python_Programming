def main():
    try:
        open("Demo.txt","w")
        print("File gets Opend")

    except FileNotFoundError as fobj:
        print("File is not found in the current directory")

if __name__ == "__main__":
    main()