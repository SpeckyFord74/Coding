my_dict = {'key_1':'value1', 'key_2':'value2', 'key_3':'value3'}
print(my_dict['key_2'])

my_dict_2 = {'key1':123, 'key2':[12, 23, 10], 'key3':['item0','item1','item2']}
print(my_dict_2['key3'])

print(my_dict_2['key3'][0])

print(my_dict_2['key3'][1].upper())

my_dict_2['key1'] -= 123
print(my_dict_2['key1'])

my_dict_3 = {}
my_dict_3['animal'] = 'Dog'
my_dict_3['answer'] = 42
print(my_dict_3)

dict_nest = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(dict_nest['key1']['nestkey']['subnestkey'])

dict_funcs = {'key1':1, 'key2':2, 'key3':3}
print(dict_funcs.keys())
print(dict_funcs.values())
print(dict_funcs.items())

mod_dict = {'key1':1, 'key2':2, 'key3':3}
mod_dict['key1'] = 4
print(mod_dict['key1'])

list_in_dict = {}
list_in_dict['List'] = ['Hello', 'World']

print(list_in_dict)
