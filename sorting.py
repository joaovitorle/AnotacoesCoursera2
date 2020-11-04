print('='*15,'#1','='*15)
#Sort function - Vai organizar do menos para o maior valor em lista
L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]

L1.sort()
print(L1)
L2.sort()
print(L2)

print('='*15,'#2','='*15)
#Sorted 

L2= ["Cherry", "Apple", "Blueberry"]
L3= sorted(L2)
print(L3)
print(sorted(L2))
print(L2)

print("--------")
L2.sort()
print(L2)
print(L2.sort())

print('='*15,'#3','='*15)
#Optional reverse parameter
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2,reverse = True))

print('='*15,'#4','='*15)
#Optional key parameters 
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))

print('='*15,'#5','='*15)
#Optional key parameters 
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x>=0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute )
print(L2)

#or in reverse order
print(sorted(L1, reverse = True, key = absolute))


print('='*15,'#6','='*15)
#Optional key parameters 
L1 = [1, 7, 4, -2, 3]
def absolute(x):
    print('--- figuring out what to write on the post-it note for ' +str(x))
    if x >=0:
        return x
    else:
        return -x
print("About to call sorted")
L2= sorted(L1, key=absolute)
print("Finish execution of sorted")
print(L2)

print('='*15,'#7','='*15)
#Sorting a dictionary
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] +1
    else:
        d[x] = 1
for x in sorted(d.keys(), key=lambda k: d[k]):
    print(f'{x} appears {d[x]} times')

print('='*15,'#8','='*15)
#Breaking Ties: Second Sorting
tups = [("A", 3, 2),
        ("C", 1, 4),
        ("B", 3, 1),
        ("A", 2, 4),
        ("C", 1, 2)]
for tup in sorted(tups):
    print(tup)

print('='*15,'#9','='*15)
#Breaking Ties: Second Sorting
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key = lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print (fruit)

print('='*15,'#9','='*15)
#When to use a Lambda Expression - A lambda expression is short and simple use, when things get complicated use a function

states = {"Minnesota": ['St.Paul', 'Minneapolis', 'Saint Cloud', 'Stillwater'],
        "Michigan":['Ann Arbor', 'Traverse City', 'Lansing', 'Kalamazoo'],
        "Washington":["Seatle", "Tacoma", "Olympia", "Vancouver"]}

def s_cities_count(cities_list):
    #return a count of how many cities begin with "S"
    ct = 0
    for city in cities_list:
        if city[0] == 'S':
            ct = ct +1
        return ct
def s_cities_count_for_state(state):
    cities_list = states[state]
    return s_cities_count(cities_list)


print(sorted(states,key=s_cities_count_for_state)) 