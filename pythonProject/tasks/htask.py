word1 = 'abbcc'
word2 = 'abbvv'
nullword=''
for i in range(len(word1)):
    if word1[i] not in word2:
        nullword+=word1[i]+' '

for i in range(len(word2)):
    if word2[i] not in word1:
        nullword+=word2[i]+' '

print(nullword)