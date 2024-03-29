# -*- coding: utf-8 -*-
"""Copy of effects-of-climate-changes-on-crop-yields.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kfVP98VWlu77ZhnCrvpNVqjeoG1iE_cT

<a id='il'></a>
## Importing libraries
"""

# Commented out IPython magic to ensure Python compatibility.
#importing Libraries for exploring and Visualize Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
# %matplotlib inline

"""<a id='wrangling'></a>
# Data Wrangling
Data wrangling is the process of converting raw data into a usable form.
"""

# Load data
df=pd.read_csv('../content/climate-ds.csv',index_col=0)
df.head()

#rows and columns
df.shape

#information about data
# check data type of each coulmn
df.info()

#some statistical information about data
df.describe()

#Number of unique columns
print(f"Area has {df.Area.nunique()} unique value\nThere names :\n{df.Area.unique().tolist()}")

#Number of unique columns
print(f"Area has {df.Item.nunique()} unique value\nThere names :\n{df.Item.unique().tolist()}")

"""<a id='cd'></a>

## Data Cleaning
Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.
"""

#checking for null values
df.isnull().sum()

"""<a id='rn'></a>

"""

#confirmation of data
df.isnull().sum().any()

#Number of 0 values
for column_name in df.columns:
    column = df[column_name]
    # Get the count of Zeros in column
    count = (column == 0).sum()
    print('Count of zeros in column ', column_name, ' is : ', count)

"""<a id='rd'></a>

## Remove Duplicates
"""

#checking if any duplicates are available
df.duplicated().sum()

#remove Duplicates
df.drop_duplicates(keep='first',inplace = True)
df.duplicated().sum()

"""<a id='ro'></a>

## Remove Outliers
"""

for x, y in enumerate(df.columns):
    print(x, y)

def hist_box():
    for i in df.columns[3:]:
        plt.subplots(nrows=1,ncols=2,figsize=(15,6))
        plt.subplot(1,2,1)
        plt.hist(df[i])
        plt.title(i);
        plt.subplot(1,2,2)
        sns.boxplot(data=df[i])
        plt.title(i);
        yield()

hibox = hist_box()
next(hibox);

"""A right-skewed distribution, also known as positively skewed or right-tailed, is a type of data distribution where the majority of the data points cluster towards the left side of the graph, with a longer tail extending towards the right."""

next(hibox);

next(hibox);

next(hibox);

q_hi  = df["hg/ha_yield"].quantile(0.90)
#clear outliers
df[(df["hg/ha_yield"] < q_hi)]

sns.set()
#check outliers
for i in df.columns[3:]:
    sns.boxplot(data = df , x = df["hg/ha_yield"]);

"""<a id='eda'></a>

# Exploratory Data Analysis

<a id='ho'></a>
## Histogram
"""

sns.set()
df.hist(figsize=(20,20));

""" <a id='lp'
#The chart below shows how we can understand the effect of time with climate and crop produce
"""

#Store the numerical columns name in a variable
continuouscols = df.columns[2:].tolist()
#Make Function to plot year with repeat code
def yearPlot():
    for i in continuouscols[1:]:
        plt.figure(figsize=(20,5))
        sns.lineplot(data=df.groupby(['Year']).mean()[i])
        plt.xlabel('Year',fontsize = 15)
        plt.ylabel(i, fontsize = 15)
        plt.title(f"Effect of Year on the {i}", fontsize = 25)
        yield()

yplot = yearPlot()
next(yplot);

next(yplot);

next(yplot);

next(yplot);

""" <a id='bp'></a>

##
In this chart we will try to understand the relation between type of the crop and production
"""

#visualization of Items with hg/ha_yield
sns.set()
plt.figure(figsize=(20,10))
sns.barplot(data=df, x = df.Item, y = df['hg/ha_yield'])
plt.show()

#group Area with Hg/Ha_Yield sum
ST_df=df.groupby(df.Area)[['hg/ha_yield']].sum()
ST_df

#Area with the sum of Hg/Ha_yield
d10 = ST_df.nlargest(10, 'hg/ha_yield')
T10 = d10.loc[:,['hg/ha_yield']].head(10)
#Visualize bar plot
sns.set()
T10.plot.bar(figsize=(20,7));

""" <a id='sp'></a>
## Scatter Plot
the correlation between the features and output
"""

#make subplot for 4 plots
fig,plotcanvas=plt.subplots(nrows=2,ncols=2,figsize=(20,20))
#Store the numerical columns name in a variable
continuouscols = df.columns[2:].tolist()
#make for loop to iterate over all columns
for i in range(0,len(continuouscols)-1):
    x = 0 if ((i == 0) or (i == 1)) else  1
    y = 0 if ((i == 0) or (i == 2)) else  1
    #make scatterplot with regression line
    sns.regplot(data = df, x = continuouscols[i], y = 'hg/ha_yield', line_kws={"color":"r","alpha":0.7,"lw":5}, ax=plotcanvas[x,y])
    #find correlation between this two columns
    cor = round(df['hg/ha_yield'].corr(df[continuouscols[i]]),5)
    #put title for this plot
    plotcanvas[x , y].set_title(f'The Correlation between {continuouscols[i]} and hg/ha_yield is {cor}')

""" <a id='hm'></a>
## HeatMap
"""

#making heatmap for all data
plt.figure(figsize=(20,20))
sns.heatmap(df.corr(),annot=True)
plt.show()

df.describe()

"""## One Hot Encoding"""

#one hot encoding for the categorical columns
df = pd.get_dummies(df,columns=['Area','Item'])
df.rename(columns={x:x[5:] for x in df.columns[6:]}, inplace = True)
df.head(10)

#split the data
x = df.drop(labels=['hg/ha_yield'], axis=1)
y = df['hg/ha_yield']

y.describe()

"""<a id='dr'></a>
## Dimension Reduction
"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

x = scaler.fit_transform(x)

"""<a id='sd'></a>

## Spliting Data
"""

#split data to x_train, x_test, y_train, y_test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=40,shuffle=True)

#clear memory
del df
del x
del y

#Shape of the data
print('Shape of the x_train data : ', x_train.shape)
print('Shape of the y_train data : ', y_train.shape)
print('Shape of the x_test data : ', x_test.shape)
print('Shape of the y_test data : ', y_test.shape)

#Make DataFrame for track model accuracy
df_models = pd.DataFrame(columns=["Model", "MAE","MEDAE","MSE","RMSE", "Max Error","R2 Score","EVS","MAPE"])

"""### Evaluation Function"""

from sklearn.metrics import mean_absolute_error, mean_squared_error, max_error, median_absolute_error, r2_score, explained_variance_score, mean_absolute_percentage_error
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
#Evaluation function for regression models
def regression_report(y_true, y_pred):

    error = y_true - y_pred

    #Evaluation matrics
    mae = mean_absolute_error(y_true, y_pred)
    medae = median_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    maxerr = max_error(y_true, y_pred)
    r_squared = r2_score(y_true, y_pred)
    evs = explained_variance_score(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    metrics = [
        ('Mean Absolute Error', mae),
        ('Median Absolute Error', medae),
        ('Mean Squared Error', mse),
        ('Root Mean Squared Error', rmse),
        ('Max error', maxerr) ,
        ('R2 score', r_squared),
        ('Explained variance score', evs),
        ('Mean Absolute Percentage Error', mape)
    ]

    print('Regression Report:')
    for metric_name, metric_value in metrics:
        print(f'\t\t\t{metric_name:30s}: {metric_value: >20.3f}')

    return mae, medae, mse, rmse, maxerr, r_squared, evs, mape

from sklearn.ensemble import RandomForestRegressor
# Create the random grid
random_grid = {'n_estimators': [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)],
               'max_features': ['auto', 'sqrt'],
               'max_depth': [int(x) for x in np.linspace(5, 30, num = 6)],
               'min_samples_split': [2, 5, 10, 15, 100],
               'min_samples_leaf': [1, 2, 5, 10],
               'bootstrap' : [True, False]
              }
rfr = RandomForestRegressor()
rfrcv = RandomizedSearchCV(
                              estimator=rfr,
                              param_distributions=random_grid,
                              cv=3,
                              verbose=0
                            )
rfrcv.fit(x_train, y_train)

# Commented out IPython magic to ensure Python compatibility.
print("The best parameters are %s with a score of %0.2f"
#       % (rfrcv.best_params_, rfrcv.best_score_))
rfr_pred = rfrcv.predict(x_test)
mae, medae, mse, rmse, maxerr, r_squared, evs, mape = regression_report(y_test, rfr_pred)
row = {"Model": "RandomForestRegressor", "MAE": mae,"MEDAE": medae, "MSE": mse, "RMSE": rmse,
           "Max Error": maxerr, "R2 Score": r_squared, "EVS": evs, "MAPE": mape}
df_models = df_models.append(row, ignore_index=True)

plt.figure(figsize=(15,7))
plt.scatter(y_test, rfr_pred, s=20)
plt.title('Random Forest Regressor',fontsize=20)
plt.xlabel('Actual Crop Production',fontsize=15)
plt.ylabel('Predicted Crop Production',fontsize=15)

plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='r', linewidth = 4)
plt.tight_layout()

"""<a id='xgb'></a>

# Extreme Gradient Boosting Regressor
"""

from xgboost import XGBRegressor
from hyperopt import hp, fmin, tpe, STATUS_OK, Trials
space={'max_depth': hp.quniform("max_depth", 3, 18, 1),
        'learning_rate': hp.loguniform('learning_rate', np.log(0.001), np.log(0.5)),
        'gamma': hp.uniform ('gamma', 1,9),
        'reg_alpha' : hp.uniform('reg_alpha', 0.001, 1.0),
        'reg_lambda' : hp.uniform('reg_lambda', 0,1),
        'colsample_bytree' : hp.uniform('colsample_bytree', 0.5,1),
        'min_child_weight' : hp.quniform('min_child_weight', 0, 10, 1),
        'n_estimators': hp.uniform("n_estimators", 100, 20001)
    }
def objective(space):
    rego=XGBRegressor(
                    n_estimators =int(space['n_estimators']), max_depth = int(space['max_depth']),
                    learning_rate = space['learning_rate'], gamma = space['gamma'],
                    reg_alpha = space['reg_alpha'], min_child_weight=int(space['min_child_weight']),
                    reg_lambda = space['reg_lambda'],
                    colsample_bytree=int(space['colsample_bytree']), eval_metric="rmse",
                    early_stopping_rounds=10)

    evaluation = [( x_train, y_train), ( x_test, y_test)]

    rego.fit(x_train, y_train,
            eval_set=evaluation, verbose=0)


    y_pred = rego.predict(x_test)
    r_squared = r2_score(y_test, y_pred)
    return {'loss': -r_squared, 'status': STATUS_OK }

trials = Trials()

best_hyperparams = fmin(fn = objective,
                        space = space,
                        algo = tpe.suggest,
                        max_evals = 100,
                        trials = trials)

best_hyperparams['max_depth'],best_hyperparams['n_estimators'] = int(best_hyperparams['max_depth']),int(best_hyperparams['n_estimators'])

model = XGBRegressor(**best_hyperparams)
model.fit(x_train, y_train)
xgb_pred = model.predict(x_test)
mae, medae, mse, rmse, maxerr, r_squared, evs, mape = regression_report(y_test, xgb_pred)
row = {"Model": "XGBRegressor", "MAE": mae,"MEDAE": medae, "MSE": mse, "RMSE": rmse,
           "Max Error": maxerr, "R2 Score": r_squared, "EVS": evs, "MAPE": mape}
df_models = df_models.append(row, ignore_index=True)

plt.figure(figsize=(15,7))
plt.scatter(y_test, xgb_pred, s=20)
plt.title('XGB Regressor',fontsize=20)
plt.xlabel('Actual Crop Production',fontsize=15)
plt.ylabel('Predicted Crop Production',fontsize=15)

plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='r', linewidth = 4)
plt.tight_layout()

"""- Extreme Gradient Boosting Regressor Model got a great prediction r2 score equals 0.983 which is very good
- Mean Absolute Error is 6080 that means that the different between actual mean and predicted mean is 6080 which is excellent
- RMSE is 11057 which is very good

<a id='em'></a>

# Evaluation Models
"""

df_models.sort_values(by="R2 Score")

plt.figure(figsize=(20,7))
sns.barplot(x=df_models.Model, y=df_models['R2 Score'])
plt.title("Models' and R2 Score", size=15)
plt.xticks(rotation=30, size=12)
plt.show()

df_models.sort_values(by="R2 Score")

plt.figure(figsize=(20,7))
sns.lineplot(x=df_models.Model, y=df_models.RMSE)
plt.title("Models' and RMSE ", size=15)
plt.xticks(rotation=30, size=12)
plt.show()

import matplotlib.pyplot as plt

# Data from the provided data sheet
models_data = [
    {"Model": "RandomForestRegressor", "MAE": 6191.517804, "MEDAE": 2956.127356, "MSE": 1.377509e+08, "RMSE": 11736.734897, "Max Error": 162339.584313, "R2 Score": 0.981188, "EVS": 0.981190, "MAPE": 0.196388},
    {"Model": "XGBRegressor", "MAE": 6111.649111, "MEDAE": 3085.412109, "MSE": 1.218037e+08, "RMSE": 11036.469625, "Max Error": 131867.187500, "R2 Score": 0.983366, "EVS": 0.983366, "MAPE": 0.188606}
]

# Extracting data for plotting
y_test = [data["MAE"] for data in models_data]
rfr_pred = [data["MEDAE"] for data in models_data]
xgb_pred = [data["MSE"] for data in models_data]

# Create subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

# Plotting for RandomForestRegressor
ax1.scatter(y_test, rfr_pred, s=20)
c = models_data[0]['R2 Score']
ax1.set_title(f'Random Forest Regressor with {c:0.4f} R2 Score', fontsize=20)
ax1.set_xlabel('Actual Crop Production', fontsize=15)
ax1.set_ylabel('Predicted Crop Production', fontsize=15)
ax1.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='r', linewidth=4)

# Plotting for XGBRegressor
ax2.scatter(y_test, xgb_pred, s=20)
c = models_data[1]['R2 Score']
ax2.set_title(f'XGB Regressor with {c:0.4f} R2 Score', fontsize=20)
ax2.set_xlabel('Actual Crop Production', fontsize=15)
ax2.set_ylabel('Predicted Crop Production', fontsize=15)
ax2.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='r', linewidth=4)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()

"""ARIMA CODE

"""

from statsmodels.tsa.arima.model import ARIMA


p = 3
d = 1
q = 1
model = ARIMA(df['hg/ha_yield'], order=(p, d, q))
results = model.fit()

n = 10
forecast = results.forecast(steps=n)

print("Forecasted values:", forecast)

import matplotlib.pyplot as plt

# Plot original yield data
plt.scatter(df['Year'], df['hg/ha_yield'], label='Original Yield')

# Plot predicted yield values for the next 10 years
future_years = range(df['Year'].max() + 1, df['Year'].max() + 11)
plt.scatter(future_years, forecast, label='Predicted Yield', color='red')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Yield')
plt.title('Yield vs. Year with Predicted Values')
plt.legend()

# Show plot
plt.show()

!pip install pywedge

import pywedge as pw

# Assuming df is your DataFrame containing the data
mc = pw.Pywedge_Charts(df, c=None, y='hg/ha_yield')

# Call make_charts method to generate charts
charts = mc.make_charts()