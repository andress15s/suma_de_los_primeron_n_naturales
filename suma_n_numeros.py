print("-------------------------------------------")
print("-------suma N primeros naturales-----------")
print("-------------------------------------------")

#entrada
N = input("digite la cantidad de numeros a sumar: ")
N = int(N)

#PROCESAMIENTO 
suma = 0 
i = 1

while i <=N:
  print("suma = " + str(suma))
  suma = suma + i
  print("1 = " + str(i))
  i = i + 1

#SALIDA
print("la suma de los " + str(N) + " primeros numeros naturales es " + str(suma))
print("eso era... fin...")