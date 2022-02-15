import pandas as pd
from pandas import DataFrame


def make_data_frame(columns: list[str]) -> DataFrame:
    _structure = {}
    for column in columns:
        _structure[column] = []
    return pd.DataFrame(
        _structure,
        index=[],
    )