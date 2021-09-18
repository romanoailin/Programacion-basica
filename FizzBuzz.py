entero = 13
NUMERO1 = 2
NUMERO2 = 4 

if (entero &NUMERO1 == 0) and (entero %NUMERO2 == 0):
    print ('FizzBuzz')
elif (entero % 2 == 0):
    print ('FizzBozz')
else:
    print ('FizzBazz')




tupla = ("Vos", "Yo")
#No puedo agregar o quitar valores
lista = ["Juan", "Maria", "Pedro", "Sofia", type(tupla), len(tupla)]
#Puedo añadir o quitar valores. Actualizar


for valor in lista:
    print(valor)

print(type(range(5)))

for key, valor in enumerate(lista):
    print(key, " =>", valor)