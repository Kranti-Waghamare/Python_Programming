#Accept : Multiple parameter
#Return : one value


def Marvellous(Value1, Value2):
    print("Inside main : ", Value1, Value2)
    return 21

def main():
    Ret = Marvellous(11, 51)
    print("Value of Ret is : ", Ret)

if __name__ == "__main__":
    main()