city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

num_cities = len(city_list)
population = 0

for i in range(0, num_cities):
    num_cities = len(city_list)
    population += city_list[i]["population"]

total_population = population
average_population = population / num_cities

print(f"Среднее арифметическое населения равно = {average_population}")
