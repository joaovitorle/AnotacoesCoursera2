#1 Optional Parameters
def f(a, L=[]):
	L.append(a)
	return L
	
print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Hello"]))

#2 Key arguments
initial = 7 
def f(x, y=3, z=initial):
	print('x, y, z, are:', x,y,z)

f(2,3)

#3 Lambda Expressions 
lf = lambda x: x-1 #The return functions is anonymous
print (lf(3))

