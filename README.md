# Predicting NBA Salaries

This project is aimed at attempting to predict an NBA player's annual salary based on various factors such as their career statistics. The data comes from players in the years 2002-2017. In this project, various machine learning algorithms were tested, namely multiple linear regression, lasso regression, ridge regression, and a regression random forest. While there are various external factors that can drastically influence how much a player gets paid, this project will use these algorithms to predict salaries as accuractely a possible subject to various constraints and assumptions on our data.

This entire project is done using Python and Jupyter Notebooks. Some libraries used include:
- Numpy
- Matplot Lib
- Seaborn
- Pandas
- SciKit Learn
- Dalex

#### Salary data set: https://www.kaggle.com/datasets/hultm28/nba-player-salary-data-2002-2017/data
#### Season data set: https://www.kaggle.com/code/koki25ando/nba-salary-prediction-using-multiple-regression/input

### Data Pre-Processing
Data pre-processing was needed in order to format both the seasonal data (contains statistics about a player's performance in a given season) and salary data (contains annual salary that season) into a compatible format. This is by far the biggest task to tackle as the resulting data set must contain matching/correct information about each player's performance, team, age, and salary for each given season. 

### Exploratory Data Analysis
EDA was done on the cleaned data set to explore how NBA statistics have changed over time as well as how salaries have changed over time. This can give us insights as to what types of players played from 2002-2017, what teams typically valued in players, and who were the top players during each season. EDA will also assist in determining which features to pick for our regression models through correlation analysis.

### Machine Learning 
As stated earlier, the three machine learning algorithms that were tested were  multiple linear regression, lasso regression, ridge regression, and a regression random forest. Out of all of these models, the regression random forest performed the best with a MSE of around 8 and a R2 of around 0.63. The primary reason for this is due to the powerful nature of a random forest in being to handle data without assuming linearity/nonlinearity in our data.

### Variable Importance
Variable importance allows us to determine which features had more weight in influencing our regression model's output. The idea behind variable importance is that a particular variable is considered "important" if permuting that variable causes the performance of the model to worsen extensively. For the regression random forest, age, rebounds per game, and points per game were the biggest contributors to a player's annual salary.

### Limitations
- Errors in raw data (For example, the salary data claimed Kevin Durant played for the Golden State Warriors from 2006-2007. He was in fact still in college at UT Austin)
- Lack of number of data points (Only about 4400 data points)
- Lack of salaries of some players
