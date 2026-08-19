def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets Opend")

        print("File offset is : ", fobj.tell())

        Data = fobj.read()
        
        print(Data)

        print("File offset is : ", fobj.tell())
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in the current directory")

if __name__ == "__main__":
    main()