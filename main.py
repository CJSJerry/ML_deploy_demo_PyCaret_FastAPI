# https://www.datacamp.com/tutorial/introduction-fastapi-tutorial

import pycaret
from pycaret.datasets import get_data
from pycaret.regression import *

data = get_data("insurance")
s = setup(data, target = 'charges')
best = compare_models()
create_api (best, 'insurance_prediction_model')

# need python3.11