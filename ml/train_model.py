import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

def train_model() -> object:
    # Load data
    data = pd.read_csv("data/disease_outbreaks.csv")
    X = data.drop(columns=["outbreak_risk"])
    y = data["outbreak_risk"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    dump(model, "ml/outbreak_model.joblib")
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()
