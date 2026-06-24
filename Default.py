def Area (Radius, PI = 3.14):
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(10.3)

    print("Area of circle is : ", Ret)

    Ret = Area(13.5, 17.2)

    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()