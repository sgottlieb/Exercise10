things = ['a', 'b', 'c', 'd',]
print things[1]

things [1] = 'z'
print things[1]

print things

# This is assigning items into the dict
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = 'San Francisco'

print stuff['city']

# This is to delete items.
del stuff['city']
del stuff[1]
del stuff[2]

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
for state, abbrv, in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in stateprint '-' * 10
for abbrev, city in cities.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city