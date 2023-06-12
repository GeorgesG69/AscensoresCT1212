
'''  
Altura entre pisos= 3.5m
El número de piso viene dado por:
-sótanos: 3 pisos para todos
-Nro de Pisos superiores:

Edicaciones pisos>=30, hoteles
Edificaciones pisos<30, edificios residenciales 

George Galindez: 85

-Pisos de área de ocupación de 750m2

-Personas que ocupan pisos sótanos: 15/piso
-Personas que ocupan cada nivel superior 35/piso
'''

''' 
Este edificio cuenta con 85 plantas superiores y 3 sotanos, un total de 88 plantas.

La altura entre pisos es de 3.5m  

'''

import numpy
import openpyxl

wb = openpyxl.Workbook()

def main():

    '''
Datos Generales: 

B: Población Estimada

TVC: Tiempo de viaje completo

Ta: Tiempo adicional

TTV: Tiempo_Total_Viaje

    '''
    Poblacion_Piso = 35
    Poblacion_Sotano = 15
    
    Planta_Principal = 1
    Pisos_Superiores = 84
    Sotanos = 3 # (ni)
    Distancia_Promedio = 3.5 #m (ep)
    Pisos_No_Servidos = 0 # (ne)
    Pisos_Servidos = 30 #(ns)
    Pisos_Totales = Pisos_Servidos + Pisos_No_Servidos # (na)

    Nro_Ascensores = 5
    Capacidad_Nominal_P = 18
    Velocidad_Nominal_Establecida = 6 #m/s
    Zona_expresa = False

    print(f"Zona expresa: {Zona_expresa}")
    print(f"Pisos servidos: {Pisos_Servidos} \nPisos NO servidos: {Pisos_No_Servidos} \nPisos totales: {Pisos_Totales}")

    Poblacion_Total = Poblacion_Piso*Pisos_Servidos + Poblacion_Sotano*Sotanos # (B)
    
    Recorrido_Ppal_Super = Pisos_Totales*Distancia_Promedio #(Ha)
    Recorrido_Ppal_1PSuper = Pisos_No_Servidos*Distancia_Promedio #(He)
    Recorrido_Sotanos = Sotanos*Distancia_Promedio #(Hi)
    Recorrido_Superior_Servido = Recorrido_Ppal_Super - Recorrido_Ppal_1PSuper #(Hs)
    Recorrido_Total = Recorrido_Ppal_Super + Recorrido_Sotanos #(Ht)

    
    Personas_Viaje = int((3.2/Capacidad_Nominal_P)+(0.7*Capacidad_Nominal_P)+0.5) #Pv

    Paradas_Probables = Pisos_Servidos*(1-(((Pisos_Servidos-1)/Pisos_Servidos)**Personas_Viaje)) #np

    Aceleracion = 1 #m/s

    ReferenciaV_Nom = numpy.sqrt((Recorrido_Superior_Servido*Aceleracion)/Paradas_Probables)

    Tiempo_Apertira_cierre = 3.95 #s
    Tiempo_Entrada_Salida = 2 #s
    Tiempo_Adicional = 3/10

    if ReferenciaV_Nom < Velocidad_Nominal_Establecida and Zona_expresa == False:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/numpy.sqrt(Recorrido_Ppal_Super*Aceleracion/Paradas_Probables))+(Velocidad_Nominal_Establecida/Aceleracion)+(Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)+(Tiempo_Apertira_cierre*(Paradas_Probables+1))+Tiempo_Entrada_Salida*Personas_Viaje

    elif ReferenciaV_Nom >= Velocidad_Nominal_Establecida and Zona_expresa == False:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)+((Velocidad_Nominal_Establecida/Aceleracion)+Tiempo_Apertira_cierre)*(Paradas_Probables+1)+Tiempo_Entrada_Salida*Personas_Viaje

    elif ReferenciaV_Nom >= Velocidad_Nominal_Establecida and Zona_expresa == True:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)+((Velocidad_Nominal_Establecida/Aceleracion)+Tiempo_Apertira_cierre)*(Paradas_Probables+1)-(Recorrido_Superior_Servido/(Paradas_Probables*Velocidad_Nominal_Establecida))+Tiempo_Entrada_Salida*Personas_Viaje

    elif ReferenciaV_Nom < Velocidad_Nominal_Establecida and Zona_expresa == True:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)-(Recorrido_Superior_Servido/Velocidad_Nominal_Establecida)+(2*Velocidad_Nominal_Establecida/Aceleracion)+((2*Recorrido_Superior_Servido)/(Recorrido_Superior_Servido*Aceleracion/Paradas_Probables)**(1/Paradas_Probables))*(Paradas_Probables-1)+(Tiempo_Apertira_cierre*(Paradas_Probables+1))+Tiempo_Entrada_Salida*Personas_Viaje

    else:

        print("Valor errado para Tiempo de Viaje Completo.")


    Tiempo_Total_Viaje = Tiempo_Viaje_Completo + Tiempo_Viaje_Completo*Tiempo_Adicional


    Capacidad_Transporte = (300*Personas_Viaje*Nro_Ascensores*100)/(Tiempo_Total_Viaje*Poblacion_Total) # (C)
    Intervalo_Probable = Tiempo_Total_Viaje/Nro_Ascensores


    Tiempo_Llenado = 500/Capacidad_Transporte

    print(f"\nLa Vel. Nominal establecida es: {Velocidad_Nominal_Establecida} [m/s]")
    print(f"Referencial Vel. Nominal: {ReferenciaV_Nom}")
    print(f"\nRecorrido Superior: {Recorrido_Ppal_Super}")
    print(f"Recorrido Expreso: {Recorrido_Ppal_1PSuper}")
    print(f"Recorrido Superior Servido: {Recorrido_Superior_Servido} \n")

    print(f"Tiempo de apertura y cierre: {Tiempo_Apertira_cierre}")
    print(f"Tiempo de entrada y salida: {Tiempo_Entrada_Salida} \n")

    print(f"Tiempo de Viaje Completo: {Tiempo_Viaje_Completo} [s]")
    print(f"Tiempo Total de Viaje: {Tiempo_Total_Viaje} [s] \n")
    print(f"Personas por viaje: {Personas_Viaje}")
    print(f"Paradas probables: {Paradas_Probables} \n")
    print(f"Capacidad de Transporte [C] {Capacidad_Transporte} % (>12)")
    print(f"Intervalo Probable [I]: {Intervalo_Probable} [s] (<40) \n")
    print(f"Tiempo de llenado: {Tiempo_Llenado}")

    def Guardar_Calculo():

        #HojaCreada = wb.create_sheet("Cálculo", 0)

        Hoja = wb.active

        Hoja["A1"] = "Hola"

        wb.save("Prueba.xlsx")

        pass

    #Guardar_Calculo()

    
if __name__ == "__main__":
    print("Running... \n")
    main()
    