# Condicionales

my_condition = True

if my_condition:
    print("my_condition es verdadero")
else:
    print("my_condition es falso")

my_condition= 5*2
if my_condition == 10:
    print("my_condition es igual a 10")
elif my_condition > 10:
    print("my_condition es mayor que 10")
else:
    print("my_condition es menor que 10")

if my_condition > 1 and my_condition < 11:
    print("my_condition está entre 1 y 11")
elif my_condition > 10 and my_condition < 21:
    print("my_condition está entre 10 y 21")
else:
    print("my_condition no está entre 1 y 21")  

my_string=""
if my_string:
    print("my_string no está vacío")
else:
    print("my_string está vacío")

print("Fin del programa")