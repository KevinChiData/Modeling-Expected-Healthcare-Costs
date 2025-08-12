from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# This function creates a machine learning model based on the data inputted.
# This was created to reduce clutter within the main notebook.
def ml_model(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    y_prediction = model.predict(x_test)
    print('R Squared:', model.score(x_test, y_test))
    print('r2_score', r2_score(y_test, y_prediction))
    print('mean_squared_error', mean_squared_error(y_test, y_prediction))
    print('mean_absolute_error', mean_absolute_error(y_test, y_prediction))
    return model