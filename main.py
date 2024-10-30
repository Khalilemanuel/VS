#questão1

metros= int(input("digite um valor em metros"))

resultado= metros*100

print(resultado, "cm")

#questão2

numero = int(input("digite o número desejado"))

percentual = int(input("digite a porcentagem"))


print(numero * (percentual / 100) , (" resultado"))


#questão3

dias = int(input ("digite a quantidade de dias "))
horas = int(input ("digite a quantidade de horas "))
minutos = int(input ("digite a quantidade de minutos "))

print((dias * 24 * 60) + (horas * 60) + minutos, ("soma total em munutos"))

#questão4
numero = int(input("digite um numero para saber se é negativo, \npositivo ou neutro"))

if numero > 0:
  print("o numero é positivo")

elif numero < 0:
  print("o numero é negativo")

else:
  print("o numero é neutro")

#questão5

numero1 = int(input("digite um número"))
numero2 = int(input("digite outro número"))
numero3 = int(input("digite mais um número"))

if numero1 > numero2 and numero1 > numero3:
  print(numero1, "é o maior")

elif numero2 > numero1 and numero2 > numero3:
  print(numero2, "é o maior")

else:
  print(numero3, "é o maior")
