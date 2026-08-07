try:

    #Datos de Entrada
    anio1=0
    anio2=0
    semanasBisiesto=0

    #Datos de salida
    cantidadSemanas=0

    #Variables Adicionales

    #Proceso

    #Paso #1: Solicitar los datos
    anio1=int(input("ingrese un año entre 1900 - 2019:"))
    anio2=int(input("ingrese el segundo año entre 1900 - 2019:"))
    semanasBisiesto=float(input("ingrese el dato de semanas (52|52.1):"))

    #Paso #1.2: Conversion de datos
    anio1=int(anio1)
    anio2=int(anio2)
    semanasBisiesto=float(semanasBisiesto)

    #Paso #2: Aspectos a controlar - validar que toda la informacion sea correcta
    if not (1900<=anio1<=2019 and 1900<=anio2<=2019):
        print("años invalidos")
        exit()

    #if semanasBisiesto==52 or semanasBisiesto==52.1:
    if semanasBisiesto not in [52,52.1]:
        print("Semanas Bisiesto invalido")
        exit()

    #Paso  #3: Operaciones
    cantidadSemanas= abs((anio1-anio2))*semanasBisiesto

    #Paso #4: Exponer Resultados
    print(f"La cantidad de semanas que hay entre el año {anio1} - {anio2} es:{cantidadSemanas}")

except Exception as e:
    print(f"Error del sistema:{e}")
