with open('test.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('test.txt', 'r') as f:
    result = f.readlines()
    print(result)