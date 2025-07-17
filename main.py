#El developer 1 estará haciendo la funcion de la calculadora

def calculator():
    op = int(input("Qué operacion deseas hacer?\n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n"))
    x = int(input("Introduce el primer número\n"))
    y = int(input("Introduce el segundo número\n"))
    if op == 1:
        print(f"El resultado es {x + y}")
    elif op == 2:
            print(f"El resultado es {x - y}")
    elif op == 3:
        print(f"El resultado es {x * y}")
    elif op == 4:
        print(f"El resultado es {x / y}")

calculator()