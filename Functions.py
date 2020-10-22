print('='*15,'#1','='*15)
#1
def hello(): #Definindo o nome da função 
    print ('Hello') #O que a função fara
    print ('Glad to meet you')
hello() #Executar a função 

print('='*15,'#2','='*15)
#2 Function parameters
def hello2(s): #s é um parametro 
    print('Hello ' + s)
    print('Glad to meet you')
hello2('João') #"João" irá assinar a variável "s" 
hello2('Barreto') #"Barreto" irá assinar a variável "s" 

print('='*15,'#3','='*15)
#3 Function parameters 
def hello3(s, n):
    greeting = f"Hello {s}"
    print (greeting*n)
hello3('Wei ', 4)
hello3("", 1)
hello3('Kitty ', 11)

print('='*15,'#4','='*15)
#4 Returning values
def square(x): #definimos a função square 
    y = x * x
    return y #retorna o valor da função, então a variável "result" recebe o valor da variável "y"
Tosquare = 10 #definimos que a variavel "Tosquare" = 10
result = square(Tosquare) 
"""Chamamos, dentro a variável result, a função "square" para atribuir o 
valor da variável "Tosquare" para a variável "x", então "x" = qualquer valor presente na variável
"Tosquare", ou seja "x" = 10 nesse caso"""
print(f'The result of {Tosquare} squared is {result}')

print('='*15,'#5','='*15)
#5
def square(x):
    y = x*x
    print (y) #Bad! This is confusing! Should use return instead!

toSquare = 10
squareResult = square(toSquare) #Variável "squareResult" não recebe o valor da variável "y".
print(f'The result of {toSquare} squared is {squareResult}')


print('='*15,'#6','='*15)
#6
def weird():
    print('here')
    return 5 #return statement makes you skip the rest of the code in that function
    print('there')
    return(10)

x = weird() #A variável x irá receber tanto o comando print, como também o valor retornado. 


print('='*15,'#7','='*15)
#7
def longer_than_five(list_of_names):
    for name in list_of_names: #iterate over the list to look at each name
        if len(name) > 5: #as soon as you see a name longer than 5 letters,
            return True #Then return true!
            #If python executes that return statement, the function is over the rest of the code will not run
    return False #You will only get to this line if you 
    #iterated over the whole list and did not get a name where
    #the if expression evaluated(avaliada) to true, so at this point, it's correct to return false!

#Here are a couple sample calls to the function with different lists of names.
list1 = ['Sam', 'Tera', 'Sal', 'Amita']
list2 = ['Rey', 'Ayo', 'Lauren', 'Natalie']

print(longer_than_five(list1))
print(longer_than_five(list2))


print('='*15,'#8','='*15)
# Decoding a function, very important decode a function before start to code
def cyu3(x, y, z): #Quantos parametros ? 3 Parametros, qual o type dos parametros ? Int, float (x e y) e list (z)
#What are the possible types of the return value from cyu3 ? Int or float 
    if x - y > 0:
        return y - 2
    else:
        z.append(y)
        return x +3


print('='*15,'#9','='*15)
#9 Function that accumulates
def total(lst):
    tot = 0   
    for num in lst:
        tot = tot + num 
    return tot
y = total([1,5,7])
print (y)


print('='*15,'#10','='*15)
#10 Functions calling other functions (compostion)
def square(x):
    y= x*x
    return y

def sum_of_square(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a+b+c

a = -5
b = 2
c = 10

result = sum_of_square(a,b,c)
print (result)


print('='*15,'#11','='*15)
#11 Functions calling other functions (compostion)
def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
             d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

print(most_common_letter("abbbbbbbbbbbccccddddd"))




print('='*15,'#12','='*15)
#12 Mutable objects 

def changeit(lst):
    lst[0] = 'Michigan'
    lst[1] = 'Wolverines'

mylst = ['our', 'students', 'are', 'great']
changeit(mylst)
print(mylst)




