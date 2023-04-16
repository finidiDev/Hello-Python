# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (41,1.82,"Hola Python",True)
my_other_tuple=(1,2,3,4,5,6,7,8,9,10)
print(my_tuple) # (41, 1.82, 'Hola Python', True)
print(type(my_tuple)) # <class 'tuple'>
print(my_tuple[2]) # Hola Python
print(my_tuple[-1]) # True
print(my_tuple.count(41)) # 1
print(my_tuple.count(1)) # 0
print(my_tuple.index(1.82)) # 1

# my_tuple[0] = 1 # TypeError: 'tuple' object does not support item assignment
my_sum_typle= my_tuple + my_other_tuple
print(my_sum_typle) # (41, 1.82, 'Hola Python', True, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

my_tuple_to_list = list(my_tuple)
print(my_tuple_to_list) # [41, 1.82, 'Hola Python', True]

del my_tuple # Elimina la tupla
# print(my_tuple) # NameError: name 'my_tuple' is not defined