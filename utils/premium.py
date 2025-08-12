import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def suggested_premium(model, x, loss_ratio, data):
    data['predicted_cost'] = model.predict(x)
    data['suggested_premium'] = (data['predicted_cost'] / loss_ratio).round(2)
    data['predicted_cost'].round(2)
    return data