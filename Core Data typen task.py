'''#1
L=[101,205,304,405,502,100]
print(L.index(304))
#2
l1=L
l1.remove(max(L))
print(max(l1))
#3
l2=L
l1.remove(min(L))
print(min(l1))
#4
L = [64, 34, 25, 12, 22, 11, 90,11]
for i in range(len(L)):
    for j in range(len(L)-i-1):
        if L[j]>L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print(L)
#5
L=list(set(L))
print(L)
#6
L=[1,2,3,5,6]
for i in range(len(L)-1):
    if i+1==L[i]:
        pass
    else:
        print(i+1)
#7
A=[10,20,30,40]
B=[30,40,50,60]
for i in A:
    for j  in B:
        if i==j:
            print(i)
#8
L = [0, 5, 0, 3, 8, 0, 2]
non_zeros = [x for x in L if x != 0]
zero_count = L.count(0)
output = non_zeros + [0] * zero_count
print("Output:", output)
#9
L=[10,20,50,20,30]
S=set(L)
for i in S:
    print(i,L.count(i))
#10
L = [64, 34, 25, 12, 22, 11, 90,11]
print("Max",max(L))
print("Min",min(L))
print("Avg",sum(L)/len(L))
#11
L=(101,205,304,405,502,100)
print(L.index(304))
#12
L = (64, 34, 25, 12, 22, 11, 90,11)
print(tuple(sorted(L)))
#13
L = (64, 34, 25, 12, 22, 11, 90,11)
print("Max",max(L))
print("Min",min(L))
#14
L=(10,20,50,20,30)
S=set(L)
for i in S:
    print(i,L.count(i))
#15
L=tuple(set(L))
print(L)
#16
A=(10,20,30,40)
B=(30,40,10,20)
if set(A)==set(B):
    print("Equal")
else:
    print("False")
#17
A=(10,20,30,40)
B=(30,40,10,20)
for i in A:
    for j  in B:
        if i==j:
            print(i)
#18
L=(30,40,10,20)
L=tuple(set(L))
for i in range(3):
    print(L[i])
#19
employees = (("E101", "Arun", 45000), ("E102", "Priya", 52000), ("E103", "Kumar", 48000))
h = max(employees, key=lambda emp: emp[2])
print(h)
#20
print(sorted(employees, key=lambda emp: emp[2]))
#21
A = {"Python", "Java", "SQL", "Git"}
B = {"Python", "SQL", "HTML", "Git"}
print(A&B)
#23
A= {101, 102, 103, 104, 105}
B= {101, 103, 105}
print(A.intersection(B))
#24
S=[10,20,30,10,20,40]
L=set(S)
for i in L:
    if S.count(i)>1:
        print(i)
#27
S={"Arun","Priya","Kumar"}
D={"Priya","Divya","Rahul"}
print("BOTH :",S.intersection(D))
print("Python ONLY :",D.difference(S))
print("Java ONLY :",S.difference(D))
#22
print("Unique :",len(S.union(D)))
#25
A = {"Python", "SQL"}
B = {"Java", "SQL", "Git"}
print(A.union(B))
#26
print(A.difference(B))
#28
A= [101, 102, 103, 104, 105,101]
print(len(set(A)))
#29
A = {"Python", "SQL"}
B = {"Java", "SQL", "Git","Python"}
if A.issubset(B):
    print("Pass")
else:
    print("Fail")
#30
A= {101, 102, 103, 104, 105}
B= {101, 103, 105}
print(A.intersection(B))
'''
#31
e={101:'Arun',102:'Gowtham',103:'Raj'}
print(e[102])

#32
a={"Arun": 45000, "Priya": 52000, "Kumar": 48000, "Divya": 60000}
h = max(a, key=a.get)
print(f"{h} with salary {a[h]}")

#33
h=dict(sorted(a.items(),key=lambda i : i[1]))
print(h)

#34
print(dict(sorted(a.items())))
