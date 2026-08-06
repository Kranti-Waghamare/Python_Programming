def AreaCircle(Radius, PI):
    Area = PI * Radius * Radius
    return Area

def main():
    Ret = AreaCircle(Radius = 10.4, PI = 3.14)
    print("Area of circle is : ", Ret)

if __name__ == "__main__" :
    main()