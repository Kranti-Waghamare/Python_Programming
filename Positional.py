def Area(Radius, PI):
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(10.2, 3.14)

    print("Area of circle is : ",Ret)

    Ret = Area(13.6, 17.2)

    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()