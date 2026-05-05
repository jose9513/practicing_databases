import pandas as pd
import sqlite3 as sql
import os

"""
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
"""


conn = sql.connect("practica_datos.db")
def promocion():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT brand_name, model FROM smartphones
                     WHERE has_5G = 1 AND price < 8000"""
        cursor.execute(comando)
        
        resultados = cursor.fetchall()
        print("¡Promoción de smartphones 5G por debajo de $5000!")
        for marca, modelo in resultados:
            print(f"- {marca} - {modelo}")
            
def publicidad_gamer_viajeros():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT brand_name, model FROM smartphones
                     ORDER BY "battery_capacity(mAh)" DESC
                     LIMIT 10"""
        cursor.execute(comando)
        
        resultados = cursor.fetchall()
        print("¡Top 10 smartphones con mayor batería para gamers y viajeros!")
        for marca, modelo in resultados:
            print(f"- {marca} - {modelo}")
            
def filtro_premiun():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT brand_name, model FROM smartphones
                     WHERE refresh_rate >= 120"""
        cursor.execute(comando)
        
        resultados = cursor.fetchall()
        print("¡Smartphones premium con tasa de refresco de 120Hz o más!")
        for marca, modelo in resultados:
            print(f"- {marca} - {modelo}")
            

def modelos_celulares():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT brand_name, COUNT(*) as num_modelos FROM smartphones
                     GROUP BY brand_name
                     HAVING COUNT(*) > 20
                     ORDER BY num_modelos DESC """
                    
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Marcas con más de 20 modelos en la base de datos!")
        for marca, num_modelos in resultados:
            print(f"- {marca}: {num_modelos} modelos")
            
            
def balance_celulares():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT AVG(price) as precio_promedio, AVG(spec_score) as promedio_spec_score FROM smartphones
                     GROUP BY spec_score
                     ORDER BY precio_promedio DESC"""
                     
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Balance de precios por puntuación de especificaciones!")
        for precio_promedio, promedio_spec_score in resultados:
            print(f"- Puntuación {promedio_spec_score}: ${precio_promedio:.2f}")

if __name__ == "__main__":
    #promocion()
    #publicidad_gamer_viajeros()
    #filtro_premiun()
    #modelos_celulares()
    balance_celulares()