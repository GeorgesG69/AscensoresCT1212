
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

    # Valores establecidos para el Sistema de Ascensores.

    Altura_entre_pisos = 3.5 #m
    Sotanos = 3
    Planta_Principal = 1
    Pisos_Superiores = 84
    Pisos_Totales = Pisos_Superiores + Planta_Principal + Sotanos

    # Cantidad de personas    

    Personas_Sotanos = 15
    Personas_P_Superiores = 35
    
    P = 20 #Capacidad nominal de la cabina

    Tiempo_Apertura_Cierre = 4.43 #s

    # Datos Grupo A: 
    '''
        El Grupo A atiende los pisos pares, la planta principal y 3 sótanos.
    '''

    Poblacion_estimada_A = 1515
    
    Nro_Ascensores_A = 7
    Velocidad_Nominal_A = 4 #m/s
    Tiempo_Entrada_Salida_A = 1.8 #s

    print(f"[Grupo A]La Vel. Nominal establecida es: {Velocidad_Nominal_A} [m/s]")

    # Datos Grupo B:

    '''
        El grupo B atiende los pisos impares, la planta principal y 3 sótanos.
    '''
    Poblacion_estimada_B = 1515

    Nro_Ascensores_B = 3
    Velocidad_Nominal_B = 6 #m/s
    Tiempo_Entrada_Salida_B = 2

    Nro_Ascensores = Nro_Ascensores_A + Nro_Ascensores_B #Bloque A + Bloque B

    Area_Pisos = 750 #m^2

    
    Aceleracion = 1 #m/s^2

    #----------------------------------------------------------

    '''
        El sistema de ascensores se divide en 2 grupos (A y B) de ascensores, con 3 ascensores cada uno
        (un total de 6 ascensores)
    '''
 
    #------------------------Cálculos del Grupo A (Pisos Pares):


    print("\n Cálculos del grupo A: \n")

    ne_A = 69 #Numero de pisos NO servidos por encima de la planta principal

    ns_A = 16 #Numero de pisos servidos encima de la planta principal

    Np_A = ns_A*(1-((ns_A-1)/(ns_A))) # Nro de paradas probables en los pisos superiores

    na_A = ns_A + ne_A #Número total de pisos encima de la planta principal.

    Ha_A = na_A*Np_A #Recorrido entre la planta principal y superior

    He_A = 3.5 #Recorrido entre la planta principal y la primera planta superior servida

    Hs_A = Ha_A - He_A #Recorrido sobre la planta principal con servicio de ascensores entre la primera y la ultima parada superior

    RVn_A = numpy.sqrt(Hs_A*Aceleracion/Np_A)

    print("[Grupo A] Referencial Vel. nominal es: " , RVn_A)

    # P: capacidad nominal de la cabina (personas).

    Pv_A = int((3.2/P)+(0.7*P)+0.5)
    # -(Hs_A/(Np_A*Velocidad_Nominal_A))
    Tiempo_Viaje_Completo_A = (2*(Ha_A/Velocidad_Nominal_A))+(((Velocidad_Nominal_A/Aceleracion)+Tiempo_Apertura_Cierre)*(Np_A+1))-(Hs_A/(Np_A*Velocidad_Nominal_A))+(Tiempo_Entrada_Salida_A*Pv_A)

    print("[Grupo A] Tiempo de Viaje completo: ", Tiempo_Viaje_Completo_A)

    Tiempo_Total_Viaje_A = Tiempo_Viaje_Completo_A + Tiempo_Viaje_Completo_A*(30/100)

    print("[Grupo A] Tiempo Total de Viaje: ", Tiempo_Total_Viaje_A)

    

    print("[Grupo A] Personas por viaje: ", Pv_A)

    C_A = (300*(Pv_A)*(Nro_Ascensores)*100)/(Tiempo_Total_Viaje_A*Poblacion_estimada_A)

    print("[Grupo A] Capacidad de transporte: ", C_A, "%")

    I_A = Tiempo_Total_Viaje_A/Nro_Ascensores_A

    print("[Grupo A] Intervalo probable: ", I_A , "[s] \n")


    #----------Cálculos del Grupo B (Pisos Impares):

    print(f"[Grupo B] La Vel. Nominal establecida es: {Velocidad_Nominal_B} [m/s]")
    print("\n Cálculos del grupo B: \n")

    ne_B = 42 #Numero de pisos NO servidos por encima de la planta principal

    ns_B = 42 #Numero de pisos servidos encima de la planta principal

    Np_B = ns_B*(1-((ns_B-1)/(ns_B))) # Nro de paradas probables en los pisos superiores

    na_B = ns_B + ne_B #Número total de pisos encima de la planta principal.

    Ha_B = na_B*Np_B #Recorrido entre la planta principal y superior

    He_B = 3.5 #Recorrido entre la planta principal y la primera planta superior servida

    Hs_B = Ha_B - He_B #Recorrido sobre la planta principal con servicio de ascensores entre la primera y la ultima parada superior

    RVn_B = numpy.sqrt(Hs_B*Aceleracion/Np_B)

    print("[Grupo B] Referencial Vel. nominal es: " , RVn_B)

    # P: capacidad nominal de la cabina (personas).

    Pv_B = int((3.2/P)+(0.7*P)+0.5)
    # -(Hs_A/(Np_A*Velocidad_Nominal_A))
    Tiempo_Viaje_Completo_B = (2*(Ha_B/Velocidad_Nominal_B))+(((Velocidad_Nominal_B/Aceleracion)+Tiempo_Apertura_Cierre)*(Np_B+1))-(Hs_B/(Np_B*Velocidad_Nominal_B))+(Tiempo_Entrada_Salida_B*Pv_B)

    print("[Grupo B] Tiempo de Viaje completo: ", Tiempo_Viaje_Completo_B)

    Tiempo_Total_Viaje_B = Tiempo_Viaje_Completo_B + Tiempo_Viaje_Completo_B*(30/100)

    print("[Grupo B] Tiempo Total de Viaje: ", Tiempo_Total_Viaje_B)

    

    print("[Grupo B] Personas por viaje: ", Pv_B)

    C_B = (300*(Pv_B)*(Nro_Ascensores)*100)/(Tiempo_Total_Viaje_B*Poblacion_estimada_B)

    print("[Grupo B] Capacidad de transporte: ", C_A, "%")

    I_B = Tiempo_Total_Viaje_A/Nro_Ascensores_B

    print("[Grupo B] Intervalo probable: ", I_B , "[s]")


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
    