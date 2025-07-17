#Aqui se hará un codigo de una calculadora en donde, para poder ser utilizada tendrá que iniciar sesion.
#developer 2 tendrá la tarea de hacer una funcion para iniciar sesion.
#Developer 1 tendrá la tarea de hacer una calculadora funcional.

def login():
    users = ["juan", "pedro", "lucas"]
    passwords = [123, 456, 789]
    userLogin = input("Introduce tu nombre de usuario\n")
    passLogin = int(input("Introduce tu contraseña\n"))
    if userLogin in users and passLogin in passwords:
        return print(f"Bienvenido {userLogin}")
    else:
        return print("Incorrecto")

login()