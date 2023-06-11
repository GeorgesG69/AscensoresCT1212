
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

    # Cantidad de personas    

    Personas_Sotanos = 15
    Personas_P_Superiores = 35
    Poblacion_estimada = 3020
    P = 20 #Capacidad nominal de la cabina

    Tiempo_Apertura_Cierre = 3 #s
    

    Nro_Ascensores = 6 #Bloque A + Bloque B

    Area_Pisos = 750 #m^2

    Velocidad_Nominal_A = 6 #m/s
    Aceleracion = 1 #m/s^2

    #----------------------------------------------------------

    '''
        El sistema de ascensores se divide en 2 grupos (A y B) de ascensores, con 3 ascensores cada uno
        (un total de 6 ascensores)
    '''
 
    # Cálculos del Grupo A (Pisos Pares):

    ne_A = 0 #Numero de pisos no servidos por encima de la planta principal

    np_A = 42 #Numero de paradas probables en los pisos superiores

    ns_A = 42 #Numero de pisos servidos encima de la planta principal

    na_A = ns_A + ne_A #Número total de pisos encima de la planta principal.

    Ha_A = na_A*np_A #Recorrido entre la planta principal y superior

    He_A = 3.5 #Recorrido entre la planta principal y la primera planta superior servida

    Hs_A = Ha_A - He_A #Recorrido sobre la planta principal con servicio de ascensores entre la primera y la ultima parada superior

    RVn_A = numpy.sqrt(Hs_A*Aceleracion/np_A)

    print("[Grupo A] Referencial Vnominal es: " , RVn_A)

    Tiempo_Viaje_Completo_A = (2*(Ha_A/Velocidad_Nominal_A))+((Velocidad_Nominal_A/Aceleracion)+Tiempo_Apertura_Cierre)
    Tiempo_Total_Viaje_A = Tiempo_Viaje_Completo_A + Tiempo_Viaje_Completo_A*(30/100)

    # ns: número de pisos servidos por encima de la planta principal.
    Np = ns_A*(1-((ns_A-1)/(ns_A)))

    # P: capacidad nominal de la cabina (personas).

    Pv = (3.2/P)+(0.7*P)+0.5

    print("Personas por viaje: ", Pv)

    C = (300*(Pv)*(Nro_Ascensores)*100)/(Tiempo_Total_Viaje_A*Poblacion_estimada)

    print("Capacidad de transporte: ", C, "%")


    I = Tiempo_Total_Viaje_A/Nro_Ascensores

    print("Intervalo probable: ", I)

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
    