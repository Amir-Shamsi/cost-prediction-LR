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

    def __init__(self, dataset_filename: str = ''):
        self._file_name = dataset_filename

    def predict(self):
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

        linearR.fit(x_train, y_train)

        linearR.score(x_test, y_test)

        y_predict = linearR.predict(x_test)

        math.sqrt(mean_squared_error(y_test, y_predict))
