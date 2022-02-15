import pandas as pd
from pandas import DataFrame


def make_data_frame(columns: list[str]) -> DataFrame:
    """
    :param columns: columns to make data frame
    :return: made data frame
    """
    _structure = {}
    for column in columns:
        _structure[column] = []
    return pd.DataFrame(
        _structure,
        index=[],
    )