Usuario = "Diego"
Clave = "234789"

user = input("Usuario: ")
password = input("Contraseña: ")

if user == Usuario and password == Clave:
    print("Acceso permitido")
else:
    print("Acceso denegado")
