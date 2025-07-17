#Aqui se hará un codigo de una calculadora en donde, para poder ser utilizada tendrá que iniciar sesion.
#developer 2 tendrá la tarea de hacer una funcion para iniciar sesion.
#Developer 1 tendrá la tarea de hacer una calculadora funcional.

def login():
    users = {123: "juan", 456: "pedro", 789: "maria"}
    userLogin = int(input("Introduce tu contraseña\n"))
    if userLogin in users:
        return print(f"Bienvenid@ {users[userLogin]}")
    else:
        return print("Incorrecto")
