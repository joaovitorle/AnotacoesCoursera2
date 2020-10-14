#1
eng2pt = {} # We just created an empty dictionary 

eng2pt['one'] = 'um' #'one' is the key and 'um' is the value. The key is like the main word, in a real dictionarie, and the value is the description of the dictionary.
eng2pt['two'] = 'dois'
eng2pt['three'] = 'três'

print(eng2pt)

print('='*30)
#2

eng2pt = {'three': 'três', 'two': 'dois', 'one': 'um'} # We just created an empty dictionary 

value = eng2pt['two']
print(value)

print(eng2pt['one'])

print('='*30)
#3 number in the dictionary

olympics = {'gold': 7, 'silver': 10, 'bronze': 20}
print(olympics)

print('='*30)
#4 Dictionary operations

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
del inventory ['pears'] #Delete from the inventory the key called pears 

print(inventory)

print('='*30)
#5 How to change the value number
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory ['pears'] = 0 #Change the value number 

print(inventory)

print('='*30)
#6 Somar um value 

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory ['bananas'] = inventory ['bananas'] + 200
numItens = len(inventory)

print (inventory)
print (numItens)
print (inventory['bananas'])

print('='*30)
#7 Dictionary Methods 
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for key in inventory.keys():
    print(key,'has the value', inventory[key])

for key in inventory:
    print ('Got key', key)

print('='*30)    
#8 Turn into a list 

keys = list(inventory.keys())
print(keys)

print('='*30)
#9
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print (list(inventory.values()))
print (list(inventory.items()))

for key in inventory:
    print('Got', key, "that maps to", inventory[key])

print('='*30)
#10
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory) #in retorna True or false se tiver aquela palavra dentro do inventorio
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print('We have no bananas')

print('='*30)

#11 Using get
 
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.get('apples')) #get the value of the key directly
print(inventory.get('cherries'))
print(inventory.get('cherries',0)) #equal to the code above, ao inves de o resultado ser "None" is "0"

print ('='*30)

#12 Aliasing and copying 

opposites = {'up' : 'down', 'right': 'wrong', 'true' : 'false'}
alias = opposites

print (alias is opposites)

alias ['right'] = 'left'
print(opposites['right'])

print ('='*30)

#12 Accumulating in dictionary

f = open ('olympics.txt', 'r')
txt = f.read() #now the txt is one long string containing all the characters 
x = {} #starts with an empty dictionary
x['t'] = 0 #initializer the t counter 
x['s'] = 0 #initialize the s counter
for c in txt: 
    if c == 't':
        x['t'] = x['t'] +1 #increment the t counter 
    elif c == 's':
        x['s'] = x['s'] +1 #increment the s counter
print('t: ' + str(x['t']) + ' occurences ')
print('s:' + str(x['s']) + ' occurences')

#13 Accumulating in dictionary 

f = open('olympics.txt', 'r')
txt = f.read() #now the txt is one long string containing all the characters 
x = {}
for c in txt:
    if c not in x: #we have not seen this characters before, so initialize a counter for it
        x[c] = 0 
    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1
print('t: ' + str(x['t']) + ' occurences ') #Now i can find all the occurences, just print it out
print('s:' + str(x['s']) + ' occurences')
print('t: ' + str(x['a']) + ' occurences ')
print('s:' + str(x['b']) + ' occurences')

#14
txt = 'MICHIGAN'
x = {}
for c in txt:
    if c not in x: #we have not seen this characters before, so initialize a counter for it
        x[c] = 0 
    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1 #Se o caracter já foi visto incrementa +1
print('t: ' + str(x[c]) + ' occurences ') #Now i can find all the occurences, just print it out


