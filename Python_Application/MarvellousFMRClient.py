from MarvellousLibrary import filterX, mapX, reduceX

CheckEven = lambda No : No % 2 == 0

Increment = lambda No : No + 1

Addition = lambda No1, No2 : No1 + No2


def main():
    Data = [12, 13, 8, 19, 22, 45, 66, 86]

    print("Input data is  : ",Data)

    FData = list(filterX(CheckEven, Data))

    print("Data after filter : " , FData)

    MData = list(mapX(Increment, FData))

    print("Data after map : ", MData)
    RData = reduceX(Addition, MData)

    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()