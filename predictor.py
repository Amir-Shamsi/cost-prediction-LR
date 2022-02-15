from dataset.data_reader import InsuranceCostData
from cat_convertor import convert_to_category

data_set = InsuranceCostData(file_name='dataset/insurance.csv')
data_set = data_set.read_data()
convert_to_category(data_set, 'sex')
convert_to_category(data_set, 'smoker')
convert_to_category(data_set, 'region')
