import math
import pandas as pd
from dataset.data_reader import InsuranceCostData
from sklearn.metrics import mean_squared_error
from cat_convertor import convert_to_category
from dataset.data_frame import dummies_data_frame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class InsuranceCostPredictor:
    _file_name = 'dataset/insurance.csv'
    _y_test = 0
    _x_test = 0
    _columns = None
    _linear_regression = None

    def __init__(self, dataset_filename: str = ''):
        if dataset_filename != '':
            self._file_name = dataset_filename
        self.__predict_init__()

    def _convert_type(self, data_set, *column_names):
        for name in column_names:
            convert_to_category(data_set, name)

    def __predict_init__(self):
        data_set = InsuranceCostData(file_name=self._file_name)
        data_set = data_set.read_data()

        self._convert_type(data_set, 'sex', 'smoker', 'region')

        dum_data = pd.get_dummies(data_set)

        x = dum_data.drop('charges', axis=1)
        y = dum_data['charges']

        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)

        linearR = LinearRegression()
        self._linear_regression = linearR

        linearR.fit(x_train, y_train)

        linearR.score(x_test, y_test)

        self._x_test = x_test
        self._y_test = y_test

        self._columns = dum_data.columns

    def predict(self, file_name: str):
    def get_mean_squared_error(self):
        y_predict = self._linear_regression.predict(self._x_test)
        return math.sqrt(mean_squared_error(self._y_test, y_predict))

