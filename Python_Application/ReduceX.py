from functools import reduce

def CheckEven(No):
    return(No % 2 == 0)

def Increment(No):
    return (No + 1)

def Addition(No1, No2):
    return (No1 + No2)


def main():
    Data = [12, 13, 8, 19, 22, 45, 66, 86]

    print("Input data is  : ",Data)

    FData = list(filter(CheckEven, Data))

    print("Data after filter : " , FData)

    MData = list(map(Increment, FData))

    print("Data after map : ", MData)

    RData = reduce(Addition, MData)

    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()