# Задача №1
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from decimal import Decimal
from random import randint, random, uniform


n = int(input("Задайте длину списка: "))

numbers = []
res = 0
for i in range(n):
    numbers.append(randint(0, 9))
    if i%2 != 0:
        res = res + numbers[i]
print(numbers)
print(res)




# Задача №2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д


nSecond = int(input("Задайте длину списка: "))
numbersSecond = []
resN = []

for j in range(nSecond):
    numbersSecond.append(randint(0, 9))

if len(numbersSecond)%2 == 0:
    l = nSecond // 2
else:
    l = (nSecond // 2) + 1
    
for j in range(l):
    resN.append(numbersSecond[j] * numbersSecond[-j -1])
    

print(numbersSecond)
print(resN)



# Задача №3
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

m = int(input("Задайте длину списка: "))
listing = []
difference = 0


for k in range(m):
    listing.append(round(uniform(0, 9), 2))   

print(listing)

difference = (max(listing) - min(listing))%1


print(max(listing))
print(min(listing))
print(f"Разница: {difference:.2f}")



# Задача №4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


number = int(input("Введите число: "))
numberBin = ""

while number > 0:
    numberBin = str(number % 2) + numberBin
    number = number // 2

# print(bin(number))
print(numberBin)

