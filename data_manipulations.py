import pandas as pd

country_table = pd.read_csv('staging_table_all_country_data.csv')
list_country = []

# Iteration over the staging table to manipulate and extract country details
for country in (country_table['Country']):
    if not (country in list_country):

        list_country.append(country)
        current_value = country_table[country_table['Country'] == country]

        # Write single country related all rows to one csv file
        df = pd.DataFrame(current_value)
        df.to_csv('Patients_{}.csv'.format(country))
