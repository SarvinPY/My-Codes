n=input().split(':')
n=[int(i) for i in n]
n1=input().split(':')
n1=[int(i) for i in n1]
if n[2]>n1[2] :
    s=(60-n[2])+n1[2]
elif n[2]<n1[2]:
    s=(n1[2]-n[2])
else:
     s=0

if n[1]>n1[1]:
    m=(60-n[1])+n1[1]
    if n[2]>n1[2] :
        m=m-1
elif n[1]<n1[1]:
    m=abs(n1[1]-n[1])
    if n[2]>n1[2] :
      m=m-1
elif n[1]==n1[1]:
    m=0
    if n[2]>n1[2] :
        if n[2]==0 and n1[2]==0 :
            m=59
        else:
             m=0
if  n[0]<n1[0]:
    h=abs(n1[0]-n[0])
elif n[0]==n1[0] :
    if n[1]>n1[1] or n[2]>n1[2]:
        h=23
        m=59
    else :
        h=0
else:
    h=abs(abs(n1[0]-n[0])-24)

if (n[1]>n1[1]) and (n[1]!=n1[1]):
    h=h-1
if s<10:
    s2=str(s)
    s='0'+s2
if m<10:
    m2=str(m)
    m='0'+m2
if h<10:
    h2=str(h)
    h='0'+h2
print(f'{h}:{m}:{s}')