def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Пример использования
result = power(2, 3)  # 2 в степени 3
print(result)  # Вывод: 8
