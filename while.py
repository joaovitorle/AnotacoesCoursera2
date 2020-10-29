#1
def sumTo(aBound): #Return the sum of 1+2+3 ... n 
    theSum = 0
    aNumber = 1
    while aNumber <= aBound: #If this conditional is true, then we run the code, if it's not true, it will run the next code
        theSum = theSum + aNumber
        aNumber = aNumber +1 
    return theSum

print(sumTo(4))
print(sumTo(1000))

#2
count = 0
eve_nums = []
while count <= 15:
    if count % 2 ==0:
        eve_nums.append(count)
    count = count + 1

#3
list1 = [8,3,4,5,6,7,9]

tot = 0 
for elem in list1:
    tot = tot + elem
idx = 0 
accum = 0 
while idx < len(list1):
    accum = accum + list1[idx]
    idx = idx + 1

#4 The listener loop
theSum = 0
x = -1
while (x !=0):
    x = int(input('Next number to add up (enter 0 if no more number):'))
    theSum = theSum +x
print (theSum)


#5
def get_yes_or_no (message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()#convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Yes or No: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')

#6 Break
while True:
    print('This phrase will always print')
    break #Podemos pausar qualquer while loop, mesmo que continue sendo true, o que estiver a baixo do break não irá rodar.
    print('Does this phrase print?')

print('We are done with the while loop.')

#7 Continue
#while True:
#    print('This phrase will always print')
#    continue #Qualquer coisa que vem acima do continue irá continuar no loop ignorando o que estiver debaixo.  
#    print('Does this phrase print?')

#print('We are done with the while loop.')

#8 
x = 0
while x < 10:
    print('we are incrementing x')
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print ('Done with our loop! X has the value' + str(x))