# Determinación de los valores del Contrapeso y la Cabina según la normativa Covenin.

import numpy
import pandas as pd
import sys

filepath = "./datos_ascensores.xlsm"
de = pd.read_excel("datos_ascensores.xls")

def Carga(f, grupo):

    Carga_nominal = de.iloc[f, 9]

    Peso_estructura_carro = Carga_nominal/2
    Exceso_Carga_Nominal = Carga_nominal*5/10
    Peso_Contrapeso = 1.5*Peso_estructura_carro

    print(f"{grupo}\n")

    print(f"Carga nominal: {Carga_nominal}")
    print(f"Contrapeso: {Peso_Contrapeso}")
    print(f"Peso Cabina = {Peso_estructura_carro}\n")

    return Carga_nominal, Peso_estructura_carro, Peso_Contrapeso, Exceso_Carga_Nominal, grupo

def guardar(Carga_N, Peso_C, Peso_co, Grupo):

    df = pd.DataFrame({"Grupo" : [Grupo],
                       "Carga Nominal" : [Carga_N],
                       "Peso cabina" : [Peso_C],
                       "Peso contrapeso" : [Peso_co]})
    
    df = df[["Grupo",
             "Carga Nominal",
             "Peso Cabina",
             "Peso contrapeso"]]

    Escritor = pd.ExcelWriter(".\\Contrapeso_Cabina.xlsx")

    df.to_excel(Escritor, f"Calculo {Grupo}", index=False)

    Escritor.save()


Carga(1, de.iloc[1, 0])
Carga(2, de.iloc[2, 0])
Carga(3, de.iloc[3, 0])
Carga(4, de.iloc[4, 0])

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





