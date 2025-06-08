#Ejemplos de practica día dos

# Variables (tipos de variables)

my_string_variable = "My String Variable"
#print(my_string_variable)

my_int_variable = 5
#print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
#print(my_int_to_str_variable)
#print(type(my_int_to_str_variable))

my_bool_variable = False
#print(my_bool_variable)

# Ejemplo 2 (Aplicación de variables)
first_name = "Luis"
last_name = "Ornelas"
country = "México"
age = 28
is_married = False
skills = ["HTML", "CSS", "LINUX", "CONTPAQi"]
person_info= {
    'firstname' : 'Enrique',
    'lastname' : 'Maciel'
}


#Print tradicional
print(first_name)

#Print puede recibir varios argumentos
print("Mi nombre es:", first_name, last_name, "Mi edad es:", age, "años", "Vivo en:", country)

#Print con función len()
#len() cuenta con el número de caracteres que tiene una cadena de texto
print(len(first_name)) 


#Imprimiendo todas los datos que se tienen en las variables
print("Mi nombre es:", first_name)
print("Mi apellido es:", last_name)
print("Vivo en el país de:", country)
print("Tengo", age, "años")
print("Casado", is_married)
print("Habilidades:", skills)
print("Información personal:", person_info)


#Asignando variables con los datos ingresados por el usuario
#Se usuara la función input() para leer lo que escriba el usuario

first_name = input('¿Cuál es tu nombre?')
last_name = input('¿Cuál es tu apellido?')
age = input('¿Cuál es tu edad?')

print ("Información ingresada por el usuario:", first_name, last_name, 'tiene', age, 'años')



#Variables con diferentes tipos de datos en Python

first_name = "Luis"
last_name = "Enrique"
age = 28
is_married = False

print(type(first_name))     # srt (String)
print(type(last_name))      # srt (String)
print(type(age))            # int (Entero)
print(type(is_married))     # boolean (Booleano)
print(type(10.4))           # float (flotante = decimales)
print(type(1 + 1j))         # Complex
print(type([1,2,3,4,5]))    # [] <-- los corchetes nos indican que son listas
print(type({"name":"Luis", "last":"Ornelas"})) # {} <-- mientras que las llaves indian que es un diccionario
print(type((1,2)))          # tuple (tupla)
print(type(zip([1,2],[3,4])))   # set 
"""
"""
# Conversión de tipo de datos  int() , float() , str() , list()
# int a float 
int_num = 10
print("El número entero es:", int_num)

num_float = float(int_num)
print("El numero decimal es:", num_float)

# float a int
gravity = 9.81
print("La gravedad en decimales es:", gravity)

gravity_int = int(gravity)
print("La gravedad en número entero es:", gravity_int)

# int a str
int_num = 10
print("El número entero es:", int_num)

num_str = str(int_num)
print("El número encadena de texto es:", num_str) # solo se tendría que agregar comillas cuando se imprima

# str a int
num_str = 3.1416
print("El valor de pi con string es:", num_str)

num_int = int(num_str)
print("El valor de pi con int es:", num_int)

float_num = float(num_str)
print("El valor de pi con float es:", float_num)

# str a list
first_name = 'Luis Ornelas'
print(first_name)

first_name_to_list = list(first_name)
print(first_name_to_list)


#EJERCICIO DE PRACTICA
# 1. Día 2: 30 días de programación en Python
# 2 al 13. Declaración de variables
nombre = 'Luis'
apellido = 'Ornelas'
nombre_completo = nombre +' ' + apellido
pais = 'México'
ciudad = 'Morelia'
edad = 28
anio = 2024
es_casado = False
es_verdadero = True
luz_encendida = False
segundo_nombre, segundo_apellido = 'Enrique', 'Maciel'

# 14. Imprimir los tipos de datos con la función type()
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(anio))
print(type(es_casado))
print(type(es_verdadero))
print(type(luz_encendida))
print(type(segundo_nombre))
print(type(segundo_apellido))

# 15. Encontrar la longitud de nombre
print(len(nombre))

# 16. Comparando la longitud de nombre y apellido
# Comparando cadenas
print('¿Las variables tiene la misma longitud?', len(nombre) == len(apellido))

# Comparando con longitud
long_nombre = len(nombre)
long_apellido = len(apellido)

print('La longitud de la variable nombre es:', long_nombre , 'mientras que la longitud de la variable apellido es:', long_apellido)
print('¿Las variables tiene la misma longitud?', long_nombre == long_apellido)

# 17. Declarar dos variables int para realizar operaciones
num_uno = 5
num_dos = 4

# Operaciones con vairables
# Suma
variable_total = num_uno + num_dos
print("El resultado de la suma es:", variable_total)
# Resta
variable_diff = num_dos - num_uno
print("El resultado de la resta es:", variable_diff)
# Multiplicación
variable_product = num_dos * num_uno
print("El resultado de la multiplicación es:", variable_product)
# División
variable_division = num_uno / num_dos
print("El resultado de la división es:", variable_division)
# Elevación de potencia (Elevar alguna potencia se puede utilizar el operador ** o la función pow())
variable_exp = num_uno ** num_dos
print("El resultado de 5 a la potencia 4 es:", variable_exp)
# Divisón con decimales (Divisón de piso se utiliza el operador //)
variable_floor_division = num_uno // num_dos
print("El resultado de la división de piso es:", variable_floor_division)

# 18. Ejercicio con un circulo
# Declarar variables
radio = 30
pi = 3.1416

# Operaciones
# Área su formula es pi * radio al cuadrado
area_of_circle = pi * (radio ** 2)
print("El área del circulo es:", area_of_circle)

# Diametro es dos veces el radio 
circum_of_circle = 2 * radio
print("El diametro del circulo es:", circum_of_circle)

# El usuario ingresa el radio del circulo y se calcula el área
radio2 = input("Ingresa el radío del circulo: ")
area_of_circle2 = pi * (int(radio2) ** 2)
print("El área del circulo del usuario es:", area_of_circle2)

# Variables que el usuario ingresar el valor
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
pais = input("Ingresa tu país: ")
edad = input("Ingresa tu edad: ")
# Imprimir las variables que el usario ingreso por teclado
print("Mi nombre es", nombre, apellido, "vivo en el país de", pais, "y tengo", edad, "años")

help("keywords")