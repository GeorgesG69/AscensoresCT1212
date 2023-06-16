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

Radio_Polea = 0

Vang_Polea = Vtan_Polea/Radio_Polea

Tension_1 = M_Cabina*Gravedad #N
Tension_2 = M_Contrapeso*Gravedad #N


Torque_Polea = Tension_2*Radio_Polea
Potencia_Polea = Torque_Polea*Vang_Polea

print(f"Tension 1: {Tension_1}")
print(f"Tension 2: {Tension_2}")