# Ejercicios Nro 1
# Instrucciones : 
#           crear un repositorio en github  (de forma publica , revisar video parte inicial de la grabacion)
#           realizar un archivo por problema 
#           trabajarlo en local y subir los archivos o trabajarlo por codespace

# 3. Realice un programa que calcule la suma de los numeros hasta el valor ingresado. Ejemplo : Si ingresa 5 se tendra que calcular 1+2+3+4+5

#EJERCICIO 3

#Ingrese un número
valor = int(input("Ingrese un número: "))
# Inicializar la variable para almacenar la suma
suma_1 = 0
# Rango
for sumandos in range(1, valor+1):
    suma =suma_1 + sumandos
# Imprimir la suma
print("La suma de los números desde 1 hasta", valor, "es:", suma)

