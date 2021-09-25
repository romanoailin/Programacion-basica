'''empanadas = ('jyq','capresse','carne','pollo')
pizzas = ('napolitana','fugazzeta','calabresa')
pastas = ('ravioles', 'spaguetti', 'canelones')
pedidosDeComida = ('empanadas','pizzas','pastas')


def contar_tuplas(pedidosDeComida):
    return (len(pedidosDeComida), len(empanadas,pizzas,pastas))

print(contar_tuplas)'''

def contar_tuplas(tuplas):
    contador = 0

    for tupla in tuplas:
        contador +=  len(tupla)

    tuplaReturn = (len(tuplas), contador)
    

    return tuplaReturn

valoresTuplas = (
    (1,2,3),
    (3.4,9),
    (0,5)
)

if __name__ == "__main__":
    print("tupla resultado")
    print(contar_tuplas(valoresTuplas))