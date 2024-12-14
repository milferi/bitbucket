def power(base, exponent):
    if exponent < 0:
        base = 1 / base 
        exponent = -exponent 

    result = 1
    for _ in range(exponent):
        result *= base 

    return result

print(power(2, 3))   #Вывод: 8
print(power(-2, 3))  #Вывод: -8
print(power(-2, 2))  #Вывод: 4
print(power(2, -3))  #Вывод: 0.125
print(power(-2, -3)) #Вывод: -0.125
