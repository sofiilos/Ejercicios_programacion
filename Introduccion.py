#Crear Variables

nombreUsuario = "" # Tipo str
edadUsuario = 0 # Tipo int
estaturaUsuario = 0.0 # Tipo float

# print(f"Tipo de Dato de la Variable edadUsuario: {type(edadUsuario)}")

# Solicitar Informacion
"""
Formula:
[Variable] = input([Mensaje])
"""

nombreUsuario = input("Ingrese su nombre:")
edadUsuario = input("Ingrese su edad:")
estaturaUsuario = float(input("Ingrese su estatura:")) #Conversion de Datos

# print(f"Tipo de Dato de la variable edadUsuario: {type(edadUsuario)}")

# Conversion de Datos
edadUsuario = int(edadUsuario)

# Instruccion para imprimir informacion por pantalla 
print (f"El nombre del Usuario es: {nombreUsuario}") 
print (f"La edad de {nombreUsuario} es {edadUsuario} años y su estatura es {estaturaUsuario} metros")

if edadUsuario>=18:
    print(f"Edad valida - Mayor de Edad")
else:
    print(f"Edad invalida - NO es mayor de edad")