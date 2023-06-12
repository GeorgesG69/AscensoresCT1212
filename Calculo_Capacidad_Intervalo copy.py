
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
    Planta_Principal = 1
    Pisos_Superiores = 84
    Sotanos = 3 # (ni)
    Distancia_Promedio = 3.5 #m (ep)
    Pisos_No_Servidos = 0 # (ne)
    Pisos_Servidos = 84 #(ns)
    Pisos_Totales = Pisos_Servidos + Pisos_No_Servidos # (na)

    print(f"Pisos servidos: {Pisos_Servidos} \n Pisos NO servidos: {Pisos_No_Servidos} \n Pisos totales: {Pisos_Totales}")
    
    Recorrido_Ppal_Super = Pisos_Totales*Distancia_Promedio #(Ha)



    Aceleracion = 1 #m/s
    Poblacion_Piso = 35
    Poblacion_Sotano = 15


    ReferenciaV_Nom = numpy.sqrt()

    Tiempo_Adicional = 30/10

    if ():
        Tiempo_Viaje_Completo = 0

    Tiempo_Total_Viaje = Tiempo_Viaje_Completo + Tiempo_Viaje_Completo*Tiempo_Adicional
    



    def Guardar_Calculo():

        #HojaCreada = wb.create_sheet("Cálculo", 0)

        Hoja = wb.active

        Hoja["A1"] = "Hola"

        wb.save("Prueba.xlsx")

        pass

    #Guardar_Calculo()

    
if __name__ == "__main__":
    print("Running...")
    main()
    