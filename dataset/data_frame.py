import pandas as pd
from pandas import DataFrame, Index


def dummies_data_frame(columns: Index, av_columns: DataFrame) -> DataFrame:
    """
    :param columns: columns to make data frame
    :param av_columns: columns that must be ignored
    :return: made data frame
    """
    _structure = {}
    for column in columns:
        if column == 'charges':
            continue
        if column not in av_columns.columns:
            _structure[column] = ['0']
        else:
            _structure[column] = av_columns[column]
    return pd.DataFrame(
        _structure,
        index=[0],
    )