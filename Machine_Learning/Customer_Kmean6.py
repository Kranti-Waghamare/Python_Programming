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

    ##############################################################
    # Step 4 : Elbow method
    ##############################################################

    WCSS = []

    for k in range(1, 11):
        model = KMeans(
            n_clusters= k,
            random_state= 42,
            n_init= 10
        )

        model.fit(X_Scaled)

        WCSS.append(model.inertia_)

    print("Value of WCSS : ")

    for i in range(len(WCSS)):
        print(f"{i + 1} {WCSS[i]}")

    ##############################################################
    # Step 5 : Visualization
    ##############################################################

    plt.plot(range(1, 11), WCSS, marker = "o")
    plt.xlabel("Number of clusters : k")
    plt.ylabel("WCSS")
    plt.title("Marvellous Elbow Method")
    plt.grid(True)
    plt.show()

    ##############################################################
    # Step 6 : Final Model
    ##############################################################

    model = KMeans(
        n_clusters= 4, 
        random_state= 42,
        n_init= 10
    )

    Clusters = model.fit_predict(X_Scaled)

    df["Cluster"] = Clusters

    print("Dataset with clusters : ")
    print(df.head(100))


if __name__ == "__main__":
    main()