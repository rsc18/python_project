"""
Test module for raw_data_extractor
    1. Testing dataset is empty or not
    2. Dataset imported from alphavantage have column name 4. close in 3rd index
    3. Dataset is a timeseries
"""
# import sys
# import os
import datasets.raw_data_extractor as rde
import pandas as pd

# CURRENT_DIR = os.getcwd()
# PARENT_DIR = "/".join(CURRENT_DIR.split("/")[:-1])
# sys.path.append(PARENT_DIR)


def test_get_intraday_dataset():
    """
    Test:
    1. Testing dataset is empty or not
    2. Dataset imported from alphavantage have column name 4. close in 3rd index
    3. Dataset is a timeseries

    Returns
    -------
    None.

    """
    symbol = "LI"
    key = "2JVYQIAGV1ABJD0O"
    interval = "60min"
    dataset = pd.DataFrame(rde.get_intraday_dataset(symbol, interval, key))
    assert len(dataset) > 0
    assert dataset.columns[3] == "4. close"
    assert pd.core.dtypes.common.is_datetime_or_timedelta_dtype(dataset.index)
