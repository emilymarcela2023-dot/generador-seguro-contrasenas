#Menú

from funciones import *

# Bucle principal del menú (Unidad 3 - While)
while True:
    print("\n" + "="*55)
    print("       FUTURSHIELD - Generador de Contraseñas")
    print("       Impacto de las tecnologías en la seguridad")
    print("="*55)
    print("1. Generar nueva contraseña")
    print("2. Analizar fortaleza de una contraseña")
    print("3. Guardar contraseña")
    print("4. Ver contraseñas guardadas")
    print("5. Ver futuro 2035 (impacto de las tecnologías)")
    print("6. Salir del programa")
    print("="*55)
    
    opcion = input("\nElige una opción (1-6): ")
    
    if opcion == "1":           # Unidad 3 - Condicionales if
        contra = generar_contrasena()
        print(f"\nTu contraseña generada es: {contra}")
        
    elif opcion == "2":
        contra = input("\nEscribe la contraseña que quieres analizar: ")
        resultado = analizar_fortaleza(contra)
        print(f"La contraseña es: {resultado}")
        
    elif opcion == "3":
        contra = input("\nEscribe la contraseña: ")
        sitio = input("¿Para qué sitio o app es? (ej: Gmail, Netflix): ")
        guardar_contrasena(contra, sitio)
        
    elif opcion == "4":
        ver_contrasenas()
        
    elif opcion == "5":
        print("\n" + "="*60)
        print("     VISUALIZACIÓN DEL FUTURO 2035")
        print("="*60)
        print("En el futuro las contraseñas tradicionales pueden desaparecer.")
        print("La IA podrá adivinar contraseñas muy rápido.")
        print("Se usarán huellas dactilares, reconocimiento facial")
        print("y posiblemente chips en el cuerpo para mayor seguridad.")
        print("\nPor eso es importante usar contraseñas fuertes hoy.")
        print("="*60)
        
    elif opcion == "6":
        print("\n¡Gracias por usar FutureShield! Hasta la próxima 👋")
        break
        
    else:
        print("Opción incorrecta. Por favor elige del 1 al 6.")
