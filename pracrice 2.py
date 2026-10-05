#1
a=eval(input("Enter a list"))
a=list(set(a))
print(a)
#2
a=eval(input("Enter a list"))
a=a[1:]+a[:1]
print(a)
#3
a=eval(input("Enter a list"))
k=int(input("Enter a element"))
a=a[k:]+a[:k]
print(a)
#4
a=eval(input("Enter a list"))
a=list(set(a))
if sorted(a)==a:
    print("True")
else:
    print("False")
#5
a=input("Enter a string")
a=a.lower()
c=0
for i in range(len(a)):
    if a[i] in 'aeiou':
        c+=1
print("vowels",c)
#6
a=eval(input("Enter a list"))
c1=0
c2=0
for i in range(len(a)):
    if a[i]%2==0:
        c1+=1
    else:
        c2+=1
d=(c1,c2)
print(d)
#7
a=eval(input("Enter a list"))
b=eval(input("Enter a list"))
a=list(set(a+b))
print(a)
#8
a=eval(input("Enter a list"))
a=list(set(a))
print(a)
#9
a=eval(input("Enter a list"))
b=eval(input("Enter a list"))
c=list(set(a) & set(b))
print(c)
#10
a=eval(input("Enter a list"))
print(min(a),max(a))