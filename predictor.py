from dataset.data_reader import InsuranceCostData
data_set = InsuranceCostData(file_name='dataset/insurance.csv')
data_set = data_set.read_data()
