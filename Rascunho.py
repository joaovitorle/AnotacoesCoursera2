def g(k,d): #Criou função "g"
    return d[k]

ks = medals.keys() #Variável ks = "Japan,Russia, ...." ou seja, todas as keys 

top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]   #Sorted classifica todos 
#as keys "ks" em ordem alfabética do menor para o maior, key informa como devemos organizar após o = do key
# lambda é uma forma mais simples de descrever uma função então Lambda tem uma varivável x,
# a função g recebe a x e medals nas suas respectivas variáveis, ou seja k = x e d = medals.
# O que são medals ? é a lista, que irá dar um return de d[k] ou seja medals[] 
   
