# Lists

my_list= list()
my_other_list = []

print(type(my_list)) # <class 'list'>
print(type(my_other_list)) # <class 'list'>

print(len(my_list)) # 0

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0]) # 1

my_other_list= [41,1.82,"Hola Python",True]
print(my_other_list) # [41, 1.82, 'Hola Python', True]
print(my_other_list[2]) # Hola Python
print(my_other_list[2][5]) # P
print(my_other_list[2][5:10]) # Pytho
print(my_other_list[-2]) # Hola Python
print (my_other_list.count(41)) # 1
# print(my_other_list[8]) # IndexError: list index out of range

age, height, name, is_married = my_other_list
print(age) # 41
print(height) # 1.82
print(name) # Hola Python
print(is_married) # True

print(my_list + my_other_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 41, 1.82, 'Hola Python', True]
print(my_list * 3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list.append(11) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(my_list)
my_list.insert(0,0) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(my_list)
my_list.extend([12,13,14,15]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(my_list)
my_list.remove(0) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] elimina el valor 0
print(my_list)
my_list.pop() # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(my_list)
my_list.pop(0) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(my_list)
del my_list[0] # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] Elimina por indice, en este caso 0
print(my_list)

my_list.clear() # []
print(my_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list.index(5)) # 4
print(5 in my_list) # True
print(15 in my_list) # False
my_list.reverse() # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(my_list)
my_list.sort() # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
my_list.sort(reverse=True) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(my_list)

my_list[1] = 20 # [10, 20, 8, 7, 6, 5, 4, 3, 2, 1]
print(my_list)
my_list[1:3] = [21,22] # [10, 21, 22, 7, 6, 5, 4, 3, 2, 1]
print(my_list)

my_new_list = my_list.copy() # [10, 21, 22, 7, 6, 5, 4, 3, 2, 1]
print(my_new_list)