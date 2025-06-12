# GENERADOR DE PERFIL
#Solicitando información al usuario

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
estatura = input("¿Cuál es tu estatura (m)? ")
estudio = input("¿Estudias? ")

print("¡Bienvenido " , nombre , "!")
print("Usuario: ", nombre)
print("Edad: ", int(edad))
print("Estatura (m): ", float(estatura))
print("Estudias: ", bool(estudio))

print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(estudio))