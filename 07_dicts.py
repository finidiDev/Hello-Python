# Dicts

my_dict = {} # empty dict
print(type(my_dict)) # <class 'dict'>
my_other_dict = dict() # empty dict
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {"name":"Juan", "age": 20, "height": 1.82, "is_married": False, 1:"Id1", 2: "Id2"}
print(my_other_dict) # {'name': 'Juan', 'age': 20, 'height': 1.82, 'is_married': False, 1: 'Id1', 2: 'Id2'}
print(my_other_dict["name"]) # Juan
print(my_other_dict[1]) # Id1

my_dict = { 
    "lenguajes":{"Python", "Java", "C++"}, 
    "frameworks":{"Django", "Flask", "Spring"} 
    }
print(my_dict) # {'lenguajes': {'Java', 'C++', 'Python'}, 'frameworks': {'Spring', 'Flask', 'Django'}}
print(my_dict["lenguajes"]) # {'Java', 'C++', 'Python'}
print(my_dict["frameworks"]) # {'Spring', 'Flask', 'Django'}
print(len(my_dict)) # 2
print(len(my_dict["lenguajes"])) # 3

del my_dict["lenguajes"]
print(my_dict) # {'frameworks': {'Spring', 'Flask', 'Django'}}

print ("lenguajes" in my_dict) # False
print ("frameworks" in my_dict) # True

print(my_dict.keys()) # dict_keys(['frameworks'])
print(my_dict.values()) # dict_values([{'Spring', 'Flask', 'Django'}])
print(my_dict.items()) # dict_items([('frameworks', {'Spring', 'Flask', 'Django'})])
my_dict.update({"lenguajes":{"Python", "Java", "C++"}})
print(my_dict.fromkeys(["lenguajes", "frameworks"])) # {'lenguajes': None, 'frameworks': None} dict.fromkeys() method creates a new dictionary with keys from seq and values set to value.
my_new_dict = dict.fromkeys(my_dict) 
print(my_new_dict) # {'frameworks': None, 'lenguajes': None}

