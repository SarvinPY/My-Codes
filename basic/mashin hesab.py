# n=float(input())
# n1=input()
# m=[]
# m.append(n)
# m.append(n1)
# while n1!='=':
#     n=float(input())
#     m.append(n)
#     n1=input()
#     m.append(n1)
# m.pop()
# while len(m)!=1:
#     if '**' in m :
#         a=m.index('**')
#         c=m[a-1]**m[a+1]
#         m.remove(m[a])
#         m.remove(m[a])
#         m.remove(m[a-1])
#         m.insert(a-1,c)
#     if '+' in m :
#         a=m.index('+')
#         c=m[a-1]+m[a+1]
#         m.remove(m[a])
#         m.remove(m[a])
#         m.remove(m[a-1])
#         m.insert(a-1,c)
# print(m[0])
# print(f'anserw is {s}')
n = input().split()
for item in n :
    