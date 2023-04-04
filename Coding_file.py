import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import os

# Input path globally for file.
input_path = os.getcwd() + "\\WorldBankClimateChange.csv"
countries_1 = ['United States', 'United Kingdom', 'Germany']
countries_2 = ['United States', 'United Kingdom', 'Germany', 'Belgium', 'Bolivia', 'Georgia', 'Libya']
countries_3 = ['United States', 'United Kingdom', 'Germany', 'Belgium', 'Bolivia']


def read_file(input_file):
    first_data_filtered = pd.read_csv(input_file, skiprows=4)
    first_data_filtered = first_data_filtered.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    first_data_filtered = first_data_filtered.dropna(how='all')
    first_data_filtered = first_data_filtered.set_index('Country Name')
    second_data_filtered = first_data_filtered.T

    return first_data_filtered, second_data_filtered


# two dataframes returning from function.
first_data_filtered, second_data_filtered = read_file(input_path)
print(first_data_filtered.loc[countries_1, '2014'].describe())

sns.boxplot(x='Country Name', y='2016', data=first_data_filtered.loc[countries_1].reset_index(), color="blue")
plot.ylabel('CO2 emissions per capita (metric tons)')
mng = plot.get_current_fig_manager()
mng.window.state('zoomed')
plot.show()


first_data_filtered.loc[countries_2, '2005':].plot()
plot.ylabel('CO2 emissions (metric tons per capita)')
mng = plot.get_current_fig_manager()
mng.window.state('zoomed')
plot.show()

sns.boxplot(x='Country Name', y='2007', data=first_data_filtered.loc[countries_3].reset_index(), color="blue")
first_data_filtered.loc[countries_3, '2007':].plot()
plot.ylabel('CO2 emissions (metric tons per capita)')
mng = plot.get_current_fig_manager()
mng.window.state('zoomed')
plot.show()