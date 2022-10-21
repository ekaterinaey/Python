# Задача №1
# Определить, присутствует ли в заданном списке строк, некоторое число


text_1 = ["5", "8", "32", "55", "7", "8"]
num = 8
numControl = str(num)

res = lambda text_1, numControl: True if numControl in text_1 else False

if(res(text_1, numControl)):
    print("Присутствует")
else:
    print("Отсутствует")


# Задача №2
# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.


n = int(input('Введите количество чисел больше 0: '))

def f(x):
    return (-3) ** x

res2 = [f(i) for i in range(n)]
print(res2)



# Задача №3
# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.


my_text = 'привет мир привет друзья'
my_text_1 = 'привет'
my_list = my_text.split(" ")

res3 = list(filter(lambda x: x == my_text_1, my_list)) 

print(len(res3))



