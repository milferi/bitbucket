def fast_power(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:  # Если степень нечетная
            result *= base
        base *= base  # Увеличиваем основание
        exponent //= 2  # Делим степень на 2
    
    return result

# Пример использования
base = float(input("Введите основание (дробное число): "))
exponent = int(input("Введите целую положительную степень: "))

result = fast_power(base, exponent)
print(f"{base} в степени {exponent} равно {result}")
