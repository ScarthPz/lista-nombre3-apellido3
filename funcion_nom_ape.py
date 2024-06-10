import os
os.system("cls")





from funcion_nom_ape import almacenar_datos 

# crear matriz, guarde 3 nombres y 3 apellidos - una lista para n y otra para a- sistema mostrar ordenado, almacenar archivo csv

personas = [["nombre", "apellido" ":"]]

for vueltas in range(3):
    nombres = input("Ingrese nombre: ")
    apellidos = input("Ingrese apellido: ")
    persona = [nombres,apellidos]
    personas.append(persona)


almacenar_datos(personas)