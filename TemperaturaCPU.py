try:

    # Datos Entrada 
    tempCPUenGradosF = 0.0 #float

    # Datos Salida
    tempCPU = 0.0
    estadoCPU = "El estado de la CPU es:"

    # Proceso

    #1 Solicitar Datos
    tempCPUenGradosF= input("Ingrese la temperatura de la CPU:")

    #1.2 Conversion de Datos

    tempCPUenGradosF= float(tempCPUenGradosF)
    tempCPU= float(tempCPU)

    # Operaciones
    tempCPU= ((tempCPUenGradosF-32) * (5/9)) #float

    if tempCPU<45:
        print(f"La temperatura del CPU es: {tempCPU}°C")
        print(f" {estadoCPU} Optimo")
    elif 45.0<=tempCPU<=64.9:
        print(f"La temperatura del CPU es: {tempCPU}°C ")
        print(f"{estadoCPU} Precaución")
    elif 65.0<=tempCPU<=79.9:
        print(f"La temperatura del CPU es: {tempCPU}°C")
        print(f"{estadoCPU} Advertencia")
    elif 80<=tempCPU:
        print(f"La temperatura del CPU es: {tempCPU}°C")
        print(f"{estadoCPU} ALERTA CRITICA")
except Exception as e:
    print(f"Error del sistema:{e}")