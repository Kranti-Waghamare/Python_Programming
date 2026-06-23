#Accept : Multiple Parameters
#Return : Multiple Values

def Mult(No1, No2):
    return No1 * No2

def Div(No1, No2):
    return No1 / No2

def main():
    Ret1 = Mult(10, 2)
    print("Multiplication is : ", Ret1)

    Ret2 = Div(15, 3)
    print("Division is : ", Ret2)


if __name__ == "__main__":
    main()