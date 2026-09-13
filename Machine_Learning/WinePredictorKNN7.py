import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    Border = "-"*40

    #############################################################
    # Step 1 : Load the Dataset from CSV file
    #############################################################
    print(Border)
    print("Step 1 : Load the Dataset from CSV file")
    print(Border)

    df = pd.read_csv(DataPath)

    print(Border)
    print("Some entries from dataset : ")
    print(df.head())
    print(Border)

    #############################################################
    # Step 2 : Clean the Dataset
    #############################################################

    print(Border)
    print("Step 2 : Clean the Dataset")
    print(Border)

    df.dropna(inplace= True)

    print("Shape of dataset : ", df.shape)

    print("Total records : ", df.shape[0])
    print("Total columns : ", df.shape[1])

    print(Border)

    #############################################################
    # Step  3: Seperate Independent and Dependent variables
    #############################################################

    print(Border)
    print("Step  3: Seperate Independent and Dependent variables")
    print(Border)

    X = df.drop(columns= ['Class'])
    Y = df['Class']

    print("Shape of X : ", X.shape)
    print("Shpae of Y : ", Y.shape)

    print(Border)
    print("Input columns : ", df.columns.tolist())
    print("Output columns : class")
    print(Border)

    #############################################################
    # Step 4 : Split the dataset for training and testing
    #############################################################

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state= 42, stratify= Y)

    print(Border)
    print("Details of Training and tesing data")

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)

    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)

    print(Border)

    #############################################################
    # Step 5 : Feature scaling
    #############################################################

    print(Border)
    print("Step 5 : Feature scaling")
    print(Border)

    scalar = StandardScaler()
    X_train_Scaled = scalar.fit_transform(X_train)
    X_test_Scaled = scalar.fit_transform(X_test)

    print("Feature scaling done")

    print(Border)

    #############################################################
    # Step 6 : HyperParameter Tuning
    #############################################################

    print(Border)
    print("Step 6 : HyperParameter Tuning")
    print(Border)

    accuracy_scores = []
    K_Values = range(1, 21)

    for k in K_Values:
        model = KNeighborsClassifier(n_neighbors= k)
        model = model.fit(X_train_Scaled, Y_train)
        Y_Pred = model.predict(X_test_Scaled)
        accuracy = accuracy_score(Y_test, Y_Pred)
        accuracy_scores.append(accuracy)

    print("Accuray report : ")
    for no in accuracy_scores:
        print(no)

    print(Border)

    print(Border)
    print("Graphical representation")
    print(Border)

    plt.figure(figsize=(8, 5))
    plt.plot(K_Values, accuracy_scores, marker = 'o')
    plt.title("K values vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_Values))
    plt.show()

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()