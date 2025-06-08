"""
#Ejemplos de boleanos simples, impresión
print(True)
print(False)

#Ejemplos de números enteros
print('Suma: ', 1 + 2)
print('Resta: ', 2 - 1)
print('Multiplicación: ', 2 * 3)
print('División: ', 4 / 2) #El resultado tiene números flotantes
print('División: ', 6 / 2)
print('División: ', 7 / 2)
print('División sin decimales: ', 8 // 3) #Esta operación regresa un resultado sin decimalees en el resultado.
print('Modulo: ', 3 % 2) #Esta operación solo regresa el residuo de la operación
print('Elevación: ', 3 ** 3), '\n' # Esta operación, eleva el número a la potencia que se le coloque

# Ejemplos de número flotantes
print('Valor flotante: PI', 3.1416)
print('Valor flotante: Gravedad: ', 9.81, '\n')

# Ejemplp de números complejos
print('Número complejo: ', 1 + 1j)
print('Multiplicación de número complejo: ', (3 + 2j) * (3 - 2j), '\n')

# Ejemplo con variables y operadores.
# Delcaración de variables
num1 = 3 # num1 es la variables, mientras que 3 es el tipo de dato
num2 = 2 # num2 es la variables, mientras que 3 es el tipo de dato

# Operaciones con las variables
suma =  num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
residuo = num1 % num2
division_piso = num1 // num2
exponencial = num2 ** num1

#Imprimir el resultado de las operaciones aritmeticas

print('La suma de; ', num1, ' + ', num2, 'es: ', suma)
print('La resta de; ', num1, ' - ', num2, 'es: ', resta)
print('La multiplicación de; ', num1, ' * ', num2, 'es: ', multiplicacion)
print('La divisón de; ', num1, ' / ', num2, 'es: ', division)
print('El residuo de; ', num1, ' % ', num2, 'es: ', residuo)
print('La divisón de piso de; ', num1, ' // ', num2, 'es: ', division_piso)
print('El número', num2, ' Elevado a la potencia ', num1, 'es: ', exponencial, '\n')

# Prácticando y conectando puntos de lo aprendido para calcular (área, volumen, peso, perímetro, distancia y fuerza)
# Calcular el área de un circula

pi = 3.1416                                       # Se declara la variable PI y se le asigna una valor fijo
radio = input('Ingresa el radío del cirulo: ')    # Se pide al usuari que ingrese el radio del circulo

# Calcular área del circulo
area_circulo = pi * (int(radio) ** 2)             # Elevamos la variable radio al cuadrado y se pultiplica por la variable PI
print('El área del circulo es: ', area_circulo, '\n')

# Calcular el área de un rectangulo
base = input('Ingresa la base del rectangulo: ')
altura = input('Ingresa la altura del triangulo: ')

area_rectangulo = int(base) * int(altura)
print('El área del rectangulo es: ', area_rectangulo, '\n')

# Calcular el peso de un objeto

masa = input('Ingresa la pasa del objeto: ')
gravedad = 8.91

peso =  int(masa) * gravedad
print('El peso dle objeto es: ', peso, '\n')

# OPERADORES DE COMPARACIÓN
print(3 >= 2)    # True, porque 3 es más grande que 2
print(3 < 2)     # False,  porque 3 es más grande que 2
print(2 < 3)     # True, porque 2 es más chico que 3
print(2 <= 3)    # True, porque 2 es más chico que 3
print(3 == 2)    # False, porque 3 no es igual a 2
print(3 != 2)    # True, porque 3 no es igual a 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparar algo da verdadero o falso

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

print('1 is 1', 1 is 1)                   # True - Porque los calores de los datos son los mismos
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - Se encontro A mayúsculas en la palabra
print('B in Asabeneh', 'B' in 'Asabeneh') # False - No hay B mayúsculas
print('coding' in 'coding for all') # True - Porque coding for all tiene la palabra coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# OPERADORES LOGICOS

print(3 > 2 and 4 > 3) # True - porque ambas afirmaciones son ciertas
print(3 > 2 and 4 < 3) # False - Porque la segunda afirmación es falsa
print(3 < 2 and 4 < 3) # False - Porque ambas afirmación son falsas
print(3 > 2 or 4 > 3)  # True - porque ambas afirmaciones son ciertas
print(3 > 2 or 4 < 3)  # True - porque una de las afirmaciones es cierta
print(3 < 2 or 4 < 3)  # False -  Porque ambas afirmación son falsas
print(not 3 > 2)     # False - porque 3 > 2 es verdadero, entonces no es verdadero y da falso
print(not True)      # False - negación, entonces la operación no se devuelve verdadera, sino falta
print(not False)     # True
print(not not True)  # True
print(not not False) # False
"""
"""
# EJERICIOS PRÁCTICOS
# 1. Declarar edad variable entera
edad = 28
print('La edad de Enrique es:', edad, '\n')

# 2. Declarar estatura variable flotante
estatura = 1.73
print('La estatura de Enrique es: ', estatura, '\n')

# 3. Declarar variable compleja
v_compleja = 1 + 1j
print('La variable compleja tien el valor: ', v_compleja)

# 4. Escriba un script que solicite al usuario que ingrese la base y
#la altura del triángulo y calcule el área de este triángulo (area = (b x h)/2)

base = input('Ingresa la base del triangulo: ')
altura = input('Ingresa la altura del triangulo: ')

area = (int(base) * int(altura)) / 2

print('El área del trinagulo es: ', area, '\n')

# 05. Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo.
# Calcula el perímetro del triángulo (perímetro = a + b + c).

input('Vamos a calcular el perimero de un triángulo, presiona cualquier tecla para continuar')

lado_a = input('Ingresa el largo del lado a: ')
lado_b = input('Ingresa el largo del lado b: ')
lado_c = input('Ingresa el largo del lado c: ')

perimetro = int(lado_a) + int(lado_b) + int(lado_c)

print('El perimetro del triángulo es: ', perimetro, '\n')

#input('Felicidades calculaste el perimero de un triángulo, presiona cualquier tecla para salir')

# 06. Obtenga el largo y el ancho de un rectángulo usando el mensaje.
# Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))

input('Vamos a calcular el área y prerímetro de un rectángulo, ingresa los valores que se solicitan')
input('Presiona enter para continuar')
print('\n')

# Obteniendo los datos para el calculo
largo = input('Ingresa el largo del rectangulo: ')
ancho = input('Ingresa el ancho del rectangulo: ')

# Calculando el área del rectángulo
area_rec = (int(largo) * int(ancho))

# Calculo del perímetro
perimetro_rec = 2 * (int(largo) + int(ancho))

# Imprimiendo los resultados
print('El área del rectángulo es: ', area_rec, '\n')
print('El perímetro del rectángulo es: ', perimetro_rec, '\n')

#input('Presiona cualquier tecla para salir')

# 07. Obtenga el radio de un círculo usando el mensaje.
# Calcula el área (área = pi xrxr) y la circunferencia (c = 2 x pi xr) donde pi = 3,14.

input('Vamos a calcular el área y la circunferencia de un círculo, ingresa los valores que se solicitan')
input('Presiona enter para continuar')
print('\n')

pi = 3.14

# Obteniendo los datos para el calculo
radio = input('Ingresa el radio del círculo: ')

# Calculando el área del círculo
area_cir = (pi * int(radio) ** 2)

# Calculo de la círcunferencia
circunferencia_cir = (2 * pi) * int(radio)

# Imprimiendo los resultados
print('El área del círculo es: ', area_cir, '\n')
print('La círcunferencia del círculo es: ', circunferencia_cir, '\n')

#input('Presiona cualquier tecla para salir')

# Calcula la pendiente, la intersección x y la intersección y de y = 2x -2
# Se declaran las variables de los puntos de la intersección

x1 = float (input("Introduzca la coordenada de x1: \n"))
y1 = float (input("Introduzca la coordenada de y1: \n"))
x2 = float (input("Introduzca la coordenada de x2: \n"))
y2 = float (input("Introduzca la coordenada de y2: \n")) 

pendiente1=float((y2-y1)/(x2-x1))

print("La pendiente es:", pendiente1, "\n")
input("Presiona cualquier tecla para continuar...")

# La pendiente es (m = y2-y1/x2-x1). Halla la pendiente entre el punto (2, 2) y el punto (6, 10).

a1 = 2
b1 = 2
a2 = 6
b2 = 10

pendiente2 = float((b2-b1)/(a2-a1))

print("La pendiente2 es: ", pendiente2, "\n")
input("Pulsar cualquier tecla para salir...")

# Compare las pendientes en las tareas 8 y 9.
mayorq = (pendiente2 > pendiente1)
print("La pendiente1 es mayor a la pendiente2: ", mayorq, "\n")

menorq = (pendiente2 < pendiente1)
print("La pendiente1 es menor a la pendiente2: ", mayorq, "\n")
input("Presiona cualquier tecla para salir...")

# Encuentra la longitud de 'python' y 'jargon' y haz una declaración de comparación falsa.
print(len('Python'))
print(len('Jargon'))
print(len('python') != len('jargon'))
input("Pulsa cualquier tecla para salir... \n")

# Utilice el operador and para comprobar si 'on' se encuentra tanto en 'python' como en 'jargon'
print('on' in 'Python' and 'on' in 'Jargon')
input("Pulsa cualquier tecla para salir...")

# Espero que este curso no esté lleno de jerga . Utilice el operador in para comprobar si hay jerga en la oración.

print('jerga' in 'Espero que este curso no esté lleno de jerga')
input('Pulsa culauqier tecla para salir...')

# No hay "on" tanto en dragon como en python
print('on' is not 'Python')
print('on' is not 'Dragon')
input('Pulsa cualquier tecla para salir...')

# Encuentra la longitud del texto de Python y convierte el valor a flotante y conviértelo en cadena
print(str(len('Python')))
"""
# Los números pares son divisibles por 2 y el resto es cero. ¿Cómo comprobar si un número es par o no con Python?
numdefinir= int(input('Ingresa el numero a verificar: \n'))

# Dividir el numero entre 2 para saber si es par
par = (numdefinir)/2

# Comprobación
comprobar = float(par * 2)

if comprobar == numdefinir:
    print('El número es par')
else:
    print('El número es impar')

print(numdefinir)
print(par)
print(comprobar)

input('Presiona cualquier tecla para salir...')

# La división del piso de 7 por 3 es igual al valor int convertido de 2,7.
dpiso = 7//3

print('El resultado de la división de piso es: ', dpiso)

resp= float(2.7)
resp_dpiso = int(resp)
print('La conversión de decimal a entero es: ', resp_dpiso, '\n')

input('Presiona cualquier tecla para salir...')