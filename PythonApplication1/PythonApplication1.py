# a) Периметр квадрата
def square_perimeter(a):
    return 4 * a

# б) Радиус и площадь круга
def circle_properties(L):
    pi = 3.14
    R = L / (2 * pi)
    S = pi * R**2
    return R, S

# в) Электронные часы
def digital_clock(n):
    hours = (n // 60) % 24  # Количество часов в пределах суток
    minutes = n % 60
    return hours, minutes

# Тесты
print(square_perimeter(5))   # 20
print(circle_properties(31.4))  # (5.0, 78.5)
print(digital_clock(150))  # (2, 30)
print(digital_clock(1141)) # (0, 1)

# a) Изменение числа
def modify_number(n):
    return n + 1 if n > 0 else n

# б) Сумма двух наибольших чисел
def sum_of_two_largest(a, b, c):
    return sum(sorted([a, b, c])[1:])  # Берём два наибольших числа

# в) Оптимальная покупка билетов
def metro_tickets(n):
    # Определяем минимальные билеты
    cost_60 = 440
    cost_10 = 125
    cost_1 = 15

    # Оптимальная стратегия
    tickets_60 = n // 60
    n %= 60

    tickets_10 = n // 10
    n %= 10

    # Проверяем, что дешевле: докупить единичные или ещё один билет на 10 поездок
    if n * cost_1 > cost_10:
        tickets_10 += 1
        n = 0

    tickets_1 = n

    return tickets_1, tickets_10, tickets_60

# Тесты
print(modify_number(5))  # 6
print(modify_number(-3)) # -3

print(sum_of_two_largest(3, 7, 2))  # 10
print(sum_of_two_largest(10, 20, 15))  # 35

print(metro_tickets(129))  # (0, 1, 2)
