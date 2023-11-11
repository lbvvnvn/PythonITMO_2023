cities = [
    'Москва',
    'Токио',
    'Париж',
    'Нью-Йорк',
    'Лондон',
    'Берлин',
    'Сингапур',
    'Копенгаген',
    'Амстердам',
    'Сидней'
]

# TODO с помощью цикла for и команды enumerate распечатайте рейтинг городов
for number, name_city in enumerate(cities, start=1):
    print(f"{number:2}-е место:", name_city)