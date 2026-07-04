def ChkEven(No):
    if(No % 2 == 0):
        print("It is even")
    else:
        print("It is odd")

def main():
    Value = int(input("Enter the number : "))

    ChkEven(Value)

if __name__ == "__main__":
    main()