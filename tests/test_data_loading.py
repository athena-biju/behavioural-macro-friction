from pathlib import Path

import pandas as pd


def test_sample_csv_loads():
    sample = Path(__file__).resolve().parents[1] / 'data' / 'sample_lfp.csv'
    df = pd.read_csv(sample)
    assert df.shape == (2, 3)
    assert list(df.columns) == ['country', 'year', 'female_lfp_rate']
