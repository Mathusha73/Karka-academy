#1
num=int(input("Enter the number:"))
if(num>0):
    print(num,"is a positive number")
else:
    print(num,"is a negative number")

#2
a=int(input("Enter a value:"))
if (a%2==0):
    print(a,"is a Even number")
else:
    print(a,"is a Odd number")

#3
def power():
   a=int(input("Enter the base value:"))
   b=int(input("Enter the exponent value:"))
   exp=a**b
   print("The power of the given number is:",exp)
   return
power()

#4
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
if x>y:
    print(x,"is greater than",y)
elif y>x:
    print(y,"is greater than",x)
else:
    print("Both are equal")

#5

#leap year
year=int(input("Enter the year:"))
if (year%4==0 and year%100==0) or (year%400):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year") 

6

score=int(input("Enter the score:"))
if score>=90 and score<=100:
    print("A grade")
elif score>=80 and score<=89:
    print("B grade")
elif score>=70 and score<=79:
    print("C grade")
elif score>=60 and score<=69:
    print("D grade")
else:
    print("F grade")
    
#7

age=int(input("Enter your age:"))
if age<16:
    print("You can't drive")
elif age>=16 and age<=17:
    print("You can drive but not vote")
elif age>=18 and age<=24:
    print("You can vote but not rent a car")
elif age>25:
    print("You can do pretty much anything")
    
#8

x=int(input("Enter a number:"))
if (x%3==0 and x%5==0):
    print("FizzBuzz")
elif x%3==0:
    print("Fizz")
elif x%5==0:
    print("Buzz")
else:
    print("This number is not divisible by 3 and 5")
    
#9

#leap year
year=int(input("Enter the year:"))
if(year%4==0 and year%100!=0)or (year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
    





