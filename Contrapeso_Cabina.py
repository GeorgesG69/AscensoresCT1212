# Determinación de los valores del Contrapeso y la Cabina según la normativa Covenin.

import numpy
import pandas as pd
import sys

filepath = "./datos_ascensores.xlsm"
de = pd.read_excel("datos_ascensores.xls")

print(de)

def Carga(f):

    Carga_nominal = de.iloc[f, 9]

    Peso_estructura_carro = Carga_nominal/2
    Exceso_Carga_Nominal = Carga_nominal*5/10
    Peso_Contrapeso = 1.5*Peso_estructura_carro

    print(f"Contrapeso: {Peso_Contrapeso}")
    print(f"Peso Cabina = {Peso_estructura_carro}")

    return Carga_nominal, Peso_estructura_carro, Peso_Contrapeso, Exceso_Carga_Nominal



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


print(f"Peso del cable + Carga máxima: {Peso_Cable}\n")

print(f"Factor seguridad (F): {Factor_Seguridad} \n")





