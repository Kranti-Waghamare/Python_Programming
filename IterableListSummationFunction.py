def Summation(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no
    
    return Sum


def main():
    Marks = [78, 95, 60, 55, 37]

    Ret = Summation(Marks)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()