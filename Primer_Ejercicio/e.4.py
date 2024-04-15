# Ejercicios Nro 1
# Instrucciones : 
#           crear un repositorio en github  (de forma publica , revisar video parte inicial de la grabacion)
#           realizar un archivo por problema 
#           trabajarlo en local y subir los archivos o trabajarlo por codespace

# 4.Realizar un programa que permita saber si un usario puede obtener un tarjeta de credito
#condiciones : ser mayor de 18 años , un ingreso mensual de 1000 soles mensual.
#               si cumple con las 2 condiciones imprimir que tipo de tarjeta puede obtener
#                 si su ingreso mensual es de 1000 hasta 3000 soles es tarjeta de clasica , mayor a ello tarjeta dorada.

Consulta= int(input('Ingresa tu edad: '))
consulta_2=int(input('ingresa el ingreso mensual que percibes: '))

if Consulta < 18: 
        print ('No puedes acceder a una tarjeta por ser menor de edad')
elif consulta_2 < 1000:
        print ('No puedes acceder a una tarjeta por POBRE')
elif consulta_2 >=1000 and consulta_2<3000:
        print ('Accedes a una tarjeta de tipo Clásica')
elif consulta_2 >=3000:
        print('¡Felicidades!, calificas para una tarjeta de tipo Dorada')
else: 
        print ('ERROR AL COLOCAR LOS DATOS, INTENTE DE NUEVO')
