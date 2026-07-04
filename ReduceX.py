from functools import reduce

def ChkEven(No):
    return(No % 2 == 0)

def Increment(No):
    return No + 1

def Addition(No1, No2):
    return No1 + No2
         
def main():
    Data = [13, 12, 8, 11, 15, 10]

    print("Input Data is : ",Data)

    FData = list(filter(ChkEven, Data))

    print("Data after filter : ",FData)

    MData = list(map(Increment, FData))

    print("Data after map : ", MData)

    RData = reduce(Addition, MData)

    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()