def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream parlour")

def main():
    BigBazar()
    Amul()
    BigBazar.Amul()

if __name__ == "__main__":
    main()
