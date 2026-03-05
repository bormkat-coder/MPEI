#задача 4
#зададим произвольный словарь
my_dict = {}
n = int(input("Сколько пар добавить: "))
for i in range(n):
    kl = input("Введите ключ: ")
    znach = input("Введите значение: ")
    my_dict[kl] = znach #добавим пару в словарь
print(my_dict)

dict2 = {}
for kl, znach in my_dict.items():
    dict2[znach] = kl
print(dict2)
