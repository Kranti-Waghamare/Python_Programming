from Marvellous import Addition, Substraction

def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Result = Addition(Value1, Value2)           
  
    print("Addition is : ",Result)

    Result = Substraction(Value1, Value2)           
      
    print("Substraction is : ",Result)
    

if __name__ == "__main__":
    main()