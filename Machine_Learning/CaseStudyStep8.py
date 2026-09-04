import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*30

###############################################################
# Step 1 :  Load the dataset
###############################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print("Initial entries from dataset are : ")
print(df.head())


###############################################################
# Step 2 :  Exploratory Data Analysis (EDA)
###############################################################

print(Border)
print("Step 2 :  Exploratory Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)

print("Columns names : ",list(df.columns))

print("Missing values per column : ")
print(df.isnull().sum())

print("Class Distribution (Species count)")
print(df["species"].value_counts())

print("Stastical report of dataset : ")
print(df.describe())

###############################################################
# Step 3 :  Decide Independent and Dependent variable
###############################################################

print(Border)
print("Step 3 :  Decide Independent and Dependent variable")
print(Border)

# X = Independent Variables / Features
#Y = Dependent Variables / Lables

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]

Y = df["species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

###############################################################
# Step 4 :  Visualization of Dataset
###############################################################

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

#Scatter plot
plt.figure(figsize = (7, 5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("Marvellous Iris case study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

###############################################################
# Step 5 :  Split the dataset for training and testing
###############################################################

print(Border)
print("Step 5 :  Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 42)

print("Dataset spliting activity done")

print("X : ",X.shape)
print("Y : ",Y.shape)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)

print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test)

###############################################################
# Step 6 :  Build the model
###############################################################

print(Border)
print("Step 6 : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth = 5)

print("Model gets created successfully")

###############################################################
# Step 7 : Train the model
###############################################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train, Y_train)

print("Model trained successfully")

###############################################################
# Step 8 : Test the model
###############################################################

print(Border)
print("Step 8 : Test the model")
print(Border)

Y_Pred = model.predict(X_test)

print("Model testing done")

print("Expected answers : ")
print(Y_test)

print("Predicted answers : ")
print(Y_Pred)