a = frozenset('abcdefg') # Неизменяемое множество
print(a)
for i in range(1,5):
    a.add(i)
print(a)