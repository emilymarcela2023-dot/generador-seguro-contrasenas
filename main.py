
# Generador de Contraseñas Seguras

import random
import string
from datetime import datetime

#  MENÚ PRINCIPAL

print("¡Bienvenido a FutureShield!")
print("Generador de contraseñas + Visión del futuro 2035\n")

while True:  # Este bucle mantiene el programa corriendo
    print("\n--- MENÚ ---")
    print("1. Generar una contraseña segura")
    print("2. Ver qué tan fuerte es una contraseña")
    print("3. Guardar una contraseña")
    print("4. Ver mis contraseñas guardadas")
    print("5. Ver el futuro 2035 (impacto de las tecnologías)")
    print("6. Salir del programa")
    
    opcion = input("\nElige una opción (1-6): ")
    
    # Opción 1: Generar contraseña
    if opcion == "1":
        print("\n--- Generar Contraseña ---")
        longitud = int(input("¿De cuántos caracteres? (recomendado 12-16): "))
        
        contrasena = ""
        contrasena += string.ascii_uppercase   # Mayúsculas
        contrasena += string.ascii_lowercase   # Minúsculas
        contrasena += string.digits            # Números
        contrasena += "!@#$%&_-"               # Símbolos
        
        password = ""
        for i in range(longitud):              # Bucle For (Unidad 3)
            password += random.choice(contrasena)
        
        print(f"\n Tu contraseña segura es: {password}")
    
    # Opción 2: Analizar fortaleza
    elif opcion == "2":
        print("\n--- Analizar Fortaleza ---")
        pw = input("Pega aquí la contraseña: ")
        
        if len(pw) >= 12:
            fuerza = "Fuerte"
        elif len(pw) >= 8:
            fuerza = "Media"
        else:
            fuerza = "Débil"
            
        print(f"La contraseña es: {fuerza}")
    
    # Opción 3: Guardar contraseña (simple)
    elif opcion == "3":
        print("\n--- Guardar Contraseña ---")
        sitio = input("¿Para qué sitio/web es? (ej: Gmail): ")
        password = input("Escribe la contraseña: ")
        
        with open("mis_contrasenas.txt", "a") as archivo:
            archivo.write(f"{sitio} | {password} | {datetime.now().strftime('%Y-%m-%d')}\n")
        print(" Guardado correctamente!")
    
    # Opción 4: Ver contraseñas
    elif opcion == "4":
        print("\n--- Mis Contraseñas Guardadas ---")
        try:
            with open("mis_contrasenas.txt", "r") as archivo:
                print(archivo.read())
        except:
            print("Todavía no has guardado ninguna contraseña.")
    
    # Opción 5: Simulador del futuro (parte más importante del proyecto)
    elif opcion == "5":
        print("\n" + "="*55)
        print("   SIMULADOR: EL IMPACTO DE LAS NUEVAS TECNOLOGÍAS")
        print("                    AÑO 2035")
        print("="*55)
        print("\nEscenario Optimista:")
        print("- La inteligencia artificial protege todas tus cuentas")
        print("- Casi no existen robos de contraseñas\n")
        print("Escenario Realista:")
        print("- Se usan huellas dactilares + reconocimiento facial")
        print("- Las contraseñas tradicionales casi desaparecen\n")
        print("Escenario Pesimista:")
        print("- La IA puede adivinar contraseñas muy rápido")
        print("- Es necesario usar autenticación biométrica")
        print("="*55)
    
    # Opción 6: Salir
    elif opcion == "6":
        print("\n¡Gracias por usar FutureShield! Hasta la próxima ")
        break
    
    else:
        print("\nOpción no válida. Por favor elige del 1 al 6.")
