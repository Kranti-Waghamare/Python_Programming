import pandas as pd
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
