#задача 6
string = "собака Шарик кошка Молли банан яблоко"
def words_function(text):
    words = text.split() #разбиваем строку на список слов по пробелам
    small_letter = list(filter(lambda x: x[0].islower(), words)) #оставляем слова с маленькой буквы
    small_letter.sort(reverse=True) #сортировка слов в порядке, обратном алфавитному
    return small_letter
result = words_function(string)
print("Итоговый список:", result)