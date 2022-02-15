import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

class InsuranceCostData:
    _file_name = ''
    _data = None

    def __init__(self, file_name):
        """
        :param file_name: to read the data set file *** must be csv ***
        """
        self._file_name = file_name

    def read_data(self):
        """
        :return: the data set in form of pandas data frame.
        """
        self._data = pd.read_csv(self._file_name)
        self._data.head()
        return self._data

    def print_info(self):
        """
        will print the information of dataframe.
        :return: None
        """
        print(self._data.info)

    def print_shape(self):
        """
        print shape or row and columns of dataframe.
        :return:
        """
        print(self._data.shape)

    def analyse(self, hue, based_on):
        sb.set_style('ticks')
        sb.pairplot(self._data[based_on],
                    hue=hue,
                    height=3,
                    palette="Set1")
        plt.show()
