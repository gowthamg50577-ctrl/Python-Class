#1
print(800+1200-150)
#2
print(180*5)
#3
print(25000+3500-1200)
#4
print(2400/4)
#5
print("Left", 25%5)
print("Shared",25//5)
#6
print(185//60,":",185%60)
#7
print("Avg",(85+90+80)/3)
print("Total",85+90+80)
#8
print("Bill :",250*6)
#9
print(2026-2005)
#11
print("Balence",10000-3750)
#12
print("500 notes",4750//500,"Remaining",4750%500)
#10
print("Simple interset",(50000*6*2)/100)
#13
print("Balence",500-249-99)
#14
print("Discount Amount",(10*60000)/100)
print("Final amount",60000-(10*60000)/100))
#15
print("Distance",60*4,"km")
#16
a=int(input("Enter celsius"))
print((a*(9/5)+32),"F")
#17
a=int(input("Enter roll no"))
if(a%2==0):
    print("Its even")
else:
    print("Its odd")
#18
a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
if(a<b):
    print(b,"is greater")
elif a>b:
    print(a,"i greater")
else:
    print("Both are equal")

#19
a=int(input("Enter attendance:"))
b=int(input("Enter no mark:"))
if(a>=75 and b>=40):
    print("Permit")
else:
    print("Donot permit")
#20
a=int(input("Enter amount:"))
b=bool(input("Enter regular cust or not:"))
if(a>=2000 and b==True):
    print("Give discount")
else:
    print("Donot give discount")

#Smallest number and Largest number 

a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
if(a<b):
    print(b,"is greater")
elif a>b:
    print(a,"i greater")
else:
    print("Both are equal")

#Absolute Value
a=int(input("Enter no 1:"))
if a>0:
    print(a)
else:
    print((~a)+1)


#Smallest Number
a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
if(a<b):
    print(a)
else:
    print(b)

#Largest number
a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
if(a<b):
    print(b)
else:
    print(a)
#odd or even
a=int(input("Enter  no"))
if(a%2==0):
    print("Its even")
else:
    print("Its odd")

#Multiple of 5
a=int(input("Enter  no"))
if(a%5==0):
    print("Its multiple of 5")
else:
    print("Its not a multiple of 5")

#Multiple of 10
a=int(input("Enter no"))
if(a%10==0):
    print("Its multiple of 10")
else:
    print("Its not a multiple of 10")

#is it two digit number or not
a=int(input("Enter no"))
if((a/10)<=10 and (a/10)>=1):
    print("Its 2 digit")
else:
    print("Its not 2 digit")
    
#is it three digit number or not
a=int(input("Enter no"))
if((a/10)<=100 and (a/10)>=10):
    print("Its 3 digit")
else:
    print("Its not 3 digit")

#Ends with 0
a=int(input("Enter no"))
if (a%10)==0:
    print("It ends with 0")
else:
    print("It doesnot end with 0")

#Square comparison
a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
if(a<b):
    print(b,"is greater")
elif a>b:
    print(a,"i greater")
else:
    print("Both are equal")
#0 Differnce
a=int(input("Enter no"))
b=int(input("Enter no"))
if (a-b)==0:
    print("Differnce is 0")
else:
    print("Differnce is not 0")

#Marks
a=int(input("Enter no"))
if a>=50:
    print("Pass")
else:
    print("Fail")

#Divisable by 10
a=int(input("Enter no"))
if (a%10)==0:
    print("Its divisable by 10")
else:
    print("Its not divisable by 10")

#Biggest digit
a=int(input("Enter no 1:"))
if(a//10)>(a%10):
    print(a//10,"is greater")
elif (a//10)<(a%10):
    print(a%10,"is greater")
else:
    print("Both are equal")
#15
a=int(input("Enter no"))
if a==1:
    print("Easy")
else:
    print("hard")
#16
a=int(input("Enter no"))
if a==1:
    print("Can play")
else:
    print("Can't play")
#17
a=int(input("Enter no"))
b=int(input("Enter no"))
if a==b:
    print("Square")
else:
    print("Rectangle")
#18
a=int(input("Enter no"))
if a>=75 and a<=90:
    print("Its a upper ch")
else:
    print("Its not a upper char")
#19
a=int(input("Enter no"))
if a>=97 and a<=122:
    print("Its a lower ch")
else:
    print("Its not a lower char")
#20
a=int(input("Enter no"))
if a>=48 and a<=57:
    print("Its numeric")
else:
    print("Its not numeric")
#21
a=int(input("Enter no"))
if a%5==0 and a%3==0:
    print("Its multiple of 5 and  3")
else:
    print("Its not multiple of 5 and 3")
#22
a=int(input("Enter no"))
if((a/10)<=100 and (a/10)>=10) and a%10==0:
    print("Its 3 digit and multiple of 10")
else:
    print("Its not 3 digit")
#23
a=int(input("Enter no"))
if a%5==0 and a%3==0 and a%10==0:
    print("Its multiple of 5 ,3,10")
else:
    print("Its not multiple of 5 ,3,10")
#24
a=int(input("Enter  no 1"))
b=int(input("Enter no 2"))
if(a%2==0)and (b%2==0):
    print(a*b)
else:
    print(a+b)

#25
a=int(input("Enter a no"))
if a%10==7 or a%7==0:
    print("Its a Buzz no")
else:
    print("Its not a Buzz no")

#Part-2 
#1
a=int(input("Enter a no"))
b=int(input("Enter a no"))
c=int(input("Enter a no"))
if a>=b and a>=c:
    if a==b==c:
        print("All are equal")
    else:
        print(a,"is greatest")
elif b>=a and b>=c:
    print(b,"is greatest")
else:
    print(c,"is greatest")
#2
a=int(input("Enter a no"))
b=int(input("Enter a no"))
c=int(input("Enter a no"))
if a<=b and a<=c:
    if a==b==c:
        print("All are equal")
    else:
        print(a,"is smallest")
elif b<=a and b<=c:
    print(b,"is smallest")
else:
    print(c,"is smallest")
#3
a=int(input("Enter a no"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print(0)

#4
a=int(input("Enter a no"))
if a<=5:
    print("Fine",40*a)
elif a>5 and a<=10:
    print("Fine",((a-5)*65)+5*40)
else:
     print("Fine",(5*65)+(5*40)+((a-10)*80))
#5
a=int(input("Enter a no"))
b=int(input("Enter a no"))
c=input("Enter operator")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)    
elif c=='/':
    print(a/b)
else:
    print("Wrong input")
#6
a=int(input("Enter no"))
if a%5==0 and a%3==0 and a%7==0:
    print("Its multiple of 5 ,3,7")
else:
    print("Its not multiple of 5 ,3,7")

#7
a=int(input("Enter a no"))
c=input("Enter Exp or od")
if c=='o':
    if a<=5:
        print("Fine",50*a)
    elif a>5 and a<=10:
        print("Fine",((a-5)*40)+5*50)
    else:
        print("Fine",(5*50)+(5*40)+((a-10)*30))
elif c=='e':
    if a<=5:
        print("Fine",80*a)
    elif a>5 and a<=10:
        print("Fine",((a-5)*70)+5*80)
    else:
        print("Fine",(5*70)+(5*80)+((a-10)*50))
else:
    print("Wrong input")

#8
a=int(input("Enter a price"))
d=0
if a<=25000:
    d=5
elif a>25000 and a<=50000:
    d=10
elif a>50000 and a<=100000:
    d=15
else:
    d=20
print("Price: ",a)
print("Discount: ",(a*d)/100)
print("Total price: ",a-(a*d)/100)