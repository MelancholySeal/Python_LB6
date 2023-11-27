import re
word = input("Введите слово")
k = int(input('Введите номер буквы'))
data = []
data2 = []
if len(word) < 3:
    print('Слово слишком маленькое')
else:
    for i in range(len(word)):data.append(word[i])
    if k == 0:
        data[1] = '§'
    else:
        data[k-1] = '§'
        data[1] = '§'
    for i in range(len(data)):
        if data[i] != '§':
            data2.append(data[i])
data = ''.join(data2)

print(data)
