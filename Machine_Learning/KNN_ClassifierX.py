import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    #Independent
    X = np.array([
        [1, 2],
        [2, 3],
        [3, 1],
        [5, 6]
    ])

    #Dependent
    Y = np.array(["Red", "Red", "Blue", "Blue"])

    new_Point = np.array([[3, 3]])

    print("Independent Variables are : ")
    print(X)

    print("Dependent Variables are : ")
    print(Y)

    print("Testing point is : ")
    print(new_Point)

if  __name__ == "__main__":
    main()