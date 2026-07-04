def ChkEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkEven(Value)

    if(Ret == True):
        print("It is even")
    else:
        print("It is odd")

if __name__ == "__main__":
    main()