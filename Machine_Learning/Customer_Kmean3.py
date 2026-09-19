import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    ##############################################################
    # Step 1 : Load the dataset
    ##############################################################

    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset Loaded with values ")
    print(df.head())

    print("Missing values : ")
    print(df.isnull().sum())

    ##############################################################
    # Step 2 : Feature Selection
    ##############################################################

    X = df[["AnnualIncome", "SpendingScore"]]

    print("Selected features : ")

    print(X.head())

    ##############################################################
    # Step 3 : Scale the data
    ##############################################################

    Scalar = StandardScaler()

    X_Scaled = Scalar.fit_transform(X)

    print("Scaled data : ")
    print(X_Scaled[:5])


if __name__ == "__main__":
    main()