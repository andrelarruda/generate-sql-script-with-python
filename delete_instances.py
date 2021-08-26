import pandas as pd
import sys

try:
    instance_names = []
    dataframe = pd.read_csv(
        'file_name.csv', sep=';', encoding='utf8')
    result_file = open(r"result.sql", "w")
    for instance in dataframe['column_name']:
        result_file.writelines(
            "EXEC DropInstanceBySubdomain " + "'" + instance + "'\n")
    print('The script was generated successfully.')
except:
    print('Something went wrong.')
    print("Error: " + sys.exc_info()[0])
