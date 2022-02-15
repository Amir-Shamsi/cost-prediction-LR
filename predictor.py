import math
import pandas as pd
from dataset.data_reader import InsuranceCostData
from sklearn.metrics import mean_squared_error
from cat_convertor import convert_to_category
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class InsuranceCostPredictor:
    _file_name = 'dataset/insurance.csv'
    _y_test = 0
    _x_test = 0
    _linear_regression = None
    _predicted = False

    def __init__(self, dataset_filename: str = ''):
        if dataset_filename != '':
            self._file_name = dataset_filename
        self.__predict_init__()

    def __predict_init__(self):
        data_set = InsuranceCostData(file_name=self._file_name)
        data_set = data_set.read_data()

        convert_to_category(data_set, 'sex')
        convert_to_category(data_set, 'smoker')
        convert_to_category(data_set, 'region')

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

        self._predicted = True
    def get_mean_squared_error(self):
        if self._predicted:
            y_predict = self._linear_regression.predict(self._x_test)
            return math.sqrt(mean_squared_error(self._y_test, y_predict))


