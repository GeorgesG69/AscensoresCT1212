#Cálculo de motor y caja de cambios:

'''
4. Considerando una caja de cambio mecánica, con un 80% de eficiencia que reduce
la velocidad del motor a la de la polea del ascensor.

6. Calculando el motor eléctrico con un 90% de eficiencia que gira a 3600RPM.
'''
import numpy

RPM_Motor = 3600

Velocidad_Tangencial_Polea = 10 #m/s

Velocidad_Angular_Motor = 3600*2*numpy.pi/60

Radio_Polea = 2 #m

Velocidad_Angular_Polea = Velocidad_Tangencial_Polea/Radio_Polea

Factor_Reduccion = Velocidad_Angular_Motor/Velocidad_Angular_Polea


# Cálculo de la caja de cambios:

Velocidad_Salida = Velocidad_Angular_Polea - Velocidad_Angular_Polea/Factor_Reduccion

Nro_Engranajes = 0

print(f"RPM = {RPM_Motor} [rpm]")
print(f"Vtan polea = {Velocidad_Tangencial_Polea} [m/s]")
print(f"Velocidad angular de la polea = {Velocidad_Angular_Polea} [rad/s]")
print(f"Vang motor= {Velocidad_Angular_Motor} [rad/s]\n")

print(f"Radio de la polea = {Radio_Polea} [m]\n")
print(f"Factor de reducción = {Factor_Reduccion} veces")

print(f"Velocidad de Salida = {Velocidad_Salida} [m/s]")
print(f"Número de engranajes = {Nro_Engranajes}\n")