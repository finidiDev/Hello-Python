# Loops

#While loop
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Fin del ciclo while")
print("Fin del programa")

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
    if my_condition == 5:
        break
print("Fin del programa")

#For loop
my_list = [1,2,3,4,5,6,7,8,9,10]
for item in my_list:
    print(item)
else:
    print("Fin del ciclo for")
print("Fin del programa")

my_string = "Hola Mundo"
for item in my_string:
    print(item)
else:
    print("Fin del ciclo for")
print("Fin del programa")

my_list = [(1,2),(3,4),(5,6),(7,8)]
for item in my_list:
    print(item)
else:
    print("Fin del ciclo for")
print("Fin del programa")

for a,b in my_list:
    print(a)
    print(b)
else:
    print("Fin del ciclo for")
print("Fin del programa")

for item in my_list:
    print(item)
    if item[0] == 3:
        break
else:
    print("Fin del ciclo for")
print("Fin del programa")