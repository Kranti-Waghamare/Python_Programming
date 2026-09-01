from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Laod Iris dataset")
    print("-"*30)

    Dataset = load_iris()

    # Metadataset of the dataset
    print("Independent variable are : ")
    print(Dataset.feature_names)
    print("Length of Independent variables : ",len(Dataset.feature_names))

    print("Dependent variable ate : ") 
    print(Dataset.target_names)
    print("Length of Dependent variables : ",len(Dataset.target_names))

if __name__ == "__main__":
    main()