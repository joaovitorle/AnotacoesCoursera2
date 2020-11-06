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
top_three = []
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

def g(k,d): #Criou função "g"
    return d[k] #d[k] = medals[Japan], ou seja o value de Japan = 41

ks = medals.keys() #Variável ks = "Japan,Russia, ...." ou seja, todas as keys 

top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]   #Sorted classifica todos 
#as keys "ks" em ordem alfabética do menor para o maior, key informa como devemos organizar após o = do key
# lambda é uma forma mais simples de descrever uma função então Lambda tem uma varivável x,
# a função g recebe a x (Keys, ou seja, Japan ou Russia sem os values) e medals nas suas respectivas variáveis, ou seja k = x e d = medals.
# O que são medals ? é a lista, que irá dar um return de d[k] ou seja ex: medals[Japan] 

print(top_three)

#5
print('='*15,'#5','='*15)

most_needed = [] #Crio uma lista 
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
#Dicionário dado 
def s(z,y):#Crio uma função com as variáveis z e y que irão receber algum valor
    return y[z] #Irá retornar apenas o value da key especificada em z de um dicionário específicado em y que no caso é o groceries 
groceries_keys = groceries.keys() #Pegar apenas as keys do dicionário, ignorar os values
most_needed = sorted(groceries_keys, key= lambda x : s(x,groceries) , reverse = True) #Adicionar para a lista
#Todas as keys de grocery, organizadas do menor para o maior (Alfabético), chamo uma key para dize que
# irei organizar o most_needed de alguma forma, na qual seria atribuindo valores a função s, 
# onde x = key e groceries = o dicionário inteiro, utilizo o reverse para deixar do maior para o menor 
print(most_needed)

#6
print('='*15,'#6','='*15)

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
def last_four(x):
    
    return (str(x)[-4:])#Transformar em string a lista e pegar apenas os 4 últimos caracteres

last_four(ids)

sorted_ids = sorted(ids, key=last_four )
print(sorted_ids)

#7
print('='*15,'#7','='*15)

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key=lambda x: str(x)[-4:])
print(sorted_id)

#8
print('='*15,'#8','='*15)
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key = lambda x: x[1])
print(lambda_sort)
