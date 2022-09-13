
from datetime import datetime
name = input('jmeno? \n')
age = int(input('věk? \n'))
hundred = int((100-age) + datetime.now().year)
print ('ahoj %s. je ti %s let. bude ti 100 v roce %s.' % (name, age, hundred))

n = int(input("cislo"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("soucet je: ", sum)

rows = int(input("pocet radku: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")


numbers = [12,75,150,180,145,525]
for i in numbers:
    if 150 < i:
        continue
    elif i > 500:
        break 
    elif((i%5==0)):
        print(i)
    
    


