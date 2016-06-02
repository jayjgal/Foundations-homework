#JJ Gallagher
#Jun 1, 2016
#Homework 3

#LISTS

countries = ['Sweden', 'Denmark', 'Norway', 'Iceland', 'Finland', 'Russia', 'Latvia']

for country in countries:
    print(country)
countries.sort()
print(countries[0])
print(countries[-2])
countries.remove('Russia')

for country in countries:
    print(country)





tree = { 'name': "Jomon Sugi", 'species': "Cryptomeria", 'age': 2170, 'location': "Yakushima", 'latitude': 40.76, 'longitude': 55.81 }

print(tree['name'], "is a tree", tree['age'], "located in", tree['location'] + ".")

if int(tree['latitude']) > 40.7128:
    print(tree['name'], "in", tree['location'], "is south of NYC.")
elif int(tree['latitude']) < 40.7128:
    print(tree['name'], "in", tree['location'], "is north of NYC.")

age = input("How old are you?")

if int(age) > (tree['age']):
    print("You are", (int(age) - tree['age']), "years older than the tree.")

elif int(age) < tree['age']:
    print(tree['name'], "was", tree['age'] - int(age), "years old when you were born.")


cities = [
    { 'name': 'Moscow', 'latitude': 55.75, 'longitude': -37.61 },
    { 'name': 'Tehran', 'latitude': 35.68, 'longitude': -51.38 },
    { 'name': 'Falkland Islands', 'latitude': -51.79, 'longitude': -59.52 },
    { 'name': 'Seoul', 'latitude': 37.56, 'longitude': 126.97 },
    { 'name': 'Santiago', 'latitude': -33.44, 'longitude': -70.66 }
]


for city in cities:
    if city['latitude'] > 0:
        print(city['name'], "is above the equator.")
    elif city['latitude'] < 0:
        print(city['name'], "is below the equator.")
    elif city['name'] is 'Falkland Islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")





for city in cities:
    if city['latitude'] > 40.76:
        print(city['name'], "is farther north than Jomon Sugi")
    elif city['latitude'] < 40.76:
        print(city['name'], "is farther south than Jomon Sugi")
