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
            
            
def os_ram():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT os,
                            MAX(ram) as bateria_maxima,
                            MIN(ram) as bateria_minima,
                            AVG(ram) as ram_promedio
                     FROM smartphones
                     GROUP BY os
                     ORDER BY ram_promedio DESC"""
                    
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡RAM máxima, mínima y promedio por sistema operativo!")
        for os, ram_max, ram_min, ram_promedio in resultados:
            print(f"- {os}: RAM Máxima: {ram_max}GB, RAM Mínima: {ram_min}GB, RAM Promedio: {ram_promedio:.2f}GB")


def inventario_por_gama():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT
                            CASE
                                WHEN price > 18000 THEN 'Alta Gama'
                                WHEN price BETWEEN 10000 AND 18000 THEN 'Media Gama'
                                ELSE 'Baja Gama'
                            END as gama,
                            COUNT(*) as cantidad
                     FROM smartphones
                     GROUP BY gama"""
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Inventario por gama de precios!")
        for gama, cantidad in resultados:
            print(f"- {gama}: {cantidad} modelos")
            
            
def costo_beneficio():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT brand_name, price, spec_score FROM smartphones
                     WHERE spec_score > (SELECT AVG(spec_score) FROM smartphones) AND price < (SELECT AVG(price) FROM smartphones)
                     ORDER BY spec_score DESC
                     LIMIT 10"""
                     
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Costo-beneficio!")
        for marca, precio, puntuacion in resultados:
            print(f"- {marca}: ${precio:.2f} - Puntuación: {puntuacion}")
            
            
def precio_y_cantidad_camaras():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT AVG(price) as precio_promedio, rear_camera_count, AVG(vfm_score) as vfm_promedio
                     FROM smartphones
                     GROUP BY rear_camera_count
                     """
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Precio promedio y puntuación VFM por cantidad de cámaras traseras!")
        for precio_promedio, camaras, vfm_promedio in resultados:
            print(f"- {camaras} Cámara(s): ${precio_promedio:.2f} - VFM Promedio: {vfm_promedio:.2f}")
            
            
def usuarios_exigentes():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT brand_name, model, price, ram, has_5G FROM smartphones
                     WHERE brand_name IN ('apple', 'samsung') AND
                     ram >= 8 AND
                     has_5G = 1
                     ORDER BY price DESC
                     LIMIT 10"""
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Usuarios exigentes!")
        for marca, modelo, precio, ram, tiene_5G in resultados:
            print(f"- {marca} {modelo}: ${precio:.2f} - RAM: {ram}GB - 5G: {'Sí' if tiene_5G == 1 else 'No'}")
            
            
def monopolio_procesadores():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT processor_brand, COUNT(model) as cantidad
                     FROM smartphones
                     GROUP BY processor_brand
                     HAVING cantidad > 15
                     ORDER BY cantidad DESC"""
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Monopolio de procesadores!")
        for marca, cantidad in resultados:
            print(f"- {marca}: {cantidad} modelos")
            
            
def filtro_doble():
    with conn:
        cursor = conn.cursor()
        
        comando = """
                     SELECT brand_name, AVG(price) as precio_promedio FROM smartphones
                     WHERE has_5G = 1
                     GROUP BY brand_name
                     HAVING precio_promedio > 30000
                     ORDER BY precio_promedio DESC"""
                     
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print("¡Filtro doble: 5G y precio promedio por marca!")
        for marca, precio_promedio in resultados:
            print(f"- {marca}: Precio Promedio: ${precio_promedio:.2f}")

if __name__ == "__main__":
    #promocion()
    #publicidad_gamer_viajeros()
    #filtro_premiun()
    #modelos_celulares()
    #balance_celulares()
    #os_ram()
    #inventario_por_gama()
    #costo_beneficio()
    #precio_y_cantidad_camaras()
    #usuarios_exigentes()
    #monopolio_procesadores()
    filtro_doble()