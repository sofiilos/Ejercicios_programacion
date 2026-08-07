#Apartado Funciones

def calcularTotalHoras (horaIngreso: int, horaSalida: int) -> int:
    try:

        totalHoras= abs(horaIngreso - horaSalida)

        return totalHoras
    
    except Exception as e:
        return e

def calcularParqueadero (totalHoras: int, valorParqueadero: int) -> int:
    try:

        subTotal= totalHoras * valorParqueadero

        return subTotal
    
    except Exception as e:
        return e

def clasificarHoras (horaIngreso: int , horaSalida: int) -> int:  #CORREGIR
    try:

        horasDiurnas= 0

        horasNocturnas= 0

        for hora in range (horaIngreso, horaSalida):
            if 5<=hora<=22:
                horaDiurna+= 1
            else:
                horaNocturna+= 1

        return horasDiurnas and horasNocturnas
    
    except Exception as e:
        return e

def calcularRecargoFinDeSemana (diaSemana: str , subtotalAntesDeAjustes: int) -> float:

    try:

        recargoFinDeSemana= 0

        if diaSemana== "S":
            recargoFindeSemana = subtotalAntesDeAjustes * 0.10
        elif diaSemana== "D":
            recargoFinDeSemana= subtotalAntesAjustes * 0.10
        else:
            recargoFinDeSemana= 0

        return recargoFinDeSemana

    except Exception as e:
        return e

def calcularDescuentoEstudiantil (esEstudiante: str , subtotalAntesDeAjustes: int) -> float:
    try:

        descuentoEstudiantil: 0

        if esEstudiante== "S":
            descuentoEstudiantil= subtotalAntesDeAjustes * 0.05
        else:
            descuentoEstudiantil: 0

        return descuentoEstudiantil
    except Exception as e:
        return e

#Apartado Principal

try:
    #Datos Entrada

    tipoVehiculo= ""
    horaIngreso= 0
    horaSalida= 0
    diaSemana= ""
    esEstudiante= ""

    #Datos Salida

    desgloseHorasConCosto= ""
    horasTotales= 0
    subtotalAntesAjustes= 0
    subtotalRecargoFinDeSemana= 0
    descuentoEstudiante= 0
    granTotal= 0

    #Variable 
    valorParqueadero= 0
    clasificacionHoras= ""
    subTotal= 0
    valorRecargoFinDeSemana= 0
    mensaje= ""
 

    #Proceso

    tipoVehiculo= input("Ingrese el tipo de Vehiculo (C: Carro | M: Moto | E: Electrico):").upper()
    horaIngreso= int(input("Ingrese la hora de ingreso (Formato 24 h):"))
    horaSalida= int(input("Ingrese la hora de salida (Formato 24 h):"))
    diaSemana= input("Ingrese el dia de la semana (L:Lunes | M:Martes | W:Miercoles | J:Jueves | V:Viernes | S:Sabado | D:Domingo):").upper()
    esEstudiantes= input("¿Es usted un estudiante? (S:Si | N:No):")

    if 6<=horasTotales<=22 and tipoVehiculo== "C": valorParqueadero= 5500
    elif 6<=horasTotales<=22 and tipoVehiculo== "M": valorParqueadero= 3500
    elif 6<=horasTotales<=22 and tipoVehiculo== "E": valorParqueadero=  4000
    elif 1<=horasTotales<=5 and 23<=horasTotales<=24 and tipoVehiculo== "C": valorParqueadero= 7000
    elif 1<=horasTotales<=5 and 23<=horasTotales<=24 and tipoVehiculo== "M": valorParqueadero= 4500
    elif 1<=horasTotales<=5 and 23<=horasTotales<=24 and tipoVehiculo== "E": valorParqueadero= 4000
    elif horasTotales==0:
        print("Horas Invalidas")
        exit()
    elif horasTotales>=24:
        print("Horas Invalidas")
        exit()
    else:
        exit()

        #Invocar Funciones

        totalHoras= calcularTotalHoras ( horaIngreso , horaSalida)
        subTotal= calcularParqueadero ( totalHoras, valorParqueadero) #no me covence
        desgloseHorasConCosto= clasificarHoras (totalHoras , horaSalida) #corregir
        subtotalAntesAjustes= ()
        valorRecargoFinDeSemana= calcularRecargoFinDeSemana (diaSemana , subtotalAntesAjustes)
        descuentoEstudiante= calcularRecargoFinDeSemana (esEstudiante , subtotalRecargoFinDeSemana)

        #Operaciones

        subtotalRecargoFinDeSemana= (valorRecargoFinDeSemana + subtotalAntesAjustes)
        granTotal= (subtotalRecargoFinDeSemana + descuentoEstudiante)

        #Imprimir todo

        tipoVehiculo= print(f"El tipo de Vehiculo es: {tipoVehiculo}")
        horasTotales= print(f"Las horas Totales en el parqueadero son:{totalHoras}")

except Exception as e:
    print(f"Error: {e}")