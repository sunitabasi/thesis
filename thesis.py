# -*- coding: utf-8 -*-
"""thesis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i6_0xMfMxUBO1KcSEU5ehuZSmSuJJSRf
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

df = pd.read_csv("all rate.csv",index_col = 0)

df

df = pd.read_csv('all rate.csv')
df= df.iloc[0:10,1:7]
df

df.info()

df.describe()

# Convert DataFrame to NumPy array
numpy_array = df.values

print(numpy_array)

nepse_index = np.array(df['NEPSE (in points)'])
nepse_index

# # calculation correlation coefficeint and
# nepse_index = np.array(df['NEPSE (in points)'])
# inflation = np.array(df['Inflation (I)(in%)'])

# # Calculate sum of products, sum of squares, and sums
# sum_xy = np.sum(nepse_index * inflation)
# sum_x = np.sum(nepse_index)
# sum_y = np.sum(inflation)
# sum_x_squared = np.sum(nepse_index**2)
# sum_y_squared = np.sum(inflation**2)
# n = len(nepse_index)

# # Calculate correlation coefficient (R)
# R = (n * sum_xy - sum_x * sum_y) / (np.sqrt(n * sum_x_squared - sum_x**2) * np.sqrt(n * sum_y_squared - sum_y**2))

# print("Coefficient of Correlation (R):", R)

from scipy.stats import pearsonr

# NEPSE Index and Inflation data
nepse_index = np.array(df['NEPSE (in points)'])
inflation = np.array(df['Inflation (I)(in%)'])

# Calculate correlation coefficient (R) and p.e (r)
R, _ = pearsonr(nepse_index, inflation)
n = len(nepse_index)
PE_R = 0.6745 * ((1 - R**2) / np.sqrt(n))

print("Correlation Coefficient (R):", R)
print("Probable Error of Correlation (PE_R):", PE_R)

# Calculate 6 P.E.
six_PER = 6 * PE_R

# Determine significance
significance = "Significant" if abs(R) > six_PER else "Insignificant"
print("6P.E (R)=",six_PER )
print(significance)

# NEPSE Index and Interest rate
nepse_index = np.array(df['NEPSE (in points)'])
interest_rate = np.array(df['Interest Rate (IR) (in %)'])

# Calculate correlation coefficient (R) and p.e (r)
R, _ = pearsonr(nepse_index, interest_rate)
n = len(nepse_index)
PE_R = 0.6745 * ((1 - R**2) / np.sqrt(n))

print("Correlation Coefficient (R):", R)
print("Probable Error of Correlation (PE_R):", PE_R)

# Calculate 6 P.E.
six_PER = 6 * PE_R

# Determine significance
significance = "Significant" if abs(R) > six_PER else "Insignificant"
print("6P.E (R)=",six_PER )
print(significance)

# NEPSE Index and money supply
nepse_index = np.array(df['NEPSE (in points)'])
money_supply = np.array(df['Money Supply (MS) (in %)'])

# Calculate correlation coefficient (R) and p.e (r)
R, _ = pearsonr(nepse_index, money_supply)
n = len(nepse_index)
PE_R = 0.6745 * ((1 - R**2) / np.sqrt(n))

print("Correlation Coefficient (R):", R)
print("Probable Error of Correlation (PE_R):", PE_R)

# Calculate 6 P.E.
six_PER = 6 * PE_R

# Determine significance
significance = "Significant" if abs(R) > six_PER else "Insignificant"
print("6P.E (R)=",six_PER )
print(significance)

# NEPSE Index and GDP
nepse_index = np.array(df['NEPSE (in points)'])
gdp = np.array(df['GDP (in %)'])

# Calculate correlation coefficient (R) and p.e (r)
R, _ = pearsonr(nepse_index, gdp)
n = len(nepse_index)
PE_R = 0.6745 * ((1 - R**2) / np.sqrt(n))

print("Correlation Coefficient (R):", R)
print("Probable Error of Correlation (PE_R):", PE_R)

# Calculate 6 P.E.
six_PER = 6 * PE_R

# Determine significance
significance = "Significant" if abs(R) > six_PER else "Insignificant"
print("6P.E (R)=",six_PER )
print(significance)

from scipy import stats

# Calculate correlation coefficient
correlation_coefficient = df['NEPSE (in points)'].corr(df['Interest Rate (IR) (in %)'])

# Calculate R Square
r_square = correlation_coefficient ** 2

# Adjusted R Square (for simplicity, assuming only one predictor)
adjusted_r_square = 1 - (1 - r_square) * ((len(df) - 1) / (len(df) - 1 - 1))

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Interest Rate (IR) (in %)'], df['NEPSE (in points)'])

# Calculate Std. Error of Estimation
std_error_estimation = np.std(df['NEPSE (in points)'] - (intercept + slope * df['Interest Rate (IR) (in %)']))

# Display results
print("Correlation Coefficient (R):", correlation_coefficient)
print("R Square:", r_square)
print("Adjusted R Square:", adjusted_r_square)
print("Std. Error of Estimation:", std_error_estimation)
print("Slope (Coefficient for Interest Rate):", slope)
print("P value", p_value)
print("std error", std_err)

import statsmodels.api as sm

# Define the independent variable (Interest Rate) and add a constant term for the intercept
X = sm.add_constant(df['Interest Rate (IR) (in %)'])

# Define the dependent variable (NEPSE Index)
y = df['NEPSE (in points)']

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the summary of the regression model
summary = model.summary()

# Extract the intercept statistics
intercept_coef = model.params['const']
intercept_std_err = model.bse['const']
intercept_p_value = model.pvalues['const']

print("Intercept:", intercept_coef)
print("Standard Error of Intercept:", intercept_std_err)
print("P-value of Intercept:", intercept_p_value)

# regression between nepse and inflation
correlation_coefficient = df['NEPSE (in points)'].corr(df['Inflation (I)(in%)'])
r_square = correlation_coefficient ** 2
adjusted_r_square = 1 - (1 - r_square) * ((len(df) - 1) / (len(df) - 1 - 1))
# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Inflation (I)(in%)'], df['NEPSE (in points)'])
std_error_estimation = np.std(df['NEPSE (in points)'] - (intercept + slope * df['Inflation (I)(in%)']))
print("Correlation Coefficient (R):", correlation_coefficient)
print("R Square:", r_square)
print("Adjusted R Square:", adjusted_r_square)
print("Std. Error of Estimation:", std_error_estimation)
print("Slope (Coefficient for Interest Rate):", slope)
print("P value", p_value)
print("std error", std_err)

X = sm.add_constant(df['Inflation (I)(in%)'])
y = df['NEPSE (in points)']
# Fit the regression model
model = sm.OLS(y, X).fit()
# Get the summary of the regression model
summary = model.summary()
# Extract the intercept statistics
intercept_coef = model.params['const']
intercept_std_err = model.bse['const']
intercept_p_value = model.pvalues['const']

print("Intercept:", intercept_coef)
print("Standard Error of Intercept:", intercept_std_err)
print("P-value of Intercept:", intercept_p_value)

# regression between nepse and inflation
correlation_coefficient = df['NEPSE (in points)'].corr(df['Money Supply (MS) (in %)'])
r_square = correlation_coefficient ** 2
adjusted_r_square = 1 - (1 - r_square) * ((len(df) - 1) / (len(df) - 1 - 1))
# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Money Supply (MS) (in %)'], df['NEPSE (in points)'])
std_error_estimation = np.std(df['NEPSE (in points)'] - (intercept + slope * df['Money Supply (MS) (in %)']))
# y intercept
X = sm.add_constant(df['Money Supply (MS) (in %)'])
y = df['NEPSE (in points)']
# Fit the regression model
model = sm.OLS(y, X).fit()
# Get the summary of the regression model
summary = model.summary()
# Extract the intercept statistics
intercept_coef = model.params['const']
intercept_std_err = model.bse['const']
intercept_p_value = model.pvalues['const']
print("Correlation Coefficient (R):", correlation_coefficient)
print("R Square:", r_square)
print("Adjusted R Square:", adjusted_r_square)
print("Std. Error of Estimation:", std_error_estimation)
print("Slope (Coefficient for Interest Rate):", slope)
print("P value", p_value)
print("std error", std_err)
print("Intercept:", intercept_coef)
print("Standard Error of Intercept:", intercept_std_err)
print("P-value of Intercept:", intercept_p_value)

# regression between nepse and GDP
correlation_coefficient = df['NEPSE (in points)'].corr(df['GDP (in %)'])
r_square = correlation_coefficient ** 2
adjusted_r_square = 1 - (1 - r_square) * ((len(df) - 1) / (len(df) - 1 - 1))
# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df['GDP (in %)'], df['NEPSE (in points)'])
std_error_estimation = np.std(df['NEPSE (in points)'] - (intercept + slope * df['GDP (in %)']))
# y intercept
X = sm.add_constant(df['GDP (in %)'])
y = df['NEPSE (in points)']
# Fit the regression model
model = sm.OLS(y, X).fit()
# Get the summary of the regression model
summary = model.summary()
# Extract the intercept statistics
intercept_coef = model.params['const']
intercept_std_err = model.bse['const']
intercept_p_value = model.pvalues['const']
print("Correlation Coefficient (R):", correlation_coefficient)
print("R Square:", r_square)
print("Adjusted R Square:", adjusted_r_square)
print("Std. Error of Estimation:", std_error_estimation)
print("Slope (Coefficient for Interest Rate):", slope)
print("P value", p_value)
print("std error", std_err)
print("Intercept:", intercept_coef)
print("Standard Error of Intercept:", intercept_std_err)
print("P-value of Intercept:", intercept_p_value)

#for multiple regresion analysis

# Define the dependent variable (Y) and independent variables (X)
Y = df["NEPSE (in points)"]
X = df[["Interest Rate (IR) (in %)", "Inflation (I)(in%)", "Money Supply (MS) (in %)", "GDP (in %)"]]

# Add a constant to the independent variables matrix for the intercept term
X = sm.add_constant(X)

# Fit the multiple regression model
model = sm.OLS(Y, X).fit()

# Extract values
R_squared = model.rsquared
adj_R_squared = model.rsquared_adj
std_err_estimation = np.sqrt(model.mse_resid)
coefficients = model.params
std_errors = model.bse
significance = model.pvalues

# R is the square root of R_squared
R = np.sqrt(R_squared)

# Print the results
print(f"R: {R:.3f}")
print(f"R-Squared: {R_squared:.3f}")
print(f"Adjusted R-Squared: {adj_R_squared:.3f}")
print(f"Standard Error of Estimation: {std_err_estimation:.3f}\n")

print("Coefficients:.3f")
print(coefficients)

print("\nStandard Errors:")
print(std_errors)

print("\nSignificance (p-values):")
print(significance)

df = pd.read_csv('all rate.csv')

df

fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot NEPSE Index
ax1.set_xlabel('Year')
ax1.set_ylabel('NEPSE Index', color='tab:orange')
ax1.plot(df['Year'], df['NEPSE (in points)'], color='tab:orange', marker='s', label="NEPSE Index")
ax1.tick_params(axis='y', labelcolor='tab:orange')

# Create a second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('interest rate', color='tab:blue')
ax2.plot(df['Year'], df['Interest Rate (IR) (in %)'], color='tab:blue', marker='o', label='Interest rate')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Adding legends
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.title("Figure 1:Graphical representation NEPSE Index and interest rate")
plt.grid(True)
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot NEPSE Index
ax1.set_xlabel('Year')
ax1.set_ylabel('NEPSE Index', color='tab:orange')
ax1.plot(df['Year'], df['NEPSE (in points)'], color='tab:orange', marker='s', label="NEPSE Index")
ax1.tick_params(axis='y', labelcolor='tab:orange')

# Create a second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('inflation rate', color='b')
ax2.plot(df['Year'], df['Inflation (I)(in%)'], color='b', marker='o', label='Inflation rate')
ax2.tick_params(axis='y', labelcolor='b')

# Adding legends
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.4, 0.95))

plt.title("Figure 2:Graphical representation NEPSE Index and inflation rate")
plt.grid(True)
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot NEPSE Index
ax1.set_xlabel('Year')
ax1.set_ylabel('NEPSE Index', color='tab:orange')
ax1.plot(df['Year'], df['NEPSE (in points)'], color='tab:orange', marker='s', label="NEPSE Index")
ax1.tick_params(axis='y', labelcolor='tab:orange')

# Create a second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('MOney Supply', color='b')
ax2.plot(df['Year'], df['Money Supply (MS) (in %)'], color='b', marker='o', label='Money supply')
ax2.tick_params(axis='y', labelcolor='b')

# Adding legends
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.4, 0.95))

plt.title("Figure 3:Graphical representation NEPSE Index and Money supply")
plt.grid(True)
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot NEPSE Index
ax1.set_xlabel('Year')
ax1.set_ylabel('NEPSE Index', color='tab:orange')
ax1.plot(df['Year'], df['NEPSE (in points)'], color='tab:orange', marker='s', label="NEPSE Index")
ax1.tick_params(axis='y', labelcolor='tab:orange')

# Create a second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('GDP', color='b')
ax2.plot(df['Year'], df['GDP (in %)'], color='b', marker='o', label='GDP')
ax2.tick_params(axis='y', labelcolor='b')

# Adding legends
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95))

plt.title("Figure 4:Graphical representation NEPSE Index and Gross Domestic Product")
plt.grid(True)
plt.show()

