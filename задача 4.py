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