from typing import Union

from pandas import DataFrame
from pandas.io.parsers import TextFileReader


def convert_to_category(data: Union[TextFileReader, DataFrame]) -> Union[TextFileReader, DataFrame]:
    """
    :param data: to convert type to category
    :return: dataframe
    """
    return data.astype('category')