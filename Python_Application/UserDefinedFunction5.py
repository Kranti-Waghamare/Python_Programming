#Accept : Multiple parameter
#Return : multiple value


def Marvellous(Value1, Value2):
    print("Inside main : ", Value1, Value2)
    return 21, 101

def main():
    Ret1, Ret2 = Marvellous(11, 51)
    print("Value is : ", Ret1, Ret2)

if __name__ == "__main__":
    main()