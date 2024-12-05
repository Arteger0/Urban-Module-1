my_dict = {'Dima': 1995, 'Gala': 1975, 'Valera': 1984}

print(my_dict)
print(my_dict['Gala'])
print(my_dict.get('Maria')) # вывод по ключу

my_dict.update({'Maria': 1994, 'Nikita': 1997}) # добавление в словарь
print(my_dict)

my_dict.pop('Gala')
print(my_dict)

my_set={2,2,2,55,334,334,55,64, True, 'Table'}
print(my_set)

my_set.add((65,46))
my_set.remove(334)
print(my_set)
