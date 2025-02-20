"""
Q2-1. Country
Write class `Country`.

- Using the `__init__` method, make a class `Country` that takes name, population, and area as parameters.
- Define an `is_larger` method that returns `True` only when the first country has a larger area than the second country (Return `False` if the area is the same).
- Define a `population_density` method that returns the population density (number of people per area) of a country (There is no case where the area is zero).
"""

# 2.

class Country :
  def __init__(self, name, population, area):
    self.name= name
    self.population = population
    self.area= area
    
  def is_larger(self, country) :
    return self.area > country.area
  
  def population_density(self) :
    return self.population / self.area

canada = Country('Canada', 34482779, 9984670)
print('Name :', canada.name, '/Expected: Canada')
print('Area :', canada.area, '/ Expected: 9984670')

usa= Country('United States of America', 313914040, 9826675)
print('Is Canada larger than USA:', canada.is_larger(usa), '/Expected : True')
print('Density of Canada is:', canada.population_density(), '/Expected 3.4535722262227995')
    
"""
Q2-2. Continent
Write class `Continent`.

- By using `__init__` method, make class `Continent` that takes name, countries as parameters.  Countries is a list of `Country` objects and at least has more than one element.
- Define `total_population` method that returns the sum of the population of countries belonging to the continent
"""

# 2-2.

class Continent :
  def __init__(self, name, countries : list):
    self.name= name
    self.countries = countries
  
  def total_population(self) :
    sum= 0
    for country in self.countries :
      sum += country.population
    return sum

canada = Country('Canada', 34482779, 9984670)
usa= Country('United States of America', 313914040, 9826675)
mexico= Country('Mexico', 112336538, 1943950)
countries= [canada, usa, mexico]
north_america= Continent('North America', countries)

print('Name :', north_america.name, '/ Expected : North America')
print('Population:', north_america.total_population(), '/ Expected: 460733357')

