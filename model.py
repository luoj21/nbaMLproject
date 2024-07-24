import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_validate

''' Regression model used to predict NBA player salaries
using Random Forest Regression'''

class RegressionModel():

    def __init__(self, X, y):
        self.X = X
        self.y =  y.ravel()
        self.model = RandomForestRegressor(random_state=0,
                                           n_estimators=200,
                                           verbose=True)
    
    def split_train_predict(self, test_size: float):

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=test_size, random_state=42)

        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        return X_train, X_test, y_train, y_test, y_pred
    
    
    @staticmethod
    def get_accuracy(y_test, y_pred):

        print(f'### Test Accuracy ###: {r2_score(y_test, y_pred)}, ### MSE ###: {mean_squared_error(y_test, y_pred)}')

        residuals = y_test - y_pred
        plt.figure(figsize = [10,3])
        plt.title("Residual Plot")
        sns.regplot(x = y_pred, y = residuals, lowess=True, line_kws=dict(color="r"))
        plt.ylabel("Residuals")
        plt.xlabel("Predicted Values")


    def cross_val(self, n_splits: int):

        kf = KFold(n_splits=n_splits, shuffle=True)
        scoring=('r2', 'neg_mean_squared_error')
        cv_results = cross_validate(self.model, self.X, self.y, cv=kf, scoring=scoring, return_train_score=False)
        cv_results_df = pd.DataFrame(cv_results)
        cv_results_df['test_mean_squared_error'] = np.abs(cv_results_df['test_neg_mean_squared_error'])
        
        for i in range(0, n_splits):
            cv_results_df.loc[i, 'fold'] = i+1

        return cv_results_df
        