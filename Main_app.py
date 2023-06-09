import numpy
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

def main():

    # Valores establecidos para el Sistema de Ascensores.

    Altura_entre_pisos = 3.5
    Sotanos = 3
    Pisos_Superiores = 85
    Pisos_Totales = Pisos_Superiores + Sotanos
    Pisos_Sobre_PSuperior = Pisos_Totales - 1

    Personas_Sotanos = 15
    Personas_P_Superiores = 35

    Nro_Ascensores = 6

    #TVC = 

    Area_Pisos = 750

    def Paradas_Probables(ns):

        # ns: número de pisos servidos por encima de la planta principal.
        Np = ns(1-((ns-1)/(ns)))

    def Personas_por_Viaje(P):
    
        # P: capacidad nominal de la cabina (personas).
        Pv = (3.2/P)+(0.7*P)+0.5

    #def Tiempo_Total_Viaje():

      #  TTV = TVC + TA
    
    #def Capacidad_de_Transporte(Pv):

    #    global Pv
    #    global TTV 

     #   C = (300*Pv*Nro_Ascensores*100)/(TTV*B)

    # Determinar el valor del contrapeso y cabina.

    def Valor_Contrapeso_Cabina():


        pass

    # Determinar cantidad de pasajeros según la norma COVENIN.

    def Cantidad_Pasajeros():


        pass

    pass
    

if __name__ == "__main__":
    main()