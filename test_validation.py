import pandas as pd

df = pd.read_csv("heart.csv")

def test_missing_values():
    assert df.isnull().sum().sum() == 0

def test_target_column():
    assert "HeartDisease" in df.columns

def test_dataset_not_empty():
    assert len(df) > 0
