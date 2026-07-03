def main():
    Marks = [78, 95, 60, 55, 37]

    for no in Marks:
        print(no)

        Marks[2] = 90
        print("-"*15)

    for no in Marks:
        print(no)

if __name__ == "__main__":
    main()