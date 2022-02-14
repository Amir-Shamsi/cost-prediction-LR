import pandas as pd

class InsuranceCostData:
    _file_name = ''
    _data = None

    def __init__(self, file_name):
        self._file_name = file_name

    def read_data(self):
        data = pd.read_csv(self._file_name)