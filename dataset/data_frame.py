import pandas as pd
from pandas import DataFrame, Index


def make_data_frame(columns: Index) -> DataFrame:
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