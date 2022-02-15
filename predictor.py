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
    _predict_data = None
    _data_reader = None

    def __init__(self, dataset_filename: str = ''):
        """
        Initial medical insurance cost predicting class
        for initial the parameter `dataset_filename`'s
        link can be given to it otherwise use default
        file name 'dataset/insurance.csv'.

        :param dataset_filename: file name of data set to extract and algo train;
        by that
        """
        if dataset_filename != '':
            self._file_name = dataset_filename
        self.__predict_init__()

    def _convert_type(self, data_set, *column_names):
        """
        Convert type of column to category to train algorithm by them.

        :param data_set: the dataset which contain the column names;
        :param column_names: column names to change the type;
        :return: None
        """
        for name in column_names:
            convert_to_category(data_set, name)

    def __predict_init__(self):
        """
        predict initial to make everything ready for the function
        `predict()`

        it will store some variable inside class vars such as:
            * _y_test
            * _x_test
            * _columns
            * _linear_regression
            * _predict_data
            * _data_reader

        :return: None
        """
        data_set = InsuranceCostData(file_name=self._file_name)
        self._data_reader = data_set
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
        """
        the main predict function which get the data line you want
        to predict cost for.

        :param file_name: file name of new data/ predict data
        :return: predicted cost of the medical insurance as type list[int]
        """
        new_data = InsuranceCostData(file_name=file_name)
        new_data = new_data.read_data()

        self._convert_type(new_data, 'sex', 'smoker', 'region')

        self._predict_data = new_data

        new_dum_data = pd.get_dummies(new_data)

        data_frame = dummies_data_frame(self._columns, new_dum_data)

        return self._linear_regression.predict(data_frame)

    def get_mean_squared_error(self):
        """
        to calculate the mean squared error
        :return: mean squared error as float
        """
        y_predict = self._linear_regression.predict(self._x_test)
        return math.sqrt(mean_squared_error(self._y_test, y_predict))

    def get_predict_data(self):
        """
        :return: return the predicted data line you given to `predict()`
        function
        """
        return self._predict_data

    def analyze(self, hue, *based_on):
        """
        :param hue:
        :param based_on:
        :return: None
        """
        self._data_reader.analyse(hue, based_on)

