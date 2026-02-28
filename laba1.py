#задача 1
#создадим кортеж
tuple = (7, 8, 9, 10, 11, 12, 13, 14, 15)
print(tuple)
#задача 2
#создадим список
list0 = []
for i in tuple: # заполняем список числами из кортежа
    if i % 2 == 0:
        i = i * 3 # если чётное, то увеличиваем в 3 раза
    else:
        i = i - 3   # если нечётное, то уменьшаем на 3
    list0.append(i) #добавляем новое число в список
print(list0)

#задача 3
#создадим массив
massiv = [3, 5, 8, 13]
#создадим множество
mnoj = set()
for i in list0:
    mnoj.add(i) #добавим элементы из списка
for i in massiv:
    mnoj.add(i)
print(mnoj)

#задача 4
#зададим произвольный словарь
dict = {
    "кошка": "животное",
    "Python": "язык",
    "малина": "ягода",
    "банан": "фрукт"
}
dict2 = {}
for kl, znach in dict.items():
    dict2[znach] = kl
print(dict2)

#задача 5
def function1(start, end, step):
    list1 = list(range(start, end + 1, step)) # создаем список по входным значениям
    multiples = list(filter(lambda x: x % 6 == 0, list1)) # отбираем числа, кратные 6ти
    count_multiples = len(multiples)  # считаем количество чисел кратных 6

    print("Числа кратные 6:", multiples)  # выводим найденные числа
    print("Количество кратных 6:", count_multiples)  # выводим их количество

    min1 = min(multiples) #находим минимальное число в списке
    min3 = min1 ** 3 # возводим его в куб
    print("Минимальное число в кубе:", min3)  # выводим куб минимального числа

    subtraction = count_multiples - min3
    print("Разница:", subtraction)  # выводим разницу

    if subtraction < 0:
        list1.reverse()  # разворачиваем список в обратном порядке
        final_list = list1  # сохраняем перевернутый список
    else:  # если результат положительный или равен нулю
        final_list = list1.copy()  # создаем копию исходного списка
        final_list.insert(0, subtraction)  # добавляем результат в начало списка
    return final_list  # возвращаем итоговый список из функции

start = 1
end = 95
step = 1
res = function1(start, end, step)
print("Итоговый список:", res)  # выводим результат работы функции

#задача 6
def words_function(text):
    words = text.split() #разбиваем строку на список слов по пробелам
    small_letter = list(filter(lambda x: x[0].islower(), words)) #оставляем слова с маленькой буквы
    small_letter.sort(reverse=True) #сортировка слов в порядке, обратном алфавитному
    return small_letter

#задача 7
string = "собака Шарик кошка Молли банан яблоко"
result = words_function(string)
print("Итоговый список:", result)

def function5(n):
    if n <= 0: # если число меньше или равно 0 - False
        return False
    while n % 3 == 0: # делим число на 3 пока оно делится без остатка
        n = n // 3  # целочисленное деление
    if n == 1: # если получили 1
        return True
    else:      # в противном случае
        return False
argument = -3
result = function5(argument)
print(result)