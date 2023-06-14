
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
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import sys

filepath = "./datos_ascensores.xlsm"
de = pd.read_excel("datos_ascensores.xls")




def main(fila):

    Res_Grupo = de.iloc[fila,0]
    print(f"\n{Res_Grupo}\n")

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
    Pisos_Superiores = 85
    Sotanos = 3 # (ni)
    Distancia_Promedio = 3.5 #m (ep)
    Distancia_Promedio_Par = 7 # (ean)
    Distancia_Promedio_Impar = 7 # (eap)
    Pisos_No_Servidos = float(de.iloc[fila,3]) # (ne)
    Pisos_Servidos = float(de.iloc[fila,2]) #(ns)
    Pisos_Totales = Pisos_Servidos + Pisos_No_Servidos # (na)

    Nro_Ascensores = float(de.iloc[fila,4])
    Tamano_Puerta = 800
    Capacidad_Nominal_P = float(de.iloc[fila,5])
    Velocidad_Nominal_Establecida = float(de.iloc[fila, 6]) #m/s
    Tiempo_Apertira_cierre = float(de.iloc[fila,7]) #s
    Tiempo_Entrada_Salida = float(de.iloc[fila, 8]) #s
    Tiempo_Adicional = 3/10
    #Zona expresa
    if de.iloc[fila,1] == "si":

        Zona_expresa = True
    
    elif de.iloc[fila,1] == "no":

        Zona_expresa = False


    Paridad = ""

    #print(f"Zona expresa: {Zona_expresa}")
    print(f"Pisos servidos: {Pisos_Servidos} \nPisos NO servidos: {Pisos_No_Servidos} \nPisos totales: {Pisos_Totales}")

    Poblacion_Total = Poblacion_Piso*Pisos_Servidos + Poblacion_Sotano*Sotanos # (B)


    if Paridad == "Impar":

        Recorrido_Ppal_Super = Pisos_Totales*Distancia_Promedio_Impar
        Recorrido_Ppal_1PSuper = Pisos_No_Servidos*Distancia_Promedio_Impar

    elif Paridad == "Par":

        Recorrido_Ppal_Super == Pisos_Totales*Distancia_Promedio_Par
        Recorrido_Ppal_1PSuper == Pisos_No_Servidos*Distancia_Promedio_Par

    else:

        print("Paridad no establecida.")
    
        Recorrido_Ppal_Super = Pisos_Totales*Distancia_Promedio #(Ha)
        Recorrido_Ppal_1PSuper = Pisos_No_Servidos*Distancia_Promedio #(He)

    Recorrido_Sotanos = Sotanos*Distancia_Promedio #(Hi)
    Recorrido_Superior_Servido = Recorrido_Ppal_Super - Recorrido_Ppal_1PSuper #(Hs)
    Recorrido_Total = Recorrido_Ppal_Super + Recorrido_Sotanos #(Ht)

    
    Personas_Viaje = numpy.nan_to_num(int((3.2/Capacidad_Nominal_P)+(0.7*Capacidad_Nominal_P)+0.5)) #Pv

    Paradas_Probables = Pisos_Servidos*(1-(((Pisos_Servidos-1)/Pisos_Servidos)**Personas_Viaje)) #np

    Aceleracion = 1 #m/s

    ReferenciaV_Nom = numpy.sqrt((Recorrido_Superior_Servido*Aceleracion)/Paradas_Probables)


    if ReferenciaV_Nom < Velocidad_Nominal_Establecida and Zona_expresa == False:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/numpy.sqrt(Recorrido_Ppal_Super*Aceleracion/Paradas_Probables))+(Velocidad_Nominal_Establecida/Aceleracion)+(Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)+(Tiempo_Apertira_cierre*(Paradas_Probables+1))+Tiempo_Entrada_Salida*Personas_Viaje

    elif ReferenciaV_Nom >= Velocidad_Nominal_Establecida and Zona_expresa == False:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)+((Velocidad_Nominal_Establecida/Aceleracion)+Tiempo_Apertira_cierre)*(Paradas_Probables+1)+Tiempo_Entrada_Salida*Personas_Viaje

    elif ReferenciaV_Nom >= Velocidad_Nominal_Establecida and Zona_expresa == True:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)+((Velocidad_Nominal_Establecida/Aceleracion)+Tiempo_Apertira_cierre)*(Paradas_Probables+1)-(Recorrido_Superior_Servido/(Paradas_Probables*Velocidad_Nominal_Establecida))+Tiempo_Entrada_Salida*Personas_Viaje

    elif ReferenciaV_Nom < Velocidad_Nominal_Establecida and Zona_expresa == True:

        Tiempo_Viaje_Completo = (2*Recorrido_Ppal_Super/Velocidad_Nominal_Establecida)-(Recorrido_Superior_Servido/Velocidad_Nominal_Establecida)+(2*Velocidad_Nominal_Establecida/Aceleracion)+(((2*Recorrido_Superior_Servido)/(Paradas_Probables*ReferenciaV_Nom))*(Paradas_Probables-1))+(Tiempo_Apertira_cierre*(Paradas_Probables+1))+Tiempo_Entrada_Salida*Personas_Viaje

    else:

        print("Valor errado para Tiempo de Viaje Completo.")


    Tiempo_Total_Viaje = Tiempo_Viaje_Completo + Tiempo_Viaje_Completo*Tiempo_Adicional


    Capacidad_Transporte = (300*Personas_Viaje*Nro_Ascensores*100)/(Tiempo_Total_Viaje*Poblacion_Total) # (C)
    Intervalo_Probable = Tiempo_Total_Viaje/Nro_Ascensores


    Tiempo_Llenado = 500/Capacidad_Transporte

    print(f"Número de Ascensores: {Nro_Ascensores}")
    print(f"\nLa Vel. Nominal establecida es: {Velocidad_Nominal_Establecida} [m/s]")
    print(f"Referencial Vel. Nominal: {ReferenciaV_Nom}")
    print(f"\nRecorrido Superior: {Recorrido_Ppal_Super}")
    print(f"Recorrido Expreso: {Recorrido_Ppal_1PSuper}")
    print(f"Recorrido Superior Servido: {Recorrido_Superior_Servido} \n")

    print(f"Tiempo de apertura y cierre: {Tiempo_Apertira_cierre}")
    print(f"Tiempo de entrada y salida: {Tiempo_Entrada_Salida} \n")

    print(f"Tiempo de Viaje Completo: {Tiempo_Viaje_Completo} [s]")
    print(f"Tiempo Total de Viaje: {Tiempo_Total_Viaje} [s] \n")
    print(f"Capacidad nominal: {Capacidad_Nominal_P}")
    print(f"Personas por viaje: {Personas_Viaje}")
    print(f"Población total: {Poblacion_Total}")
    print(f"Paradas probables: {Paradas_Probables} \n")
    print(f"Capacidad de Transporte [C]: {Capacidad_Transporte} % (>12)")
    print(f"Intervalo Probable [I]: {Intervalo_Probable} [s] (<40) \n")
    print(f"Tiempo de llenado: {Tiempo_Llenado}")

    

    return (Res_Grupo, Zona_expresa,Pisos_Servidos,Pisos_No_Servidos,Pisos_Totales,Nro_Ascensores,Velocidad_Nominal_Establecida,ReferenciaV_Nom,Recorrido_Ppal_Super,Recorrido_Ppal_1PSuper,Recorrido_Superior_Servido,Tiempo_Apertira_cierre,Tiempo_Entrada_Salida,Tiempo_Viaje_Completo,Tiempo_Total_Viaje,Capacidad_Nominal_P,Personas_Viaje,Poblacion_Total,Paradas_Probables,Capacidad_Transporte,Intervalo_Probable,Tiempo_Llenado)

def Guardar_Calculo(Res_Grupo,Zona_expresa,Pisos_Servidos,Pisos_No_Servidos,Pisos_Totales,Nro_Ascensores,Velocidad_Nominal_Establecida,ReferenciaV_Nom,Recorrido_Ppal_Super,Recorrido_Ppal_1PSuper,Recorrido_Superior_Servido,Tiempo_Apertira_cierre,Tiempo_Entrada_Salida,Tiempo_Viaje_Completo,Tiempo_Total_Viaje,Capacidad_Nominal_P,Personas_Viaje,Poblacion_Total,Paradas_Probables,Capacidad_Transporte,Intervalo_Probable,Tiempo_Llenado): 


    df = pd.DataFrame({ "Grupo" : [Res_Grupo],
                            "Ascensores" : [Nro_Ascensores],
                            "Zona expresa" : [Zona_expresa],
                            "Pisos Servidos" : [Pisos_Servidos],
                            "Pisos no servidos" : [Pisos_No_Servidos],
                            "Pisos totales" : [Pisos_Totales],
                            "Velocidad Nominal" : [Velocidad_Nominal_Establecida],
                            "Ref. Vel. Nominal" : [ReferenciaV_Nom],
                            "Recorrido superior" : [Recorrido_Ppal_Super],
                            "Recorrido expreso" : [Recorrido_Ppal_1PSuper],
                            "Recorrido superior servido" : [Recorrido_Superior_Servido],
                            "Tiempo de apertura y cierre" : [Tiempo_Apertira_cierre],
                            "Tiempo de entrada y salida" : [Tiempo_Entrada_Salida],
                            "Tiempo de Viaje Completo" : [Tiempo_Viaje_Completo],
                            "Tiempo Total de viaje" : [Tiempo_Total_Viaje],
                            "Capacidad Nominal" : [Capacidad_Nominal_P],
                            "Personas por viaje" : [Personas_Viaje],
                            "Paradas Probables" : [Paradas_Probables],
                            "C (>12)" : [Capacidad_Transporte],
                            "I (<40)" : [Intervalo_Probable],
                            "Tiempo de llenado" : [Tiempo_Llenado]})
        
    df = df[["Grupo",
                 "Ascensores",
                 "Zona expresa",
                 "Pisos Servidos",
                 "Pisos no servidos",
                 "Pisos totales",
                 "Velocidad Nominal",
                 "Ref. Vel. Nominal",
                 "Recorrido superior",
                 "Recorrido expreso",
                 "Recorrido superior servido",
                 "Tiempo de apertura y cierre",
                 "Tiempo de entrada y salida",
                 "Tiempo de Viaje Completo",
                 "Tiempo Total de viaje",
                 "Capacidad Nominal",
                 "Personas por viaje",
                 "Paradas Probables",
                 "C (>12)",
                 "I (<40)",
                 "Tiempo de llenado"]]
        
    Writer = ExcelWriter(f".\\Cálculo Todos.xlsx")
    df.to_excel(Writer, f"Calculo Todos", index=False)

    try:

        Writer._save()

        if AttributeError:

            print("\nError al guardar:", AttributeError)

    finally:

        print(f"Programa terminado para {Res_Grupo}.\n")

    

def run():
    print(de)

    Res_Grupo_G, Zona_expresa_G,Pisos_Servidos_G,Pisos_No_Servidos_G,Pisos_Totales_G,Nro_Ascensores_G,Velocidad_Nominal_Establecida_G,ReferenciaV_Nom_G,Recorrido_Ppal_Super_G,Recorrido_Ppal_1PSuper_G,Recorrido_Superior_Servido_G,Tiempo_Apertira_cierre_G,Tiempo_Entrada_Salida_G,Tiempo_Viaje_Completo_G,Tiempo_Total_Viaje_G,Capacidad_Nominal_P_G,Personas_Viaje_G,Poblacion_Total_G,Paradas_Probables_G,Capacidad_Transporte_G,Intervalo_Probable_G,Tiempo_Llenado_G = main(1)
    Guardar_Calculo(Res_Grupo_G,Zona_expresa_G,Pisos_Servidos_G,Pisos_No_Servidos_G,Pisos_Totales_G,Nro_Ascensores_G,Velocidad_Nominal_Establecida_G,ReferenciaV_Nom_G,Recorrido_Ppal_Super_G,Recorrido_Ppal_1PSuper_G,Recorrido_Superior_Servido_G,Tiempo_Apertira_cierre_G,Tiempo_Entrada_Salida_G,Tiempo_Viaje_Completo_G,Tiempo_Total_Viaje_G,Capacidad_Nominal_P_G,Personas_Viaje_G,Poblacion_Total_G,Paradas_Probables_G,Capacidad_Transporte_G,Intervalo_Probable_G,Tiempo_Llenado_G)

    Res_Grupo_2, Zona_expresa_2,Pisos_Servidos_2,Pisos_No_Servidos_2,Pisos_Totales_2,Nro_Ascensores_2,Velocidad_Nominal_Establecida_2,ReferenciaV_Nom_2,Recorrido_Ppal_Super_2,Recorrido_Ppal_1PSuper_2,Recorrido_Superior_Servido_2,Tiempo_Apertira_cierre_2,Tiempo_Entrada_Salida_2,Tiempo_Viaje_Completo_2,Tiempo_Total_Viaje_2,Capacidad_Nominal_P_2,Personas_Viaje_2,Poblacion_Total_2,Paradas_Probables_2,Capacidad_Transporte_2,Intervalo_Probable_2,Tiempo_Llenado_2 = main(2)
    Guardar_Calculo(Res_Grupo_2,Zona_expresa_2,Pisos_Servidos_2,Pisos_No_Servidos_2,Pisos_Totales_2,Nro_Ascensores_2,Velocidad_Nominal_Establecida_2,ReferenciaV_Nom_2,Recorrido_Ppal_Super_2,Recorrido_Ppal_1PSuper_2,Recorrido_Superior_Servido_2,Tiempo_Apertira_cierre_2,Tiempo_Entrada_Salida_2,Tiempo_Viaje_Completo_2,Tiempo_Total_Viaje_2,Capacidad_Nominal_P_2,Personas_Viaje_2,Poblacion_Total_2,Paradas_Probables_2,Capacidad_Transporte_2,Intervalo_Probable_2,Tiempo_Llenado_2)

    Res_Grupo_3, Zona_expresa_3,Pisos_Servidos_3,Pisos_No_Servidos_3,Pisos_Totales_3,Nro_Ascensores_3,Velocidad_Nominal_Establecida_3,ReferenciaV_Nom_3,Recorrido_Ppal_Super_3,Recorrido_Ppal_1PSuper_3,Recorrido_Superior_Servido_3,Tiempo_Apertira_cierre_3,Tiempo_Entrada_Salida_3,Tiempo_Viaje_Completo_3,Tiempo_Total_Viaje_3,Capacidad_Nominal_P_3,Personas_Viaje_3,Poblacion_Total_3,Paradas_Probables_3,Capacidad_Transporte_3,Intervalo_Probable_3,Tiempo_Llenado_3 = main(3)
    Guardar_Calculo(Res_Grupo_3,Zona_expresa_3,Pisos_Servidos_3,Pisos_No_Servidos_3,Pisos_Totales_3,Nro_Ascensores_3,Velocidad_Nominal_Establecida_3,ReferenciaV_Nom_3,Recorrido_Ppal_Super_3,Recorrido_Ppal_1PSuper_3,Recorrido_Superior_Servido_3,Tiempo_Apertira_cierre_3,Tiempo_Entrada_Salida_3,Tiempo_Viaje_Completo_3,Tiempo_Total_Viaje_3,Capacidad_Nominal_P_3,Personas_Viaje_3,Poblacion_Total_3,Paradas_Probables_3,Capacidad_Transporte_3,Intervalo_Probable_3,Tiempo_Llenado_3)

    Res_Grupo_4, Zona_expresa_4,Pisos_Servidos_4,Pisos_No_Servidos_4,Pisos_Totales_4,Nro_Ascensores_4,Velocidad_Nominal_Establecida_4,ReferenciaV_Nom_4,Recorrido_Ppal_Super_4,Recorrido_Ppal_1PSuper_4,Recorrido_Superior_Servido_4,Tiempo_Apertira_cierre_4,Tiempo_Entrada_Salida_4,Tiempo_Viaje_Completo_4,Tiempo_Total_Viaje_4,Capacidad_Nominal_P_4,Personas_Viaje_4,Poblacion_Total_4,Paradas_Probables_4,Capacidad_Transporte_4,Intervalo_Probable_4,Tiempo_Llenado_4 = main(4)
    Guardar_Calculo(Res_Grupo_4,Zona_expresa_4,Pisos_Servidos_4,Pisos_No_Servidos_4,Pisos_Totales_4,Nro_Ascensores_4,Velocidad_Nominal_Establecida_4,ReferenciaV_Nom_4,Recorrido_Ppal_Super_4,Recorrido_Ppal_1PSuper_4,Recorrido_Superior_Servido_4,Tiempo_Apertira_cierre_4,Tiempo_Entrada_Salida_4,Tiempo_Viaje_Completo_4,Tiempo_Total_Viaje_4,Capacidad_Nominal_P_4,Personas_Viaje_4,Poblacion_Total_4,Paradas_Probables_4,Capacidad_Transporte_4,Intervalo_Probable_4,Tiempo_Llenado_4)


if __name__ == "__main__":

    print("Running... \n")
    run()
    