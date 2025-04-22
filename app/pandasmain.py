import utils 
import read_csv
import charts
import pandas as pd

def run():
    dateframe = pd.read_csv('data.csv')
    dateframe = dateframe[dateframe['Continent'] == 'Africa']

    countries = dateframe['Country'].values
    percentages = dateframe['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

