
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

    # Datos Grupo A: 
    
    Nro_Ascensores_A = 3
    Velocidad_Nominal_A = 6 #m/s
    Tiempo_Entrada_Salida_A = 2 #s

    # Datos Grupo B:
    Nro_Ascensores_B = 3
    Nro_Ascensores = Nro_Ascensores_A + Nro_Ascensores_B #Bloque A + Bloque B

    Area_Pisos = 750 #m^2

    
    Aceleracion = 1 #m/s^2

    #----------------------------------------------------------

    '''
        El sistema de ascensores se divide en 2 grupos (A y B) de ascensores, con 3 ascensores cada uno
        (un total de 6 ascensores)
    '''
 
    # Cálculos del Grupo A (Pisos Pares):

    ne_A = 0 #Numero de pisos NO servidos por encima de la planta principal

    ns_A = 28 #Numero de pisos servidos encima de la planta principal

    Np_A = ns_A*(1-((ns_A-1)/(ns_A))) # Nro de paradas probables en los pisos superiores

    na_A = ns_A + ne_A #Número total de pisos encima de la planta principal.

    Ha_A = na_A*Np_A #Recorrido entre la planta principal y superior

    He_A = 3.5 #Recorrido entre la planta principal y la primera planta superior servida

    Hs_A = Ha_A - He_A #Recorrido sobre la planta principal con servicio de ascensores entre la primera y la ultima parada superior

    RVn_A = numpy.sqrt(Hs_A*Aceleracion/Np_A)

    print("[Grupo A] Referencial Vel. nominal es: " , RVn_A)

    # P: capacidad nominal de la cabina (personas).

    Pv_A = (3.2/P)+(0.7*P)+0.5
    # -(Hs_A/(Np_A*Velocidad_Nominal_A))
    Tiempo_Viaje_Completo_A = (2*(Ha_A/Velocidad_Nominal_A))+(((Velocidad_Nominal_A/Aceleracion)+Tiempo_Apertura_Cierre)*(Np_A+1))+(Tiempo_Entrada_Salida_A*Pv_A)

    print("[Grupo A] Tiempo de Viaje completo: ", Tiempo_Viaje_Completo_A)

    Tiempo_Total_Viaje_A = Tiempo_Viaje_Completo_A + Tiempo_Viaje_Completo_A*(30/100)

    print("[Grupo A] Tiempo Total de Viaje: ", Tiempo_Total_Viaje_A)

    

    print("[Grupo A] Personas por viaje: ", Pv_A)

    C_A = (300*(Pv_A)*(Nro_Ascensores)*100)/(Tiempo_Total_Viaje_A*Poblacion_estimada)

    print("[Grupo A] Capacidad de transporte: ", C_A, "%")

    I_A = Tiempo_Total_Viaje_A/Nro_Ascensores_A

    print("[Grupo A] Intervalo probable: ", I_A , "[s]")

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
    