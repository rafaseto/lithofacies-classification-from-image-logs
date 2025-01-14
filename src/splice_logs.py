import os
import pandas as pd
from utils.data_preprocessing import load_csv_files, create_df_subset, remove_nan_values, spliced_dfs_to_csv
import argparse

# Configurar os argumentos de linha de comando
parser = argparse.ArgumentParser(description="Splice the logs of a given curve")
parser.add_argument("variable_name", type=str, help="The name of the curve, e.g. RHOB.")
args = parser.parse_args()

# Substituir RHOB pelo nome da variável fornecida pelo usuário
variable_name = args.variable_name

base_path = os.path.join('..', 'data', 'dlis_preprocessed')
csv_data = load_csv_files(base_path)

# Criar um subconjunto do DataFrame baseado na variável fornecida
logs = create_df_subset(csv_data, [variable_name])

# Remover valores NaN
remove_nan_values(logs)

spliced_data = {}
for well, w_dict in logs.items():
    well_data = []

    for logical_file, lf_dict in w_dict.items():
        for frame, df in lf_dict.items():
            if variable_name in df.columns:
                well_data.append(df)

    try:
        df_concat = pd.concat(well_data).sort_values(by='TDEP', ascending=True)
    except Exception as e:
        print(f"Error when concatenating {well}: {e}")
        df_concat = None

    spliced_data[well] = df_concat

# Salvar os dados processados em CSV
output_path = os.path.join('..', 'data', 'dlis_spliced', variable_name)
spliced_dfs_to_csv(spliced_data, output_path)

print(f"Dados processados e salvos em {output_path}.")
