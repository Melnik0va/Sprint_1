world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'
for champions in world_champions: 
    print(champions, '-', world_champions[champions])

country = 'Италия'
def check_italy(country): 
    if country in world_champions.values(): 
            return True
    else: 
            return False

for keys in world_champions.keys():
    if keys // 1000 >=2: 
        check_italy(country)


if check_italy(country): 
     print(country, 'становилась чемпионом мира по футболу в 21 веке!')
else:      
    print(country, 'не выиграла чемпионат мира по футболу в 21 веке.')