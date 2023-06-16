#Cálculo de motor y caja de cambios:

'''
4. Considerando una caja de cambio mecánica, con un 80% de eficiencia que reduce
la velocidad del motor a la de la polea del ascensor.

6. Calculando el motor eléctrico con un 90% de eficiencia que gira a 3600RPM.
'''
import numpy
import pandas as pd
import sys

filepath = "./datos_ascensores.xlsm"
de = pd.read_excel("datos_ascensores.xls")

def Calculos(fila):

    grupo = de.iloc[fila, 0]
    M_Cabina = de.iloc[fila, 9]/2 #kg
    M_Contrapeso = de.iloc[fila, 9]*1.5/2 #kg
    Gravedad = 9.8

    Vtan_Polea = de.iloc[fila, 6] #m/s

    Radio_Polea = 0.2


    Vang_Polea = Vtan_Polea/Radio_Polea

    Tension = 4.4*M_Cabina+5.4*M_Contrapeso #N



    Torque_Polea = Tension*Radio_Polea

    Potencia_Polea = Torque_Polea*Vang_Polea

    Potencia_Caja = 10*Potencia_Polea/8
    Potencia_Motor = 10*Potencia_Caja/9

#Torque_Motor = Potencia_Motor*152.069 # 487.5
#Vang_Motor = Potencia_Motor/Torque_Motor

    Nro_Engranes = 376.99/Vang_Polea

    print(f"{grupo} \n")

    print(f"Contrapeso: {M_Contrapeso} kg")
    print(f"Cabina: {M_Cabina} kg")
    print(f"Tension: {Tension}\n")

    print(f"Radio de la polea: {Radio_Polea}")

    print(f"Torque de la polea: {Torque_Polea}\n")

    print(f"Potencia de la polea: {Potencia_Polea}")
    print(f"Potencia de la caja: {Potencia_Caja}")
    print(f"Potencia del motor: {Potencia_Motor}\n")

    print(f"Velocidad angular de la polea: {Vang_Polea}")

    print(f"Nro de engranajes: {Nro_Engranes} => {round(Nro_Engranes)} engranajes \n")

    return grupo, M_Contrapeso, M_Cabina, Tension, Radio_Polea, Torque_Polea, Potencia_Polea, Potencia_Caja, Potencia_Motor, Vang_Polea, round(Nro_Engranes)

def guardar(grp, contrapeso, cabina, tension, radiop, torquep, potenciap, potenciac, potenciam, vangp, engranes):

    df = pd.DataFrame({"Grupo" : [grp],
                       "Contrapeso": [contrapeso],
                       "Cabina" : [cabina],
                       "Tension" : [tension],
                       "Radio polea" : [radiop],
                       "Torque polea" : [torquep],
                       "Potencia polea" : [potenciap],
                       "Potencia caja" : [potenciac],
                       "Potencia motor" : [potenciam],
                       "Vel ang polea" : [vangp],
                       "Nro engranes" : [engranes]})
    
    df = df[["Grupo",
             "Contrapeso",
             "Cabina",
             "Tension",
             "Radio polea",
             "Torque polea",
             "Potencia polea",
             "Potencia caja",
             "Potencia motor",
             "Vel ang polea",
             "Nro engranes"]]
    
    Escritor = pd.ExcelWriter(".\\Caja_Motor.xlsx")

    df.to_excel(Escritor, f"Calculo {grp}", index=False)

    Escritor._save()

grpa, contrapesoa, cabinaa, tensiona, radiopa, torquepa, potenciapa, potenciaca, potenciama, vangpa, engranesa = Calculos(1)
guardar(grpa, contrapesoa, cabinaa, tensiona, radiopa, torquepa, potenciapa, potenciaca, potenciama, vangpa, engranesa)

grpB, contrapesoB, cabinaB, tensionB, radiopB, torquepB, potenciapB, potenciacB, potenciamB, vangpB, engranesB = Calculos(2)
guardar(grpB, contrapesoB, cabinaB, tensionB, radiopB, torquepB, potenciapB, potenciacB, potenciamB, vangpB, engranesB)

grpC, contrapesoC, cabinaC, tensionC, radiopC, torquepC, potenciapC, potenciacC, potenciamC, vangpC, engranesC = Calculos(3)
guardar(grpC, contrapesoC, cabinaC, tensionC, radiopC, torquepC, potenciapC, potenciacC, potenciamC, vangpC, engranesC)

grpD, contrapesoD, cabinaD, tensionD, radiopD, torquepD, potenciapD, potenciacD, potenciamD, vangpD, engranesD = Calculos(4)
guardar(grpD, contrapesoD, cabinaD, tensionD, radiopD, torquepD, potenciapD, potenciacD, potenciamD, vangpD, engranesD)