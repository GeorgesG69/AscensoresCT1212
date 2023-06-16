# Determinación de los valores del Contrapeso y la Cabina según la normativa Covenin.

import numpy
import pandas
import sys

sys.path.append("C:\\Users\\Georges\\Desktop\\Mine\\Proyectos CT1212\\Ascensores\\AscensoresCT1212\\Calculo_Capacidad_Intervalo.py")
from Calculo_Capacidad_Intervalo import main

#Res_Grupo_G, Zona_expresa_G,Pisos_Servidos_G,Pisos_No_Servidos_G,Pisos_Totales_G,Nro_Ascensores_G,Velocidad_Nominal_Establecida_G,ReferenciaV_Nom_G,Recorrido_Ppal_Super_G,Recorrido_Ppal_1PSuper_G,Recorrido_Superior_Servido_G,Tiempo_Apertira_cierre_G,Tiempo_Entrada_Salida_G,Tiempo_Viaje_Completo_G,Tiempo_Total_Viaje_G,Capacidad_Nominal_P_G,Personas_Viaje_G,Poblacion_Total_G,Paradas_Probables_G,Capacidad_Transporte_G,Intervalo_Probable_G,Tiempo_Llenado_G = main

#print(f"Velocidad nominal: {Velocidad_Nominal_Establecida}")

Carga_nominal = 1800

Peso_estructura_carro = Carga_nominal/2
Exceso_Carga_Nominal = Carga_nominal*5/10
Peso_Contrapeso = Peso_estructura_carro + Exceso_Carga_Nominal

# Cabina
#-Superficie:

Ancho_Cabina = 2100
Largo_Cabina = 1750

Superficie_Cabina = Ancho_Cabina*Largo_Cabina/1000

# Cables:

Valor_T7 = 4

Nro_Cables_Suspencion = 15

Carga_Rotura_Cable = 2000

Peso_Cable = 0.14 + 2000

Factor_Seguridad = Valor_T7*Nro_Cables_Suspencion*Carga_Rotura_Cable/Peso_Cable





print(f"Valor de la tabla 7: {Valor_T7}")
print(f"Número de cables suspendidos: {Nro_Cables_Suspencion}")
print(f"Carga de rotura del cable: {Carga_Rotura_Cable}\n")

print(f"Ancho cabina: {Ancho_Cabina/1000} [m]")
print(f"Largo cabina: {Largo_Cabina/1000} [m]")
print(f"Superficie de la cabina: {Superficie_Cabina} [m^2]\n")

print(f"Contrapeso: {Peso_Contrapeso}")
print(f"Peso Cabina = {Peso_estructura_carro}")
print(f"Peso del cable + Carga máxima: {Peso_Cable}\n")

print(f"Factor seguridad (F): {Factor_Seguridad} \n")





