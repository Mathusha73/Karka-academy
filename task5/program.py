#1
for i in range(1,11):
    print(i)

#2
for i in range(1,21):
    if(i%2==0):
        print(i)

#3
for i in range(1,21):
    if(i%2==1):
        print(i)

#4  
n=int(input("Enter a number:"))
fact=1
if n==0:
        print("The factorial of",n,"is",fact)
else:
        for i in range(1,n+1):
            fact=fact*i
        print("The factorial of",n,"is",fact)
        

#5
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)    
        
#6  
list =[10,20,30,40,50]  
sum=0
for i in range(len(list)):
    sum=(sum+list[i])
    avg=sum/len(list)
print("Average=",avg)

#7
#square
rows = 5
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()
    
#triangle
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

diamond    
  
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()  
     
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print() 

#8
for i in range(1,6):
    print(i)
    
#9
for i in range(1,11):
    print(i)

#10
a=[10, 20, 30, 40, 10]
if a[0]==a[-1]:
    print("True")

#11
b=[10,12,15,25,27,32,30,50,56,]
for i in range(len(b)):
    if(b[i]%5==0):
        print(b[i])
        
#12
char = input("Enter a character: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if char in vowels:
    print(char, "is a vowel")
else:
    print(char, "is a consonant")

#13
odd=[]
even=[]
for i in range(10,55):
    if(i%2==0):
       even.append(i)  
    else:
       odd.append(i)
print("The count of odd numbers between 10 and 55 is",len(odd))
print("The count of even numbers between 10 and 55 is",len(even))
    
#14
for i in range(1,26):
    if(i%5!=0):
        print(i)

#15

numbers = [3, 4, 5, 6]  
for num in numbers:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")

#16

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
product = a*b
if product > 500:
    result = a+b
else:
    result = product
print("Result:", result)

#17

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
if a > b:
    print("Greater number is:", a)
else:
    print("Greater number is:", b)

#18
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if (a > b and a>c):
    print("Greater number is:", a)
elif(b>c and b>a):
    print("Greater number is:", b)
else:
    print("Greater number is:", c)

#19

x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
pos = []
neg= []
for n in x:
    if n >= 0:
        pos.append(n)
    else:
        neg.append(n)
print("Positive numbers:", pos)
print("Negative numbers:", neg)





        