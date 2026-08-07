#Apartado de Funciones

def valorParqueadero (horas:int, valorHoras:int) -> int:
    try:
        subTotal= 0
        costoAdicional= 2000
        limiteHoraBase= 3

        if horas<=limiteHoraBase:
            subTotal= horas * valorHoras
        else:
            subTotal= (valorHoras * limiteHoraBase) + (horas - limiteHoraBase) * (valorHoras * costoAdicional)
            return subTotal
        
    except Exception as e:
        return e    

def calcularDescuento (horas: int, subTotal: int, estudiante: str)-> float:
    try:
        descuento= 0

        if horas >= 4 and estudiante == "N":
            descuento= subTotal * 0.3
        elif horas >= 4 and estudiante == "S":
            descuento= subTotal * 0.35
        else:
            descuento= 0

        return descuento 

    except Exception as e:
        return e

#Apartado Principal

try:
    #Datos de Entrada
    tipoVehiculo= ""
    cantidadHora= 0.0
    esEstudiante= ""

    #Datos Salida
    valorSubTotal= 0
    valorTotal= 0
    valorDescuento= 0
    valorIva= 0

    #Variables Adicionales

    valorParqueo= 0
    mensaje= ""

    # Proceso
    tipoVehiculo= input("(C: Carro | M: Moto | B: Bicicleta):"). upper()
    cantidadHora= int(input("Ingrese la cantidad de horas:"))
    esEstudiante= input("¿es usted estudiante?(S: Si | N: No):").upper()

    if cantidadHora <= 0:
        print("cantidad de horas invalidas")
        exit()
    if tipoVehiculo == "C": valorParqueo = 5000
    elif tipoVehiculo == "M": valorParqueo = 3000
    elif tipoVehiculo == "B": valorParqueo = 1000
    else:
        print(" Tipo de vehiculo invalido")
        exit()
        
    valorSubTotal= valorParqueadero (cantidadHora,valorParqueo)
    valorDescuento= calcularDescuento (cantidadHora,valorSubTotal,esEstudiante)
    valorIva= (valorSubTotal - valorDescuento ) * 0.19
    valorTotal= valorSubTotal - valorDescuento + valorIva

    tipoVehiculo= print(f"el tipo de vehiculo es {tipoVehiculo} ")
    valorSubTotal= print(f"El valor Subtotal es de ${valorSubTotal}")
    valorDescuento= print(f"el valor con descuento aplicado es de ${valorDescuento}")
    valorIva= print(f"el valor total con IVA aplicado es de ${valorIva}")
    valorTotal= print(f"el valor total del servicio de parqueadero es de ${valorTotal}")
except Exception as e:
 print(f"Error:{e}")