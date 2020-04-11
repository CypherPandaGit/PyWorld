# txt = open('ipsum.txt', 'r')
#
# for line in txt:
#     if 'bc' in line.lower():
#         print(line, end='')
#
# txt.close()

# with open('ipsum.txt', 'r') as txt: # you don't need close()
#     for line in txt:
#         if 'bc' in txt:
#             print(line, end='')
#
# ==============================================================

# cities = ['Paris', 'Berlin', 'Vienna', 'Zug', 'Hamburg', 'Salzburg', 'Linz']
#
# with open('cities.txt', 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

cities = []

with open('cities.txt', 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)
