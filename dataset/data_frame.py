import pandas as pd
from pandas import DataFrame, Index


def dummies_data_frame(columns: Index, av_columns: DataFrame) -> DataFrame:
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