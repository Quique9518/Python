# CALCULADORA DE CALORÍAS con varibale de valor fijo
calorias_burger = 540
calporminuto = 5

# Solcita información
cant_burgers = input("¿Cuantas hambuerguesas te comiste el día de hoy? ")
min_ejercicio = input("¿Cuantos minutos hiciste de ejercicio? ")


# Cálculo de calorías
calorias_ingeridas = calorias_burger * int(cant_burgers)
calorias_quemadas =  calporminuto * int(min_ejercicio)

saldo_calorico = float(calorias_ingeridas) - float(calorias_quemadas)

#Información.
print("Las calorías consumidas el día de hoy fueron: ", float(calorias_ingeridas))
print("Las calorías quemadas el día de hoy fueron: ", float(calorias_quemadas))

if(saldo_calorico > 50 ):
   
   print("Tú saldo calorico es de: ", saldo_calorico)
   print("Tienes un super hábito")
   
else:
       
       print("Tú saldo calorico es de: ", saldo_calorico)
       print("Aún no tienes un super hábito")