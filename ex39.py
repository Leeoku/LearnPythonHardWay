#create mapping of state to abbrev
states = {
    'Oregeon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

provinces = {
    'Ontario': 'ON',
    'Quebec': 'QC',
    'British Columbia': 'BC'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cadcities = {
    'ON': 'Toronto',
    'QC': 'Montreal',
    'BC': 'Vancouver'
}
#add more cities
cities['NY']='New York'
cities['OR']='Portland'

#print cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-'*10)
print("Michigan abbreviation is: ", states['Michigan'])
print("Florida abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at same time
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#CAD prints
for province, abbrev in list(provinces.items()):
    print(f"{province} province is abbreviated {abbrev}")
    print(f"with city {cadcities[abbrev]}")

print('-'*10)
#safely get abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with defualt value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
