def ChkEven(No):
    return(No % 2 == 0)
         
def main():
    Data = [13, 12, 8, 11, 15, 10]

    print("Input Data is : ",Data)

    FData = list(filter(ChkEven, Data))

    print("Data after filter : ",FData)

if __name__ == "__main__":
    main()