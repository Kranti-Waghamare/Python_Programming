import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Load the dataset
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("Values of Independent Variables : ", X)
    print("Values of Dependent Variables : ", Y)

    Sum_X = 0
    Sum_Y = 0

    for i in range(len(X)):
        Sum_X = Sum_X + X[i]
        Sum_Y = Sum_Y + Y[i]    

    mean_X = Sum_X / len(X)
    mean_Y = Sum_Y / len(Y)

    print("Mean_X is : ", mean_X)
    print("Mean_Y is : ", mean_Y)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()