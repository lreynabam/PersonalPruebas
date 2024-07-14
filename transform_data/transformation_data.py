import pandas as pd
from datetime import datetime
import os
# Rutas en Docker
input_file_path = '/data/extracted_data.csv'
output_file_path = '/data/transformed_data.csv'

df = pd.read_csv(input_file_path)

# Renombro columnas
df.rename(columns={'name': 'company_name', 'paid_at': 'updated_at'}, inplace=True)

df['id'] = df['id'].astype(str)
df['company_name'] = df['company_name'].astype(str)
df['company_id'] = df['company_id'].astype(str)
def handle_large_numbers(value):
    try:
        num = float(value)
        if abs(num) >= 1e10000000000:  #if para valores muy grandres, para almacenarlos como cadena
            return str(value)
        return round(num, 2)
    except (ValueError, OverflowError):
        return str(value)

df['amount'] = df['amount'].apply(handle_large_numbers)
df['status'] = df['status'].astype(str)
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')

df.to_csv(output_file_path, index=False)

print(f"Los datos se han transformado y guardado en '{output_file_path}'.")
