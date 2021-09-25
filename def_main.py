def suma(valor1,valor2):
   return valor1 + valor2

def main():
   entrada1= input("valor 1 = ")
   entrada2= input("valor 2 = ")
   resultado = suma(entrada1, entrada2)
   print("resultado de suma es", resultado)

#con la funcion main defino la función principal de mi programa, de todo mi programa, sin tener en cuenta las demás funciones adicionales. 
#instancia un objeto entero

if __name__ == "__main__":
    main() 