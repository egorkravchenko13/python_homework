print("""Кравченко Єгор Володимирович
Лабораторна робота №2
Варіант 11 
Обчислення виразу \n""")

import re
pattern_int=r"^[-\d]\d*$"
var1=input("Введіть перше число діапазону: ")
while (not re.match(pattern_int, var1)):
    var1=input("Введіть верхню межу суми")
var2=input("Введіть останнє число діапазону: ")
while (not re.match(pattern_int, var2)):
    var2=input("Введіть змінну відмінну від 0")
   
sum=0
for i in range(int(var1), int(var2)+1):
    if (i%2!=0):
        sum+=i
        print(i,end='')
    if i<(int(var2)): 
        print("+", end='')    
print('=',(sum))



