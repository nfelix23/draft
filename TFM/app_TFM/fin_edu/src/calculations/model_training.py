from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

def train_and_evaluate_models(data_encoded):
    school_datasets = {}
    for school in data_encoded['school'].unique():
        school_data = data_encoded[data_encoded['school'] == school]
        X = school_data.drop(['final_grade'], axis=1)
        y = school_data['final_grade']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        school_datasets[school] = (X_train, X_test, y_train, y_test)

    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Support Vector Regressor': SVR()
    }

    results = {}
    for school, datasets in school_datasets.items():
        X_train, X_test, y_train, y_test = datasets
        school_results = {}
        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            school_results[model_name] = mse
        results[school] = school_results

    return results
