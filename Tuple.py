#1

julia = ('Julia', 'Roberts', 1967, 'Duplicity', 2009, 'Actress', 'Atlanta')
#or equivalently
julia = 'Julia', 'Roberts', 1967, 'Duplicity', 2009, 'Actress', 'Atlanta'
print(julia[4])

#2 Returning multiple values
def circleInfo(r):
    # Return (cirfumference, area ) of a circle of radius r
    c = 2* 3.14 * r
    a = 3.14 * r * r
    return c,a

print(circleInfo(10))

#3 Tupple Assignment with unpacking 
julia = 'Julia', 'Roberts', 1967, 'Duplicity', 2009, 'Actress', 'Atlanta'
name, surname, birth_year, movie, movie_year, profession, birth_place = julia


#4 
def add(x, y):
    return x+y
print(add(3,4))
z = (5,4)
print(add(*z)) #this line will cause the values to be unpacked 
#print(add(z)) #this will be an error

#5 
d = {'k1': 3, 'k2': 7, 'k3': 'some other value'}
for p in d.items():
    print(f"key: {p[0]}, value: {p[1]}")



