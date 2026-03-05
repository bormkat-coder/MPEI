#задача 7
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