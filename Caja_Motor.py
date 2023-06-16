#Cálculo de motor y caja de cambios:

'''
4. Considerando una caja de cambio mecánica, con un 80% de eficiencia que reduce
la velocidad del motor a la de la polea del ascensor.

6. Calculando el motor eléctrico con un 90% de eficiencia que gira a 3600RPM.
'''
import numpy

M_Cabina = 450 #kg
M_Contrapeso = 1350 #kg
Gravedad = 9.8

Vtan_Polea = 10 #m/s

Radio_Polea = 0.2

Vang_Polea = Vtan_Polea/Radio_Polea

Tension_1 = M_Cabina*Gravedad #N
Tension_2 = M_Contrapeso*Gravedad #N


Torque_Polea = Tension_1*Radio_Polea

Potencia_Polea = Torque_Polea*Vang_Polea

Potencia_Caja = 10*Potencia_Polea/8
Potencia_Motor = 10*Potencia_Caja/9

Torque_Motor = 162.5
Vang_Motor = Potencia_Motor/Torque_Motor

Nro_Engranes = Vang_Motor/Vang_Polea

print(f"Tension 1: {Tension_1}")
print(f"Tension 2: {Tension_2}\n")

print(f"Radio de la polea: {Radio_Polea}")
print(f"Torque de la polea: {Torque_Polea}\n")

print(f"Potencia de la polea: {Potencia_Polea}")
print(f"Potencia de la caja: {Potencia_Caja}")
print(f"Potencia del motor: {Potencia_Motor}\n")

print(f"Velocidad angular de la polea: {Vang_Polea}")
print(f"Velocidad angular del motor: {Vang_Motor} [rad/s] (377)\n")

print(f"Nro de engranajes: {Nro_Engranes}")