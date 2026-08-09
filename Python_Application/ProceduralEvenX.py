def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("It is even number")
    else:
        print("It is odd number")

if __name__ == "__main__":
    main()