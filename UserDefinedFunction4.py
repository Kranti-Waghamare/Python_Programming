#Accept : Multiple Parameter
#Return : One Value

def Marvellous(Value1, Value2):
    print("Inside marvellous",Value1, Value2)
    return 21

def main():
    Ret = Marvellous(10, 20)
    print("Return value is ", Ret)

if __name__ == "__main__":
    main()