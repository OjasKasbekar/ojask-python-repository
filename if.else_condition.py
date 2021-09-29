'''no1 = int(input("Enter no1"))
no2= int(input ("Enter no2"))
if(no1 < no2):
    sum = no1+no2
    print(sum)
elif(no1> 5):
    sub = no1-no2
    print(sub)
else:
    print("Hello")'''
                                    #largest of 3 numbers
'''a= int(input("Enter 3 numbers"))
b= int(input("Enter 3 numbers"))
c= int(input("Enter 3 numbers"))
if(a>b and a>c):
    print("largest no is",a)
elif(a<b and b>c):
    print("largest no is",b)
else:
    print("largest no is",c)'''
def largest(a,b,c):
    if (a > b and a > c):
        print("largest no is", a)
    elif (a < b and b > c):
        print("largest no is", b)
    else:
        print("largest no is", c)
x= int(input("Enter 3 numbers"))
y= int(input("Enter 3 numbers"))
z= int(input("Enter 3 numbers"))
r=largest(x,y,z)





                                  #turning 100
'''n= input("your name")
a= int(input("your age"))
d=2021+(100-a)
print(n,"you will turn 100 in",d)'''
