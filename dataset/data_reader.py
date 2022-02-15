import pandas as pd

class InsuranceCostData:
    _file_name = ''
    _data = None

    def __init__(self, file_name):
        self._file_name = file_name

    def read_data(self):
        self._data = pd.read_csv(self._file_name)
        self._data.head()
        return self._data

    def print_info(self):
        print(self._data.info)

    def print_shape(self):
        print(self._data.shape)