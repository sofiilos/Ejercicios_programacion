try:

    # Datos Entrada
    caraDado=0

    # Datos Salida
    caraOpuestaDado=0

    # Variables Adicionales

    # Proceso

    caraDado = input("Ingrese el valor de la cara del Dado:")

    caraDado = int(caraDado)

    if caraDado ==1:
        print(f"La cara opuesta del dado es: 6")
    elif caraDado ==2:
        print(f"La cara opuesta del dado es: 5")
    elif caraDado ==3:
        print(f"La cara opuesta del dado es: 4")
    elif caraDado ==4:
        print(f"La cara opuesta del dado es: 3")
    elif caraDado ==5:
        print(f"La cara opuesta del dado es: 2")
    elif caraDado ==6:
        print(f"La cara opuesta del dado es: 1")
    else:
        print(f"Cara del dado invalida")
    
except Exception as e:
    print(f"Error del sistema:{e}")