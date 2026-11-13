#1
def reverse(n):
    r=0
    while n!=0:
        k=n%10
        r=r*10+k
        n=n//10
    return r
#print(reverse(123))
#2
def sum1(n):
    r=0
    while n!=0:
        k=n%10
        r=r+k
        n=n//10
    return r
#print(sum1(584))
#3
def prime(n):
    for i in range(2,int(n/2)):
        if n%i==0:
            return "Not Prime"
    return "Prime"
#print(prime(16))
#4
def rprime(n,l):
    k=[]
    for j in range(n,l+1):
        f=0
        for i in range(2,int(j/2)):
            if j%i==0:
                f=1
        if f==0:
            k.append(j)
    return k
#print(rprime(11,30))
#5
def palindrome(n):
    if str(n)==str(n)[::-1]:
        return "Palindrome"
    return " Not  Palindrome"
#print(palindrome(1231))
#6
def reversep(n):
    return n[::-1]
#print(reversep("prpgramming"))
#7
def vowel(n):
    c=0
    for i in n:
        if i.lower() in "aeiou":
            c+=1
    return c
#print(vowel('prpgrammiaong'))
#8
def frequency(n):
    n=n.lower()
    l=[]
    for i in n:
        if i not in l:
            l.append(i)
            print(i,n.count(i))
#frequency("banana")
#9
def nonc(n):
    n=n.lower()
    for i in n:
        if n.count(i)==1:
            print(i)
            break
#nonc("aaaefefefv")
#10
def rdup(n):
    return "".join(dict.fromkeys(n))
#print(rdup("prgggrrh"))
#11
def sl(n):
  largest = float('-inf')
  second = float('-inf')
  for num in n:
    if num > largest:
      second = largest
      largest = num
    elif num > second and num != largest:
      second = num
  return second
#print(sl([10,30,20,22]))
#12
def sl(n):
    d=list(set(n))
    return d
#print(sl([10,30,20,22,22,10]))
#13
def zer(n):
    f=[]
    for i in n:
        if i!=0:
            f.append(i)
    f=f+[0]*n.count(0)
    return f
#print(zer([0,5,8,0,2,0,0]))
#14
def mis():
    n=int(input())
    l=list(input())
    for i in range(1,n+1):
        if str(i) not in l:
            print(i)
#mis()
#15
def pair():
    l=list(map(int,input().split()))
    i=0
    while i!=len(l):
        if l[i]+l[i+1]==9:
            print(l[i],l[i+1])
        i=i+2
#pair()
#16
def ana():
    n=input()
    l=input()
    if set(n)==set(l):
        return "Analgrom"
    return "Not Analgrom"
#print(ana())
#17
def frequency1(n):
    n=n.lower()
    l=[]
    for i in n:
        if i not in l:
            l.append(i)
            print(f"{i}{n.count(i)}",end='')
#frequency1("aaassd")
#18
def left(n):
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            print(n[i],end=" ")
    print(n[len(n)-1])
left([16,17,4,3,5,2])
#19
def dict1():
    n = {}
    for _ in range(4):
        name, val = input().split()
        n[name] = int(val)
    print("Highest", max(n,key=n.get), n[max(n,key=n.get)])
    n.pop(max(n,key=n.get))
    print("2 Highest", max(n,key=n.get), n[max(n,key=n.get)])
dict1()
