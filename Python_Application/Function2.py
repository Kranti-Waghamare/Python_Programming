def Addition(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Result = Addition(Value1, Value2)

    print("Addition is : ",Result)

if __name__ == "__main__":
    main()