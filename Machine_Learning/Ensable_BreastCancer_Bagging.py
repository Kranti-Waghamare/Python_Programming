import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


##############################################################
# Step 1 : Load the Dataset
##############################################################

df = pd.read_csv("breast_cancer.csv")

print("Shape of dataset : ",df.shape)

print("First few records : ")

print(df.head())

##############################################################
# Step 2 : Seperate features and labels
##############################################################

X = df.drop("target", axis = 1)
Y = df["target"]

print("X Shape : ", X.shape)
print("Y shape : ", Y.shape)

##############################################################
# Step 3 : split dataset from training and testing
#############################################################

X_train, X_test, Y_train, Y_test = train_test_split(
                                                        X,
                                                        Y, 
                                                        test_size= 0.2,
                                                        random_state= 42
                                                    )

#############################################################
# Step 4 : Scale the Feature
#############################################################

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

#############################################################
# Step 5.1 : Create the  Base model
#############################################################

base_model = DecisionTreeClassifier(random_state= 42)

#############################################################
# Step 5.2 : Create the Bagging model
#############################################################

model = BaggingClassifier(
    estimator= base_model, 
    n_estimators= 10,
    random_state= 42
)

#############################################################
# Step 6 : Train the Model 
#############################################################

model = model.fit(X_train, Y_train)

#############################################################
# Step 7 : Test the model
#############################################################

Y_Pred = model.predict(X_test)

#############################################################
# Step 8 : Evaluate the model 
#############################################################

print("Accuracy : ",accuracy_score(Y_test, Y_Pred))

print("Confusion Matrix : ")
print(confusion_matrix(Y_test, Y_Pred))

print("Classification Report : ")
print(classification_report(Y_test, Y_Pred))