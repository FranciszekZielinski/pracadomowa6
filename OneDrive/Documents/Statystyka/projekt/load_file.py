import pandas as pd
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Load CSV files containing CO2 emissions, population, and GDP data')

# Add arguments for each CSV file
parser.add_argument('co2_file', type=str, help='CSV file containing CO2 emissions data')
parser.add_argument('population_file', type=str, help='CSV file containing population data')
parser.add_argument('gdp_file', type=str, help='CSV file containing GDP data')

# Parse the arguments
args = parser.parse_args()


gdp_file = args.gdp_file
population_file = args.population_file
CO2_file = args.co2_file




print("gdp_file:", gdp_file)
print("population_file:", population_file)
print("CO2_file:", CO2_file)