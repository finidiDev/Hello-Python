# Strings
my_string = "Hola Python"
my_other_string = 'Hola otro Python'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Hola Python\nHola otro Python con salto de linea"
print(my_new_line_string)
my_tab_string = "Hola Python\tHola otro Python con tabulacion"
print(my_tab_string)
my_scaped_string = "Hola Python\\Hola otro Python con barra invertida"
print(my_scaped_string)

# Formateo de strings
my_name,my_surname,age="Juan","Perez",35
print("Hola %s %s, tienes %d años" % (my_name,my_surname,age)) # %s para string, %d para int, %f para float, %r para raw, %x para hex , %o para octal
print("Hola {} {}, tienes {} años".format(my_name,my_surname,age))  # .format
print(f"Hola {my_name} {my_surname}, tienes {age} años") # f-strings
print("Hola {1} {0}, tienes {2} años".format(my_name,my_surname,age)) # .format con indices

# desempaquetado de strings
language="Python"
a,b,c,d,e,f=language
print(a,b,c)
print(d,e,f)

# dividir strings
language_slice = language[0:3]
print(language_slice)
language_slice = language[:3] # desde el indice 0 hasta el 3
print(language_slice)
language_slice = language[3:] # desde el indice 3 hasta el final
print(language_slice)
language_slice = language[::2] # saltos de 2 en 2
print(language_slice)
language_slice = language[::-1] # invertir strings
print(language_slice)
language_slice = language[::-2] # invertir strings y saltos de 2 en 2
print(language_slice)
language_slice= language[1:6:2] # desde el indice 1 hasta el 6 con saltos de 2 en 2
print(language_slice)

# Funciones de strings
print(language.upper()) # mayusculas
print(language.lower()) # minusculas
print(language.capitalize()) # primera letra en mayuscula
print(language.title()) # primera letra de cada palabra en mayuscula
print(language.swapcase()) # intercambia mayusculas por minusculas y viceversa
print(language.count("P")) # cuenta cuantas veces aparece la letra P
print(language.isnumeric()) # verifica si es numerico
print(language.isalpha()) # verifica si es alfabetico
