def AreaCircle(Radius, PI):
    Area = PI * Radius * Radius
    return Area

def main():
    Ret = AreaCircle(10.4, 3.14)
    print("Area of circle is : ", Ret)

    Ret = AreaCircle(4.3, 7.12)
    print("Area of Circle is : ", Ret)

if __name__ == "__main__" :
    main()