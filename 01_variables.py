#Variables
my_string_variable="My string variable"
print(my_string_variable)

my_int_variable=1
print(my_int_variable)

my_bool_variable=True
print(my_bool_variable)

# Concatenación de variables de diferentes tipos en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print("Este es el valor de:", my_bool_variable)


my_int_to_string_variable=str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

# Algunas Funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea
name,surname,age="Juan","Perez",30
print(name,surname,"y mi edad es ",age)

#first_name= input("Ingrese su nombre: ")
#age = input("Ingrese su edad: ")
#print("Su nombre es: ",first_name)
#print("Su edad es: ",age) 

# Cambiamos el tipo de variable
age = "Gorka"
first_name=41
print(first_name)
print(age) 

# Forzar el tipo de variable
address : str = "Calle 123"
address : int = 123
print(type(address))