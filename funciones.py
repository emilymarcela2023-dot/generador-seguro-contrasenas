
# FUNCIONES.PY - Archivo con todas las funciones

import random
import string
import json
from datetime import datetime

# Función para generar contraseñas
def generar_contrasena():
    """Esta función genera una contraseña segura"""
    print("\n--- Generando contraseña segura ---")
    
    # Preguntamos la longitud
    longitud = int(input("¿De cuántos caracteres quieres la contraseña? (mínimo 8): "))
    
    # Creamos los caracteres posibles
    mayusculas = string.ascii_uppercase   # ABCDEFGH...
    minusculas = string.ascii_lowercase   # abcdefgh...
    numeros = string.digits               # 0123456789
    simbolos = "!@#$%^&*()_+-="
    
    # Unimos todo
    todos_caracteres = mayusculas + minusculas + numeros + simbolos
    
    # Generamos la contraseña
    contrasena = ""
    for i in range(longitud):           # Unidad 3 - Bucle For
        caracter = random.choice(todos_caracteres)
        contrasena = contrasena + caracter
    
    return contrasena


# Función para analizar si la contraseña es fuerte 
def analizar_fortaleza(contrasena):
    """Analiza si la contraseña es débil, media o fuerte"""
    if len(contrasena) >= 12:
        return "Fuerte "
    elif len(contrasena) >= 8:
        return "Media "
    else:
        return "Débil "


# Función para guardar contraseñas 
def guardar_contrasena(contrasena, sitio):
    """Guarda la contraseña en un archivo"""
    try:
        with open("contraseñas.json", "r") as archivo:
            lista = json.load(archivo)
    except:
        lista = []
    
    # Creamos un diccionario (Unidad 4)
    registro = {
        "sitio": sitio,
        "contrasena": contrasena,
        "fecha": datetime.now().strftime("%d/%m/%Y")
    }
    
    lista.append(registro)
    
    with open("contraseñas.json", "w") as archivo:
        json.dump(lista, archivo, indent=4)
    
    print(" Contraseña guardada correctamente")


# Función para ver las contraseñas guardadas
def ver_contrasenas():
    """Muestra todas las contraseñas guardadas"""
    try:
        with open("contraseñas.json", "r") as archivo:
            lista = json.load(archivo)
            print("\nContraseñas guardadas:")
            for item in lista:   # Bucle For
                print(f"Sitio: {item['sitio']} | Contraseña: {item['contrasena']} | Fecha: {item['fecha']}")
    except:
        print("Todavía no tienes contraseñas guardadas.")
