def Summation(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum
    
def main():
    Marks = [45, 56, 78, 89, 96, 43]

    Ret = Summation(Marks)
   
    print("Addition is : ", Ret)
    
if __name__ == "__main__":
    main()