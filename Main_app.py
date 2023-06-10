
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

    Nro_Ascensores = 6


    NN = 0

    '''
        na = 88
        ep = 3.5m
        np = 88
        ne = 0

        Ha = 308

        Hs = 308
    '''

    Area_Pisos = 750 #m^2

    Aceleracion = 1 #m/s^2

    #----------------------------------------------------------

    ne = 0 #Numero de pisos no servidos por encima de la planta principal

    np = 84 #Numero de paradas probables en los pisos superiores

    ns = 84 #Numero de pisos servidos encima de la planta principal

    na = ns + ne #Número total de pisos encima de la planta principal.

    Ha = na*np #Recorrido entre la planta principal y superior

    He = 3.5 #Recorrido entre la planta principal y la primera planta superior servida

    Hs = Ha - He #Recorrido sobre la planta principal con servicio de ascensores entre la primera y la ultima parada superior

    Vn = numpy.sqrt(Hs*Aceleracion/np)

    print ("Velocidad Nominal 1: " , Vn)

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

    


    def Paradas_Probables(ns):

        # ns: número de pisos servidos por encima de la planta principal.
        Np = ns(1-((ns-1)/(ns)))

    def Personas_por_Viaje(P):
    
        # P: capacidad nominal de la cabina (personas).
        Pv = (3.2/P)+(0.7*P)+0.5

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

    




    
    #Guardar_Calculo()
    
    
if __name__ == "__main__":
    print("Running...")
    main()
    