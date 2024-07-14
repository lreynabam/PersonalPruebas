import psycopg2
import pandas as pd
import os

def extract_company_buy_to_csv(output_file):
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'compras_c'),
            database=os.getenv('DB_NAME', 'postgres'),
            port=os.getenv('DB_PORT', '5432'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', '12345')
        )
        query = "SELECT * FROM company_buy"

        dataFrame = pd.read_sql_query(query, conn)
        dataFrame.to_csv(f'/app/output/{output_file}', index=False)
        conn.close()
        
        print(f"Los datos se han exportado correctamente a '{output_file}'.")
        
    except psycopg2.Error as e:
        print(f"Error al extraer datos: {e}")

extract_company_buy_to_csv('extracted_data.csv')
