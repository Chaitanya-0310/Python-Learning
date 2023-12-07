

x="Hello"
print("X",id(x))
y= "Hello"
print("Y",id(y))
z= x
print("z",id(z))

print(x is y)  #-> T
print(x == y)  #-> T
print(x is z)  #->T
print(x == z)  #-> T


x= []
print("X",id(x))
y= []
print("Y",id(y))
z= x
print("z",id(z))

print(x is y)  #-> F
print(x == y)  #->T
print(x is z)  #->T
print(x == z)  #-> T