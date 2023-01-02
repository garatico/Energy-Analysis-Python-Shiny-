import os

# Library Imports
import pandas as pd  # Pandas
import numpy as np  # NumPy
from shiny import App, render, ui  # Shiny
import matplotlib.pyplot as plt  # MatPlotLib
from sklearn.linear_model import LinearRegression  # SciKit-Learn
from sklearn.preprocessing import PolynomialFeatures

# src File Imports
from src.wrangle import *
from src.nav_controls import *
from src.plot_controls import *

# Gets current working directory and reads the CSV file
pwd = os.getcwd()
data = pd.read_csv(pwd + "/data/wec.csv")
countries = list(data.country.unique())

# Defines Regression Models
lm = LinearRegression()
pm = PolynomialFeatures(degree=2, include_bias=False)

# Defines UI controls
app_ui = ui.page_navbar(
    # Operator * unpacks the argument out of a list
    *nav_controls(countries=countries),
    title="Energy Analysis")

# Defines server functionality
def server(input, output, session):
    # 1.) Line Plot
    plot_one_controls(input, output, render, data, wrangle=world_electricity_data, pd=pd, plt=plt)
    # 2.) Pie Chart
    #text_two_controls(input, output, render, data, wrangle=sawces_my_year_data)
    plot_two_controls(input, output, render, data, wrangle=sawces_my_year_data, plt=plt)
    # 3.) Regression Plot
    text_three_controls(input, output, render, data, wrangle=regression_country_data, np=np, lm=lm)
    plot_three_controls(input, output, render, data, wrangle=regression_country_data, np=np, lm=lm, pm=pm, plt=plt)
    
app = App(app_ui, server)
