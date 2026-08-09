def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("It is odd number")

def main():
    Value = int(input("Enter the number : "))

    CheckEven(Value)

if __name__ == "__main__":
    main()