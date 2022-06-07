import pandas as pd
import sys

try:
    dataframe = pd.read_csv(
        './InstanciasCandidatasParaExclusao.csv', sep=';',
        encoding='latin-1')  # It might be 'latin-1' or 'utf-8'

    # 1. Gerar e rodar este script para consultar se existem instâncias que não são free (1)
    result_temp = "select [Plan] as 'Plano', count(Id) as 'Quantidade de instâncias' from cash.global.ApplicationInstances where SubDomain='" + "' or SubDomain = '".join(
        dataframe['Instancia'])
    result_temp += "' group by [Plan]"

    # 2. Caso existam, gerar e rodar o script abaixo para ver quais são as instâncias (comentar o passo 1 e descomentar o passo 2.)
    # result_temp = "select Id, SubDomain, [Plan] from cash.global.ApplicationInstances where (SubDomain='" + "' or SubDomain = '".join(
    #     dataframe['Instancia'])
    # result_temp += "') and [Plan] != 1"
    result_file = open(r"free_verification_result.sql", "w")
    result_file.writelines(result_temp)
    print('The script was generated successfully.')
except:
    print('Something went wrong.')
    print("Error: " + sys.exc_info()[0])
