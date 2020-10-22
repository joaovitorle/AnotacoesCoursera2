#1 
def int_return(x):
    return x


v = 10
y = int_return(v)

#2
def add(x):
    y = x + 2
    return y

input_number = int(input('Digite um valor: '))
y = add(input_number)
print(y)

#3
def change(x):
    y = x + " Nice to meet you!"
    return y
input_string = input('Digite seu nome: ')
Return_value = change(input_string)    
print (f'Welcome, {Return_value}')

#4
def accum(lst):
    tot = 0
    for num in lst:
        tot = tot + num
    return tot

list_integers = [1, 2, 3, 4, 10, 23, 22, 20]
return_Value = accum(list_integers)
print(return_Value)


#5
def length(c):
    if len(c) >=5:
        return "Longer than five"
    else:
        return 'Less than five'


lst1=[1,2,3]
l1=[1, 1, 1, 1, 1]
l2=[4, 4, 4, 3, 5, 6, 7, 8, 9]

print(length(l2))
print(length(lst1))
print(length(l1))

#6
def divide(x):
    y = (x/2)
    return y
def sum(x):
    y = x +6
    return y
num = 10
Return_Value_Divided = divide(num)
Return_Value_Sum= sum(Return_Value_Divided)
print(Return_Value_Sum)