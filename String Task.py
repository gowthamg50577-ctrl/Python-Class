#1
s=input("Enter a str")
print(len(s))
#2
print(s[::-1])
#3
if s==s[::-1]:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
#4
s.lower()
d=s.count("a")+s.count("e")+s.count("i")+s.count("o")+s.count("u")
print(d)
#5
print(len(s)-d)
#6,7
c,f=0,0
for i in s:
    if i.isdigit():
        c+=1
    if i.isspace():
        f+=1
print(c,f)
#8
a=input("Enter str2")
print(s.count(a))
#9
s=input("Enter a str")
l=s.split()
print("".join(l))
#10
print(s.swapcase())
#11
s=input("Enter a str")
l=s.split()
print(len(l))
#12,22
print(max(l))
#13

d=set(s)
a=[]
for i in s:
    if i not in a:
        print(i,end="")
        a.append(i)
    print()
#14
for i in s:
    print(i,s.count(i))
#15
s=input("Enter a str")
for i in s:
    if s.count(i)>1:
        print(i)
        break
#16
for i in s:
    if s.count(i)==1:
        print(i)
        break
#17
d=input("Enter a str")
if set(s)==set(d):
    print("Its a anagram")
else:
    print("Its not a anagram")
#19
s=input("Enter a str")
l=list(s)
for i in range((len(l)-1),-1,-1):
    print(l[i],end="")
#18
s=input("Enter a str")
l=s.split()
print(" ".join(l[::-1]))
#20
for i in s:
    if i.lower() in 'aeiou':
        pass
    else:
        print(i,end="")
#21
d=input("Enter a str")
print(set(s).issubset(set(d)))
#23
s=input("Enter a str")
d=set(s)
a=[]
for i in s:
    if i not in a:
        print(i,s.count(i),end="")
        a.append(i)
print()
#24;
if len(s)>=8 and any(i.isupper() for i in s) and any(i.islower() for i in s) and any(i.isdigit() for i in s):
    print("Correct")
else:
    print("Error")
#25
if "@" in s and s.startswith("@")==False and "." in s and s.index("@")<s.index("."):
    print("Valid")
else:
    print("Invaild")
#17
s=input("Enter a str")
d=input("Enter a str")
s.lower()
d.lower()
if sorted(s)==sorted(d):
    print("Anagram")
else:
    print("Its not a anagram")