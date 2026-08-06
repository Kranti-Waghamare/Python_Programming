#----------------------------------
#               List    Tuple
#----------------------------------
# Ordered       Yes      Yes
# Indexed       Yes      Yes
# Mutable       Yes      No
# Heterogeneous     Yes      Yes
#----------------------------------

def main():
    Data1 = (10, 11.8, True, "Python")
    Data2 = [10, 11.8, True, "Python"]

    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[0])

if __name__ == "__main__":
    main()