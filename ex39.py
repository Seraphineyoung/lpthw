#LIST
# things = ["a","b","c","d"]
# print(things[1])
# things[1] = "z"
# print(things[1])
# print(things)

#DICT

# stuff = {"name": "Seraphine", "age": 30, "height": 6 * 12 + 2}
# print(stuff["name"])
# print(stuff["age"])
# print(stuff["height"])

# stuff["city"] = "London"
# print(stuff["city"])

# stuff[1] = "wow"
# stuff[2] = 500
# print(stuff[1])
# print(stuff[2])

# del stuff ["city"]
# del stuff [1]
# del stuff [2]

# print(stuff)


#create a mapping of state to abbreviation

states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}
#createa basic set of states and some cities in them
cities = {
"CA": "San Francisco",
"MI": "Detriot",
"FL": "Jacksonville"
}

#add some more cities

cities["NY"] = "New York"
cities["OR"] = "Portland"

print("-" * 10)
print("NY state has: ", cities["NY"])
print("OR state has: ", cities["OR"])

#print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

#do it by uing the state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

#print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f" and has city {cities[abbrev]}")

print("-" * 10)
#safely get an abbreviation by state that might not be there
state = states.get("Texas")

if not states:
    print("Sorry, no Texas.")

#get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")