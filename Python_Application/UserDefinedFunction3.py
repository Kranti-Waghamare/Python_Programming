#Accept : One parameter
#Return : one value


def Marvellous(Value):
    print("Inside main : ", Value)
    return 21

def main():
    Ret = Marvellous(11)
    print("Value of Ret is : ", Ret)

if __name__ == "__main__":
    main()