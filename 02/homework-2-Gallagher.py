#JJ Gallagher
#May 25, 2016
#Homework 2

numlist = [22, 90, 0, -10, 3, 22, 48]


print(len(numlist))
print(numlist[3])
print(numlist[1] + numlist[3])
print(sorted(numlist)), (numlist[5])
print(numlist[6])


for num in numlist:
    if num <= 10:
        print(num * 30)
    elif num % 2 == 0:
        print(num + 6)
    elif num > 50:
        print(num - 10)
    elif num != -10:
        print(num - 1)


total = 0
for num in numlist:
    num = num/2
    total = total + num
print(total)

movies = { 'title': "Inherent Vice", 'year': "2014", 'director': "Paul Thomas Anderson", 'budget': 20, 'gross': 14.7 }

print("My favorite movie is", movies['title'], "which was released in", movies['year'], "and was directed by", movies['director'] + ".")

print(movies['title'], "grossed $" +str(movies['gross']), "million at box offices worldwide.")

if movies['gross'] > movies['budget']:
    print("It was a good investment.")
elif movies['gross'] < movies['budget']:
    print("It was a box office flop.")


nyc_info = [
    { 'name': 'Manhattan', 'population': 1600000 },
    { 'name': 'Brooklyn', 'population': 2600000 },
    { 'name': 'Queens', 'population': 2300000 },
    { 'name': 'Staten Island', 'population': 470000 }
]

#for boro in nyc_info
manhattan = nyc_info[0]
brooklyn = nyc_info[1]
queens = nyc_info[2]
staten = nyc_info[3]
print("Brooklyn's population is", ((brooklyn['population']) /1000000), "million.")
print("New York City's total population is", ((brooklyn['population'] + manhattan['population'] + staten['population'] + queens['population']) /1000000), "million.")
