import pandas as pd
import sqlite3
import os

def importar_csv_a_db(smartprix_smartphones_april_2026, datos_smartphones, smartphones):
    print(f"Leyendo el archivo {smartprix_smartphones_april_2026}...")
    
    # 1. Cargar los datos con Pandas (el Excel de los programadores)
    df = pd.read_csv(smartprix_smartphones_april_2026)
    
    # 2. Conectar (o crear) la base de datos SQLite
    conexion = sqlite3.connect(datos_smartphones)
    
    print(f"Insertando datos en la tabla '{smartphones}'...")
    
    # 3. La magia: pasar de DataFrame a SQL en una sola línea
    # 'if_exists=replace' crea la tabla si no existe o la sobreescribe
    df.to_sql(smartphones, conexion, if_exists='replace', index=False)
    
    conexion.close()
    print(f"¡Éxito! Ahora los datos viven en {datos_smartphones} dentro de la tabla '{smartphones}'.")

if __name__ == "__main__":
    # AJUSTA ESTOS TRES NOMBRES:
    archivo_csv = "smartprix_smartphones_april_2026.csv" # El nombre del archivo de Kaggle
    base_datos = "practica_datos.db"          # Como quieres que se llame tu DB
    tabla = "smartphones"             # El nombre de la tabla interna
    
    if os.path.exists(archivo_csv):
        importar_csv_a_db(archivo_csv, base_datos, tabla)
    else:
        print("Error: No encontré el archivo CSV. Asegúrate de que esté en la misma carpeta.")