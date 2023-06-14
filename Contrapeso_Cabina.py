# Determinación de los valores del Contrapeso y la Cabina según la normativa Covenin.

Longitud_Fijacion_Cable = 0

Contrapeso_Pared = 5 + Longitud_Fijacion_Cable*2/1000
Carro_Contrapeso = 7 + Longitud_Fijacion_Cable*2/1000

# Cables:

Valor_T7 = 1

Nro_Cables_Suspencion = 10

Carga_Rotura_Cable = 2000

Peso_Cable = 0.14 + 2000

Factor_Seguridad = Valor_T7*Nro_Cables_Suspencion*Carga_Rotura_Cable/Peso_Cable