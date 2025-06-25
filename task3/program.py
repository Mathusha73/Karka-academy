#1
def sayHello(name):
    print("Hello,world",name)
    return
sayHello("Mathusha")

#2
def add(a,b):
    sum=a+b
    return (sum)
c=add(45,40)
print(c)

#3
def multiply(x,y):
    out=x*y
    return (out)
d=multiply(2,4)
print(d)

#4
a=5
b=6
def multiply(a,b):
    mul=a*b
    return mul
print(multiply(5,6))

#5
def div(a,b):
    f=a/b
    print(f)
div(10,3)

#6
def factorial(n):
    if n==0:
        return 1
    ans=n*factorial(n-1)
    return ans
print (factorial(5))

#7
def number(d): #square of a number
    f=d**2
    print(f)
number(7)




    
    