from typing import Union

from pandas import DataFrame
from pandas.io.parsers import TextFileReader


def convert_to_category(data: Union[TextFileReader, DataFrame], index: str):
    """
    :param data: to convert type to category
    :param index: index of the data we want to change to category
    :return: dataframe
    """
    data[index] = data[index].astype('category')