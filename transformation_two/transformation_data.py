import pandas as pd
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.dialects.postgresql import insert
#conexion
db_url = 'postgresql://user1:2468@postgres_db/transactions_db'
engine = create_engine(db_url)
metadata = MetaData()

input_file_path = '/data/extracted_data.csv'
df = pd.read_csv(input_file_path, parse_dates=['created_at', 'paid_at'])

# Cambio nombres de columnas
df.rename(columns={'name': 'company_name', 'paid_at': 'updated_at'}, inplace=True)
df['id'] = df['id'].astype(str)
df['company_id'] = df['company_id'].astype(str)
df['amount'] = df['amount'].astype(float)  
df['status'] = df['status'].astype(str)
df['company_name'] = df['company_name'].astype(str)

# Quito valores NaT por None
df['created_at'] = df['created_at'].where(df['created_at'].notnull(), None)
df['updated_at'] = df['updated_at'].where(df['updated_at'].notnull(), None)
df['created_at'] = df['created_at'].apply(lambda x: x if pd.notnull(x) else None)
df['updated_at'] = df['updated_at'].apply(lambda x: x if pd.notnull(x) else None)

companies_df = df[['company_id', 'company_name']].drop_duplicates(subset=['company_id'])
charges_df = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']]

def upsert_data(df, table_name, engine, key_columns):
    table = Table(table_name, metadata, autoload_with=engine)
    with engine.connect() as conn:
        for index, row in df.iterrows():
            insert_stmt = insert(table).values(row.to_dict())
            do_update_stmt = insert_stmt.on_conflict_do_update(
                index_elements=key_columns,
                set_={c.key: c for c in insert_stmt.excluded if c.key not in key_columns}
            )
            conn.execute(do_update_stmt)

upsert_data(companies_df, 'companies', engine, ['company_id'])
upsert_data(charges_df, 'charges', engine, ['id'])

print("Los datos se han cargado correctamente en la base de datos.")
