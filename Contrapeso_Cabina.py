# Determinación de los valores del Contrapeso y la Cabina según la normativa Covenin.

import numpy
import pandas
import sys

sys.path.append("C:\\Users\\Georges\\Desktop\\Mine\\Proyectos CT1212\\Ascensores\\AscensoresCT1212\\Calculo_Capacidad_Intervalo.py")
from Calculo_Capacidad_Intervalo import main

#Res_Grupo_G, Zona_expresa_G,Pisos_Servidos_G,Pisos_No_Servidos_G,Pisos_Totales_G,Nro_Ascensores_G,Velocidad_Nominal_Establecida_G,ReferenciaV_Nom_G,Recorrido_Ppal_Super_G,Recorrido_Ppal_1PSuper_G,Recorrido_Superior_Servido_G,Tiempo_Apertira_cierre_G,Tiempo_Entrada_Salida_G,Tiempo_Viaje_Completo_G,Tiempo_Total_Viaje_G,Capacidad_Nominal_P_G,Personas_Viaje_G,Poblacion_Total_G,Paradas_Probables_G,Capacidad_Transporte_G,Intervalo_Probable_G,Tiempo_Llenado_G = main

#print(f"Velocidad nominal: {Velocidad_Nominal_Establecida}")

Longitud_Fijacion_Cable = 0

Peso_estructura_carro = 500
Exceso_Carga_Nominal = 2000*4/10
Peso_Contrapeso = Peso_estructura_carro + Exceso_Carga_Nominal

Contrapeso_Pared = 5 + Longitud_Fijacion_Cable*2/1000
Carro_Contrapeso = 7 + Longitud_Fijacion_Cable*2/1000

# Cables:

Valor_T7 = 4

Nro_Cables_Suspencion = 15

Carga_Rotura_Cable = 2000

Peso_Cable = 0.14 + 2000

Factor_Seguridad = Valor_T7*Nro_Cables_Suspencion*Carga_Rotura_Cable/Peso_Cable

# Rozamiento entre cables y polea:
Coeficiente_M = 0.09

Tipo_Garganta = "cuna" #sin ñ

if Tipo_Garganta == "cuna":

    Angulo_Mecanizado_Garganta = 0.785398

    Indice_Rozamiento = Coeficiente_M/numpy.sin(Angulo_Mecanizado_Garganta/2)

elif Tipo_Garganta == "comb":

    Angulo_Entralladura = 0.785398

    Indice_Rozamiento = 4*Coeficiente_M*(1-numpy.sin(Angulo_Entralladura/2))/(numpy.pi-Angulo_Entralladura-numpy.sin(Angulo_Entralladura))

else:
    print("Tipo de garganta no especificado")

# Presion específica entre los cables y gargantas de la polea:

Carga_Estatica_Cables = 2000 + (1000)
Numero_Cables_Traccion = 15
Diametro_Cable_Traccion = 10
Diametro_Primitivo_Polea = 400

Velocidad_Nominal = 10


if Tipo_Garganta == "cuna":

    Presion_esp = (5*Carga_Estatica_Cables)/(Numero_Cables_Traccion*Diametro_Cable_Traccion*Diametro_Primitivo_Polea*numpy.sin(Angulo_Mecanizado_Garganta/2))

elif Tipo_Garganta == "comb":

    Presion_esp = (8*Carga_Estatica_Cables*numpy.cos(Angulo_Entralladura/2))/(Numero_Cables_Traccion*Diametro_Cable_Traccion*Diametro_Primitivo_Polea*(numpy.pi-Angulo_Entralladura-numpy.sin(Angulo_Entralladura)))

else:
    print("Error en la presion específica.")

Ref_Presion_esp = 125+40*Velocidad_Nominal


# Tension:

Tension_1 = Peso_estructura_carro*9.8
Tension_2 = Peso_Contrapeso*9.8

Ceoficiente_aceleracon = (9.8+1)/(9.8-1)
Coeficiente_Forma_Garganta = 1

ANgulo_Contacto = 141

Relacion_equilibrio_cables = Tension_1/Tension_2

efa = numpy.exp(Indice_Rozamiento*ANgulo_Contacto)

if Relacion_equilibrio_cables*Ceoficiente_aceleracon*Coeficiente_Forma_Garganta <= efa:

    print(f"Relación: {Relacion_equilibrio_cables*Ceoficiente_aceleracon*Coeficiente_Forma_Garganta} <= {efa}")
    print(f"Hay estabilidad en la instalación")

elif Relacion_equilibrio_cables*Ceoficiente_aceleracon*Coeficiente_Forma_Garganta > efa:

    print(f"Relación: {Relacion_equilibrio_cables*Ceoficiente_aceleracon*Coeficiente_Forma_Garganta} >= {efa}")
    print(f"No hay estabilidad en la instalación")



print(f"Valor de la tabla 7: {Valor_T7}")
print(f"Número de cables suspendidos: {Nro_Cables_Suspencion}")
print(f"Carga de rotura del cable: {Carga_Rotura_Cable}")
print(f"Peso del cable + Carga máxima: {Peso_Cable}\n")

print(f"Factor seguridad (F): {Factor_Seguridad} \n")

print(f"Indice de rozamiento: {Indice_Rozamiento}")
print(f"Referencia de la presión esperada: {Ref_Presion_esp}")
print(f"Presion esperada: {Presion_esp} \n")

