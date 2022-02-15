from _colors import Mcolor
from predictor import InsuranceCostPredictor

icp = InsuranceCostPredictor('../../dataset/insurance.csv')
pred_cost = icp.predict(file_name='../../src/example/new_data.csv')

pred_data = icp.get_predict_data()

icp.analyze(hue='smoker', based_on=['age', 'bmi', 'smoker', 'charges'])

print('+--------------------------------------------------+')
print('|\t\t\t\tMade by Amir Shamsi\t\t\t\t   |')
""" 
    Github: https://github.com/Amir-Shamsi
    Linkedin: https://linkedin.com/in/amir-shamsi
"""

print('+--------------------------------------------------+')
print(Mcolor.HEADER + Mcolor.BOLD +
      'data for prediction:\n' + Mcolor.ENDC + Mcolor.OKCYAN
      , pred_data, Mcolor.ENDC)
print('+--------------------------------------------------+')
print(Mcolor.HEADER + 'predicted cost for this data is:', Mcolor.BOLD + Mcolor.OKGREEN + str(pred_cost[0]) + Mcolor.ENDC)
print('+--------------------------------------------------+')
