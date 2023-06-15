#Cálculo de motor y caja de cambios:

'''
4. Considerando una caja de cambio mecánica, con un 80% de eficiencia que reduce
la velocidad del motor a la de la polea del ascensor.

6. Calculando el motor eléctrico con un 90% de eficiencia que gira a 3600RPM.
'''
import numpy

RPM_Motor = 3600

Velocidad_Tangencial = 10 #m/s

Velocidad_Angular = 3600*2*numpy.pi/60

Radio_Ideal = Velocidad_Tangencial/Velocidad_Angular


# Cálculo de la caja de cambios:

RPM_Salida = RPM_Motor - RPM_Motor*2/10

Nro_Engranajes = RPM_Motor/RPM_Salida

print(f"RPM = {RPM_Motor} [rpm]")
print(f"Vtan = {Velocidad_Tangencial} [m/s]")
print(f"Vang = {Velocidad_Angular} [rad/s]\n")

print(f"Radio ideal = {Radio_Ideal} [m]\n")

print(f"RPM de Salida = {RPM_Salida} [rpm]")
print(f"Número de engranajes = {Nro_Engranajes}\n")