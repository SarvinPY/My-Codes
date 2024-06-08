n=int(input())
a=[]
b=[]
for i in range(n+4):
    m=input().split()
    a.append(m)
for j in range(len(a)):
    for i in range(2):
            b.append(a[j][i])

a1=b.index('Gen')
a2=b.index('-',a1)
a3=b.index('Base')
a4=b.index('-',a3)
a5=b.index('Pro')
a6=b.index('-',a5)
a7=b.index('Opt')
b1=[]
b2=[]
b3=[]
b4=[]
for i in range(a1+1,a2):
     b1.append(b[i])
for i in range(a3+1,a4):
     b2.append(b[i])
for i in range(a5+1,a6):
     b3.append(b[i])
for i in range(a7+1,len(b)):
     b4.append(b[i])
e=0
e1=0
e2=0
e3=0
for i in range(1,len(b1),2):
     e=e+int(b1[i])
for i in range(1,len(b2),2):
     e1=e1+int(b2[i])
for i in range(1,len(b3),2):
     e2=e2+int(b3[i])
for i in range(1,len(b4),2):
     e3=e3+int(b4[i])
s=22-e
s1=21-e1
s2=63-e2
s3=30-e3
print('Gen : %i'%(s))
print('Base : %i'%(s1))
print('Pro : %i'%(s2))
print('Opt : %i'%(s3))
      