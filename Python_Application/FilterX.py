def CheckEven(No):
    return(No % 2 == 0)


def main():
    Data = [12, 13, 8, 19, 22, 45, 66, 86]

    print("Input data is  : ",Data)

    FData = list(filter(CheckEven, Data))

    print("Data after filter : " , FData)

if __name__ == "__main__":
    main()