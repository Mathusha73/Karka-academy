#1
studentName="Varshini" #camelCase
marks_obtained=88  #snake_case
print(studentName)
print(marks_obtained)

#2
print("Addition of two numbers")
a=403
b=347
print(a)
print(b)
sum=a+b
print("The sum is",sum)

#3
print("To find the area of the circle")
r=int(input("radius=",))
area_of_circle=3.14*(r**2)
print("Area of the circle=",area_of_circle)

#4
print("To find area of the rectangle")
length=int(input("Enter the length:"))
width=int(input("Enter the width:"))
area=length*width
print("The area of the rectangle=",area)

#5
print("Area of a triangle")
base=int(input("Enter the base :"))
height=int(input("Enter the height:"))
area=(height*base)/2
print("Area of the triangle=",area)

#6
print("simple calculator")
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
addition=a+b
subtraction=a-b
multiplication=a*b
division=a/b
print("Addition:",addition)
print("Subtraction:",subtraction)
print("multiplication:",multiplication)
print("Division:",division)


#7
a=20
print(a)
a=30
print(a)
a+=36
print(a)
a-=20
print(a)
a*=2
print(a)
a/=2
print(a)

#8
a=18
print("The value of a=",a)
a+=25
print("The value of a after increment=",a)
a-=23
print("The value of a after decrement=",a)

#9
a=35
b=20
print("The value of a=",a)
print("The value of b=",b)
print(a==b)
print(b>=a)
print(a<=b)
print(a!=b)
print(a>b)
print(b<a)

#10
x=True
y=False
print("x=",x)
print("y=",y)
print(x and y)
print(x or y)
print(not y)

#11
#swap two variables
#swap using third variable
a=25
b=40
print("a=",a)
print("b=",b)
c=a
a=b
b=c
print("After swap using third variable")
print("a=",a)
print("b=",b)

#swap without third variable
a,b=b,a
print("After swap without third variable")
print("a=",a)
print("b=",b)

#12
#average of three numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the second number:"))
average=(a+b+c)/3
print("The average of three numbers=",average)

#13
a = 10
b = 30
c = 12
d = 3
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
output=((a + b) * c) / d
print("output=",output)

#14

tamil=98
english=98
maths=97
science=98
social=100
print("Tamil=",tamil)
print("English=",english)
print("Maths=",maths)
print("Science=",science)
print("Social=",social)
total_mark=(tamil+english+maths+science+social)
average=(total_mark/5)
print("Total mark=",total_mark)
print("Average=",average)









