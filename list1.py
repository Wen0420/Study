list_int = [1,2,3,4,5,6]
print(list_int)

print(list_int[3])

list_int[3] = 'B'
print(list_int)

list_int.append("AA")
print(list_int)

print(list_int[2:5])

print(list_int[2::3])

print(list_int[::2])

print(list_int[1:6:2])

list_int.insert(0, 'AA')
list_int.insert(4, 'AA')
print(list_int)

del list_int[1]
print(list_int)

print(list_int.index('AA'))

print(list_int.index('AA',3))

print(list_int.index('AA',3,5))

print(list_int.index('AA',-2))

print(list_int.index('AA',-1))