import pytest

from src.inference import load_model, predict


MODEL_PATH = "models/iris_classifier.joblib"


@pytest.fixture
def model():
    return load_model(MODEL_PATH)


def test_model_loads(model):
    assert model is not None


def test_valid_prediction(model):
    features = {
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2,
    }

    result = predict(model, features)

    assert "prediction" in result
    assert "probability" in result
    assert isinstance(result["prediction"], int)
    assert 0 <= result["probability"] <= 1


def test_missing_feature(model):
    features = {
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
    }

    with pytest.raises(ValueError):
        predict(model, features)


def test_extra_feature(model):
    features = {
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2,
        "extra": 10,
    }

    with pytest.raises(ValueError):
        predict(model, features)


def test_non_numeric_feature(model):
    features = {
        "sepal length (cm)": "five",
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2,
    }

    with pytest.raises(ValueError):
        predict(model, features)