def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets Opend")

        fobj.seek(10, 0)

        Data = fobj.read()

        print(Data)

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in the current directory")

if __name__ == "__main__":
    main()