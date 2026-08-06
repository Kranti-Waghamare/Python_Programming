def main():
    Marks = [45, 56, 78, 89, 96, 43]

    for no in Marks:
        print(no)

    Marks[2] = 99

    print("-" *15)

    for no in Marks:
        print(no)

if __name__ == "__main__":
    main()