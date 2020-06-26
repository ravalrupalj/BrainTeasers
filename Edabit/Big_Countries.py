#Big Countries
#A country can be said as being big if it is:

#Big in terms of population.
#Big in terms of area.
#Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

#Population is greater than 250 million.
#Area is larger than 3 million square km.
#Also, create a method which compares a country's population density to another country object. Return a string in the following format:

#{country} has a {smaller / larger} population density than {other_country}
class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        # implement self.is_big
        self.is_big = self.population > 250000000 or self.area > 3000000

    def compare_pd(self, other):
        # code
        this_density = self.population / self.area
        other_density = other.population / other.area
        if this_density > other_density:
            s_or_l = 'larger'
        else:
            s_or_l = 'smaller'
        return self.name + ' has a ' + s_or_l + ' population density than ' + other.name


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big )
#➞ True
print(andorra.is_big )
#➞ False
andorra.compare_pd(australia)
#➞ "Andorra has a larger population density than Australia"
#Notes
#Population density is calculated by diving the population by the area.
#Area is given in square km.
#The input will be in the format (name_of_country, population, size_in_km2), where name_of_country is a string and the other two inputs are integers.