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
