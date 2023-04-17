# Sets
my_set= set() 
my_other_set={}
print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # <class 'dict'>

my_other_set = {41,1.82,"Hola Mundo",True}
print(type(my_other_set)) # <class 'set'>
print(len(my_other_set)) # 4

my_other_set.add(1)
print(my_other_set) # {1, 41, 1.82, 'Hola Mundo', True} # un set no es una estructura ordenada

my_other_set.add(1)
print(my_other_set) # {1, 41, 1.82, 'Hola Mundo', True} # no se pueden agregar elementos repetidos

print (1 in my_other_set) # True
print (2 in my_other_set) # False

my_other_set.remove(41) # elimina el elemento 41
print(my_other_set) # {1.82, 'Hola Mundo', True}

my_other_set.discard(1) # elimina el elemento 1
print(my_other_set) # {1.82, 'Hola Mundo', True}

my_other_set.clear() # elimina todos los elementos del set
print(len(my_other_set)) # 0

del my_other_set # elimina el set
# print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {41,1.82,"Hola Mundo",True}
my_list = list(my_set) # convierte el set en una lista
print(my_list) # [1.82, 41, 'Hola Mundo', True]

my_other_set = {"Kotlin", "Python", "Java"}
my_set.update(my_other_set) # agrega los elementos de my_other_set al set my_set
my_set.union(my_other_set) # agrega los elementos de my_other_set al set my_set

print(my_set.difference (my_other_set)) # {1.82, 41, True} # elementos que están en my_set pero no en my_other_set
print(my_set.intersection(my_other_set)) # {'Kotlin', 'Python', 'Java'} # elementos que están en my_set y en my_other_set
print(my_set.symmetric_difference(my_other_set)) # {1.82, 41, True, 'Kotlin', 'Python', 'Java'} # elementos que están en my_set o en my_other_set pero no en ambos