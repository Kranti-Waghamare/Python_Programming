def BigBazar():
    print("Inside the Big Bazar")

    def Amul():
        print("Inside the Amul Icecreame parlor")

def main():
    BigBazar()        #Allowed
    Amul()            #Not allowed / Error
    BigBazar.Amul()   #Not Allowed / Error

if __name__ == "__main__":
    main()