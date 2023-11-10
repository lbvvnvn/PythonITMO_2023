city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

max_population = 5  # Пороговое значение для населения


num_cities = len([city for city in city_list if city["population"] < max_population])

print(f"Количество городов с население до 5 млн. жителей равно = {num_cities}")
