#JJ Gallagher
#May 23, 2016
#Homework 1



name = input("Hi, What's your name?")
print("Hi, " + name)

year_of_birth = input("What year were you born in?")

age = 2016 - int(year_of_birth)

if age <= 0:
    year_of_birth = input("What year were you born in?")
    age = 2016 - int(year_of_birth)
else:
    print("You are about", age, "years old")

ageinearthdays = (age * 365)
venusage = (ageinearthdays / 225)
neptuneage =  (ageinearthdays / 60190)

heartrate = (age * 31536000)
bluewhaleheartrate = (age * 4207592)
rabbitheartrate = (age * 63113880)

print("Your heart has beaten about", heartrate, "times")
print("The heart of a blue whale born in the same year as you has has beaten about", bluewhaleheartrate, "times")
print("The heart of a rabbit born in the same year as you has has beaten about", round((rabbitheartrate / 1000000000),2), "billion times")
print("In Venus years, you are", (venusage), "years old")
print("In Neptune years, you are", (neptuneage), "years old")

if age > 36:
    print("You are", (age - 36), "years older than me")

elif age <= 36:
    print("You are", (36 - age), "years younger than me")

if (int(year_of_birth) % 2 == 0):
    print("You were born in an even numbered year")
elif (int(year_of_birth) % 2 != 0):
    print("You were born in an odd numbered year")
else:
    print("didn't work")
