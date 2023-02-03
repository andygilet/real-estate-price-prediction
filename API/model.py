#from sklearn.linear_model import LinearRegression
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.linear_model import Ridge
#from sklearn.linear_model import SGDRegressor
#from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
#from sklearn.neighbors import KNeighborsRegressor
#from sklearn.neural_network import MLPRegressor
#from sklearn.tree import DecisionTreeRegressor
#from sklearn.tree import ExtraTreeRegressor
#from sklearn.svm import LinearSVR
#from sklearn.svm import SVR
import pickle

from data_cleaning import data_clean_for_price_range

def gradient_boosting_regression(X, y):
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X, y)
    return model

def model_to_file():
    X, y = data_clean_for_price_range()
    #model = test_linear_regression(X_train, X_test, y_train, y_test)
    #model = test_random_forest_regression(X_train, X_test, y_train, y_test)
    #model = test_ridge(X_train, X_test, y_train, y_test)
    #model = test_SGD_regression(X_train, X_test, y_train, y_test)
    #model = test_extra_tree_regression(X_train, X_test, y_train, y_test)
    model = gradient_boosting_regression(X, y)
    #model= test_K_Neighbors_regression(X_train, X_test, y_train, y_test)
    #model = test_MLP_regression(X_train, X_test, y_train, y_test)
    #model = test_decision_tree_regression(X_train, X_test, y_train, y_test)
    #model = test_extra_tree_regression(X_train, X_test, y_train, y_test)
    #model = test_linear_SVR_regression(X_train, X_test, y_train, y_test)
    #model = test_SVR(X_train, X_test, y_train, y_test)
    pickle.dump(model, open("API/model.pickle", "wb"))
    
model_to_file()