def CheckEven(No):
    return (No % 2 == 0)

def main():
    Value = int(input("Enter the number : "))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("It is even number")
    else:
        print("It is odd number")

if __name__ == "__main__":
    main()