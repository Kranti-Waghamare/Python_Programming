def Display(*Data):                  #Variable Number is shown by adding * in the parameter
    print(Data)
    print(type(Data))

def main():
    Display(11, 21.89, False, "Python")

if __name__ == "__main__":
    main()