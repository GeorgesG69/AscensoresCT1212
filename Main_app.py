
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
Este edificio cuenta con 85 plantas superiores y 3 sotanos, un total de 57 plantas.

La altura entre pisos es de 3.5m  

'''

import numpy
import openpyxl

wb = openpyxl.Workbook()

def main():

    # Valores establecidos para el Sistema de Ascensores.

    Altura_entre_pisos = 3.5 #m
    Sotanos = 3
    Planta_Principal = 1
    Pisos_Superiores = 84
    Pisos_Totales = Pisos_Superiores + Planta_Principal + Sotanos
    

    Personas_Sotanos = 15
    Personas_P_Superiores = 35
    Poblacion_estimada = 3020

    Nro_Ascensores = 6


    Tiempo_Viaje_Completo = 104 #S

    Tiempo_Total_Viaje = Tiempo_Viaje_Completo + Tiempo_Viaje_Completo*(30/100)


    Area_Pisos = 750 #m^2

    Aceleracion = 1 #m/s^2

    #----------------------------------------------------------

    '''
        El sistema de ascensores se divide en 2 grupos (A y B) de ascensores, con 3 ascensores cada uno
        (un total de 6 ascensores)
    '''
 

    # Valores del Grupo A (Pisos Pares):

   

    Entrada_libre_minima = float(input("Ingrese la Entrada Libre mínima: "))
    #Velocidad_Nominal = float()
    #TiempoP_Apertura_T1 = float()
    #Tiempo_Entrada_Salida_T2 = float()

    if Entrada_libre_minima == 800:

        Tiempo_Entrada_Salida_T2 = 2.2 #s
        TiempoP_Apertura_T1 = 4.3 #s
        Velocidad_Nominal = 1.6 #m/s

    elif Entrada_libre_minima >= 900 and Entrada_libre_minima <= 1000:

        TiempoP_Apertura_T1 = 5.26 #s
        Velocidad_Nominal = 2 #m/s

    if Entrada_libre_minima == 900:

        Tiempo_Entrada_Salida_T2 = 2.1 #s

    elif Entrada_libre_minima == 1000:

        Tiempo_Entrada_Salida_T2 = 2 #s

    elif Entrada_libre_minima == 1100:

        Tiempo_Entrada_Salida_T2 = 1.9 #s

    elif Entrada_libre_minima == 1200:

        Tiempo_Entrada_Salida_T2 = 1.8 #s

    
    
    else:

        print("Entrada Libre Mínima: Fuera de rango.")

    

    print("La Velocidad Nominal [Vn] del ascensor es de: " , Velocidad_Nominal , "[m/s]")
    print("El Tiempo Promedio de Apertura [T1] es de: " , TiempoP_Apertura_T1 , "[s]")
    print("El Tiempo de Entrada y Salida es de: " , Tiempo_Entrada_Salida_T2 , "[s]")

    # Cálculos Generales:

    def Paradas_Probables(ns):

        # ns: número de pisos servidos por encima de la planta principal.
        Np = ns*(1-((ns-1)/(ns)))
        return Np

    def Personas_por_Viaje(P):
    
        # P: capacidad nominal de la cabina (personas).
        Pv = (3.2/P)+(0.7*P)+0.5

        return Pv
    
    

        
    
    def Capacidad_de_Transporte(Nro_Ascensores):

        C = (300*Personas_por_Viaje*Nro_Ascensores*100)/Tiempo_Total_Viaje*Poblacion_estimada

        return C

    def Valor_Contrapeso_Cabina():

        pass

    # Determinar cantidad de pasajeros según la norma COVENIN.

    def Cantidad_Pasajeros():

        pass

    def Guardar_Calculo():

        #HojaCreada = wb.create_sheet("Cálculo", 0)

        Hoja = wb.active

        Hoja["A1"] = "Hola"

        wb.save("Prueba.xlsx")

        pass

    def Valores_Grupo_A_PPares(ne_A, np_A, ns_A):



        #ne_A = 0 #Numero de pisos no servidos por encima de la planta principal

        #np_A = 42 #Numero de paradas probables en los pisos superiores

        #ns_A = 42 #Numero de pisos servidos encima de la planta principal

        na_A = ns_A + ne_A #Número total de pisos encima de la planta principal.

        Ha_A = na_A*np_A #Recorrido entre la planta principal y superior

        He_A = 3.5 #Recorrido entre la planta principal y la primera planta superior servida

        Hs_A = Ha_A - He_A #Recorrido sobre la planta principal con servicio de ascensores entre la primera y la ultima parada superior

        Vn_A = numpy.sqrt(Hs_A*Aceleracion/np_A)

        print ("[Grupo A] Velocidad Nominal 1: " , Vn_A)

    
    
    #Guardar_Calculo()
    
    Valores_Grupo_A_PPares(42, Paradas_Probables(42), 42, )
    
    
if __name__ == "__main__":
    print("Running...")
    main()
    