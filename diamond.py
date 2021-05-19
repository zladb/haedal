
str = ''

for num in range(4,0,-1):
    str +=' '*num + '*'*((4-num)*2+1) +'\n'
    
for num in range(0,5,1):
    str +=' '*num + '*'*((4-num)*2+1) +'\n'

print(str)
