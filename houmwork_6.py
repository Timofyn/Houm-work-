my_dict = {"IO":2045, "Pipboy":1997 }
print(my_dict)
print(my_dict['IO'])
print(my_dict.get("Pop"))
my_dict.update({'pop':12348765, 'yo-yo':12457869})
print(my_dict)
a = my_dict.pop('Pipboy')
print(my_dict)
print(a)
my_set = {1, 2,'Io', 1.2, 3, 5, 2, 1, 4,6, 6, 6, 7,(11, 12, 12,342,11 ) }
print(my_set)
print(my_set.add(45))
print(my_set.add(78))
print(my_set.discard(0))
print(my_set.remove(1))
print(my_set)