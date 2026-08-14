def main():
    Ans = 0

    try:
        print("Enter the first number : ")
        No1 = int(input())

        print("Enter the second number : ")
        No2 = int(input())

        Ans =  No1 / No2

        print("Division is successful")

    except ZeroDivisionError as zobj:

        print("Exception occur due to second operand is zero : ",zobj)

    except ValueError as vobj:

        print("Exception occur due to Invalid datatype : ",vobj)

    except Exception as eobj:

        print("Exception occured : ", eobj)

    print("Result is : ", Ans)

if __name__ == "__main__":
    main()