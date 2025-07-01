import pandas as pd


def test_sample_csv_loads():
    df = pd.read_csv('data/sample.csv')
    assert df.shape == (2, 2)
