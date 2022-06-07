import pandas as pd
import sys

try:
    instance_names = []
    dataframe = pd.read_csv(
        './InstanciasCandidatasParaExclusao.csv', sep=';',
        encoding='latin-1')  # It might be 'latin-1' or 'utf-8'
    result_file = open(r"result.sql", "w")
    for instance in dataframe['Instancia']:
        result_file.writelines("EXEC DropInstanceBySubdomain " + "'" +
                               instance + "'\n")
    print('The script was generated successfully.')
except:
    print('Something went wrong.')
    print("Error: " + sys.exc_info()[0])
