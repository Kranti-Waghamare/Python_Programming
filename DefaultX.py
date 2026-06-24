def Area (PI = 3.14, Radius):          #Error
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(10.3)

    print("Area of circle is : ", Ret)

    Ret = Area(13.5, 17.2)

    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()