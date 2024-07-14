# https://www.datacamp.com/tutorial/introduction-fastapi-tutorial

import pycaret
from pycaret.datasets import get_data
from pycaret.regression import *
#from pydantic import v1 as pydantic_v1

data = get_data("insurance")
s = setup(data, target = 'charges')
best = compare_models()
create_api(best, 'insurance_prediction_model')

# need python3.11, and older pydantic
# pip uninstall pydantic
# pip install pydantic==1.10.13