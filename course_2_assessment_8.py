#1
print('='*15,'#1','='*15)

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters,reverse = True)

print(sorted_letters)

#2
print('='*15,'#2','='*15)

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)
print(animals_sorted)

#3
print('='*15,'#3','='*15)

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

alphabetical = sorted(medals)
print (alphabetical)

#4
print('='*15,'#4','='*15)


top_three = [] #Criou lista 
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70} #Criou dicionário
def g(k,d): #Criou função "g"
    return d[k]

ks = medals.keys() #Variável ks = "Japan,Russia, ...." ou seja, todas as keys 

top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]   #Sorted classifica todos 
#as keys "ks" em ordem alfabética do menor para o maior, key informa como devemos organizar após o = do key
# lambda é uma forma mais simples de descrever uma função então Lambda tem uma varivável x,
# a função g recebe a x e medals nas suas respectivas variáveis, ou seja k = x e d = medals.
# O que são medals ? é a lista, que irá dar um return de d[k] ou seja medals[] 

#5
print('='*15,'#5','='*15)

top_three = [] #Criou lista 
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70} #Criou dicionário
def g(k,d): #Criou função "g"
    return d[k]

ks = medals.keys() #Variável ks = "Japan,Russia, ...." ou seja, todas as keys 

def s(x):
    top_three = sorted(ks,reverse= True(g(x,medals)[:3]
    
print(s(top_three))