dict1={"name":"name",'age':19,"other":"v2"}
print(dict1)

dict1['A1']='A1'
print(dict1)

dict1['A1']='A2'
print(dict1)

del dict1['A1']
print(dict1)

print(dict1['name'])

dict1['A2'] = None
print(dict1.get('A1'))
print(dict1.get('A2'))
print(dict1['A2'])

print(dict1.get('A2',"default"))
print(dict1.get('A1',"default"))

print(dict1.keys())
print(dict1.items())