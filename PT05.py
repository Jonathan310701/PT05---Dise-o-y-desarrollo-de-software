import math

def suma_numeros():
    n = int(input("Ingrese la cantidad de numeros a sumar: "))
    numeros = [float(input("Ingrese el número {}: ".format(i + 1))) for i in range(n)]
    resultado = sum(numeros)
    print("La suma de los numeros es:", resultado)

def producto_numeros():
    n = int(input("Ingrese la cantidad de numeros a multiplicar: "))
    numeros = [float(input("Ingrese el numero {}: ".format(i + 1))) for i in range(n)]
    resultado = 1
    for num in numeros:
        resultado *= num
    print("El producto de los numeros es:", resultado)

def division_numeros():
    num1 = float(input("Ingrese el numerador: "))
    num2 = float(input("Ingrese el denominador: "))
    if num2 != 0:
        resultado = num1 / num2
        print("La division es:", resultado)
    else:
        print("No se puede dividir entre cero.")

def calcular_factorial():
    n = int(input("Ingrese un numero para calcular su factorial: "))
    resultado = math.factorial(n)
    print("El factorial de {} es: {}".format(n, resultado))

def imprimir_tabla_multiplicar():
    num = int(input("Ingrese un numero para ver su tabla de multiplicar (del 1 al 10): "))
    for i in range(1, 11):
        print("{} x {} = {}".format(num, i, num * i))

def calcular_cuadrado_y_cubo():
    num = float(input("Ingrese un numero para calcular su cuadrado y cubo: "))
    cuadrado = num ** 2
    cubo = num ** 3
    print("El cuadrado de {} es: {}".format(num, cuadrado))
    print("El cubo de {} es: {}".format(num, cubo))

def calcular_promedio():
    numeros = []
    while True:
        num = float(input("Ingrese un numero (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    if len(numeros) > 0:
        promedio = sum(numeros) / len(numeros)
        print("El promedio de los numeros es:", promedio)
    else:
        print("No se ingresaron numeros.")

def encontrar_maximo_y_minimo():
    n = int(input("Ingrese la cantidad de numeros enteros a comparar: "))
    numeros = [int(input("Ingrese el número {}: ".format(i + 1))) for i in range(n)]
    if len(numeros) > 0:
        maximo = max(numeros)
        minimo = min(numeros)
        print("El valor maximo es:", maximo)
        print("El valor minimo es:", minimo)
        print("Total de valores ingresados:", len(numeros))
    else:
        print("No se ingresaron numeros.")

def menu():
    while True:
        print("\nMenu de opciones:")
        print("1. Suma de numeros")
        print("2. Producto de numeros")
        print("3. Division de dos numeros")
        print("4. Calcular factorial")
        print("5. Imprimir tabla de multiplicar")
        print("6. Calcular cuadrado y cubo")
        print("7. Calcular promedio")
        print("8. Encontrar maximo y minimo")
        print("9. Salir")

        opcion = int(input("Seleccione una opcion (1-9): "))

        if opcion == 1:
            suma_numeros()
        elif opcion == 2:
            producto_numeros()
        elif opcion == 3:
            division_numeros()
        elif opcion == 4:
            calcular_factorial()
        elif opcion == 5:
            imprimir_tabla_multiplicar()
        elif opcion == 6:
            calcular_cuadrado_y_cubo()
        elif opcion == 7:
            calcular_promedio()
        elif opcion == 8:
            encontrar_maximo_y_minimo()
        elif opcion == 9:
            print("'¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del 1 al 9.")

if __name__ == "__main__":
    menu()
