from predictor import InsuranceCostPredictor


icp = InsuranceCostPredictor('../../dataset/insurance.csv')
pred_cost = icp.predict(file_name='../../src/example/new_data.csv')

pred_data = icp.get_predict_data()
