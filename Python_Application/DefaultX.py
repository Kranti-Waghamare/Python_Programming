def AreaCircle(PI = 3.14, Radius):            #Error because after default parameter compiler considered all parameters are default 
    Area = PI * Radius * Radius
    return Area

def main():
    Ret = AreaCircle(10.4)
    print("Area of circle is : ", Ret)

    Ret = AreaCircle(4.3, 7.12)
    print("Area of Circle is : ", Ret)

if __name__ == "__main__" :
    main()