import joblib
import pandas as pd

EXPECTED_FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]


def load_model(path: str):
    return joblib.load(path)


def predict(model, features: dict):
    if set(features.keys()) != set(EXPECTED_FEATURES):
        raise ValueError(
            f"Expected features: {EXPECTED_FEATURES}"
        )

    # Validate values are numeric
    if not all(isinstance(value, (int, float)) for value in features.values()):
        raise ValueError("All feature values must be numeric.")

    # Preserve the exact feature names and order used during training
    ordered_features = {
        name: features[name]
        for name in EXPECTED_FEATURES
    }

    input_data = pd.DataFrame([ordered_features])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0].max()

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }