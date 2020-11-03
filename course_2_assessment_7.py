
def mult(a, b = 6):
    m = a*b
    return m 
print(mult(2))

#2
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

#3
def sum(intx, intz = 5):
    soma =  intz + intx
    return soma
print(sum(2))

#4
def test(x, abool = True, dict1 = {2:3, 4:5, 6:8}):
    return abool and dict1.get(x, False)

#5
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return True 
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return False

#6

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('peas')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans= checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('potatos', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
