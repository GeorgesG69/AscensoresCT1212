
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

    




    
    #Guardar_Calculo()
    
    
if __name__ == "__main__":
    main()
    print("hola")