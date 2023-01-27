import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.svm import LinearSVR
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from data_cleaning import data_clean_for_price_range

def training_results(y_train, y_test, train_pred, test_pred) -> list:
    train_mse = mean_squared_error(y_train, train_pred)
    train_r2 = r2_score(y_train, train_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    test_r2 = r2_score(y_test, test_pred)
    return [train_mse, train_r2, test_mse, test_r2]

def return_frame(model_name : str, training_result : list) -> pd.DataFrame:
    result = pd.DataFrame([model_name, training_result[0], training_result[1], training_result[2], training_result[3]]).transpose()
    result.columns = ["Model name", "Training MSE", "Training R2", "Test MSE", "Test R2"]
    return result

def test_linear_regression(X_train, X_test, y_train, y_test) -> pd.DataFrame:
    model = LinearRegression()
    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    return return_frame("Linear regression", training_results(y_train, y_test, train_pred, test_pred))

def test_random_forest_regression(X_train, X_test, y_train, y_test) ->list:
    model = RandomForestRegressor(max_depth=2, random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("Random Forest regression", training_results(y_train, y_test, train_pred, test_pred))

def test_ridge(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = Ridge(random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("Ridge", training_results(y_train, y_test, train_pred, test_pred))

def test_SGD_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = SGDRegressor(random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("SGD regression", training_results(y_train, y_test, train_pred, test_pred))

def test_extra_tree_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = ExtraTreesRegressor(max_depth= 2, random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("Extra trees regression", training_results(y_train, y_test, train_pred, test_pred))

def test_gradient_boosting_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("Gradient boosting regression", training_results(y_train, y_test, train_pred, test_pred))

def test_K_Neighbors_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = KNeighborsRegressor()
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("K neighbors regression", training_results(y_train, y_test, train_pred, test_pred))

def test_MLP_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = MLPRegressor(random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("MLP regression", training_results(y_train, y_test, train_pred, test_pred))

def test_decision_tree_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("Decision tree regression", training_results(y_train, y_test, train_pred, test_pred))

def test_extra_tree_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = ExtraTreeRegressor(random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("Extra tree regression", training_results(y_train, y_test, train_pred, test_pred))

def test_linear_SVR_regression(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = LinearSVR(random_state=42)
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("Linear SVR regression", training_results(y_train, y_test, train_pred, test_pred))

def test_SVR(X_train, X_test, y_train, y_test) ->pd.DataFrame:
    model = SVR()
    model.fit(X_train, y_train) 
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test) 
    return return_frame("SVR", training_results(y_train, y_test, train_pred, test_pred))

def lunch_model_test():
    X, y = data_clean_for_price_range()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    linear_regression_result = test_linear_regression(X_train, X_test, y_train, y_test)
    random_forest_result = test_random_forest_regression(X_train, X_test, y_train, y_test)
    ridge_result = test_ridge(X_train, X_test, y_train, y_test)
    sgd_result = test_SGD_regression(X_train, X_test, y_train, y_test)
    extra_trees_result = test_extra_tree_regression(X_train, X_test, y_train, y_test)
    gradient_boosting_result = test_gradient_boosting_regression(X_train, X_test, y_train, y_test)
    k_neighbors_result = test_K_Neighbors_regression(X_train, X_test, y_train, y_test)
    mlp_result = test_MLP_regression(X_train, X_test, y_train, y_test)
    decision_tree_result = test_decision_tree_regression(X_train, X_test, y_train, y_test)
    extra_tree_result = test_extra_tree_regression(X_train, X_test, y_train, y_test)
    linear_svr_result = test_linear_SVR_regression(X_train, X_test, y_train, y_test)
    svr_result = test_SVR(X_train, X_test, y_train, y_test)
    
    result = pd.concat([linear_regression_result, random_forest_result, ridge_result, sgd_result,extra_trees_result,
                        gradient_boosting_result, k_neighbors_result, mlp_result,decision_tree_result, extra_tree_result,
                        linear_svr_result, svr_result])
    
    print(result)
    
