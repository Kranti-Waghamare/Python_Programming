#############################################
# Deep Learning Pipeline
#############################################
# 1. Read the data from csv
# 2. Data Analysis (EDA)
# 3. Preprocessing
# 4. Train Test Split
# 5. Feature Scaling
# 6. FNN model Training
# 7. Model Evaluation
# 8. Graphical Representation
# 9. Model Preserve
# 10. Model Loading and Preserve
# 11. Test unseen Data
#############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#############################################
# Step 1 : Read the data from csv
#############################################
Border = "-"* 40

print(Border)
print("Step 1 : Read the data from csv")
print(Border)

data = pd.read_csv("placement_data.csv")

print("Complete Dataset : ")
print(data)

#############################################
# Step 2 : Data Analysis (EDA)
#############################################

print(Border)
print(" Step 2 : Data Analysis (EDA)")
print(Border)

print("First 5 rows : ")
print(data.head())

print("Columns names : ")
print(data.columns)

print("Shapes of dataset : ")
print(data.shape)

print("Statistical Summary : ")
print(data.describe())

#############################################
# Step 3 : Preprocessing
#############################################

print(Border)
print("Step 3 : Preprocessing")
print(Border)

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']

print("Input features : ")
print(X.head())

print("Target : ")
print(Y.head())

#############################################
# Step 4 : Train test split
#############################################

print(Border)
print("Step 4 : Train test split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.30, random_state= 42)

print("Training Input shape : ", X_train.shape)
print("Testing Input Shape : ", X_test.shape)
print("Training Output Shape : ", Y_train.shape)
print("Testin Output shape : ", Y_test.shape)

#############################################
# Step 5 : Feature Scaling
#############################################

print(Border)
print("Step 5 : Feature Scaling")
print(Border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print("Scaled training Data : ")
print(X_train_scaled[:5])

#############################################
# Step 6 : FNN Model Training
#############################################

print(Border)
print("Step 6 : FNN Model Training")
print(Border)

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter= 1000,
    random_state=42
)

print(model)

print("Train the model")

model.fit(X_train_scaled, Y_train)

print("Model Training completed")

#############################################
# step 7 : Model Evaluation
#############################################

print(Border)
print("step 7 : Model Evaluation")
print(Border)

Y_Pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test, Y_Pred)

print("Accuracy is : ", accuracy)

cm = confusion_matrix(Y_test, Y_Pred)

print("Confusion Matrix : ",cm)

print("Predict the probability : ")

Y_Prob = model.predict_proba(X_test_scaled)

print(Y_Prob[:5])

#############################################
# Step 8 : Graphical Representation
#############################################

print(Border)
print("Step 8 : Graphical Representation")
print(Border)

plt.plot(model.loss_curve_, color = 'blue')
plt.title("Model Training Loss over Time")
plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.grid(True)
plt.show()

print("Graphical Representation completed Successfully")

#############################################
# Step 9 : Model Preserve
#############################################

print(Border)
print("Step 9 : Model Preserve")
print(Border)

joblib.dump(model, "Placement_fnn_model.pkl")
joblib.dump(scalar, "Placement_scalar.pkl")

print("Model and scalar gets dump successfully")

#############################################
# Step 10 : Model Loading and preserving
#############################################

print(Border)
print("Step 10 : Model Loading and preserving")
print(Border)

loaded_model = joblib.load("Placement_fnn_model.pkl")
loaded_scalar = joblib.load("Placement_scalar.pkl")

print("Model gets loaded successfully")

#############################################
# Step 11 : Test unseen data
# Aptitude :           70
# Coding :             75
# Communication :      80
# Academics :          85
# Internship :         1
#############################################

new_student = pd.DataFrame([[70, 75, 80, 85, 1]], columns = ['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probability = loaded_model.predict_proba(new_student_scaled)

print("New Student Data : ")
print(new_student)

print("Prediction Probability : ", new_probability)

if new_prediction[0] == 1:
    print("Prediction : Placed")
else:
    print("Prediction : Not Placed")