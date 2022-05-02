#136
a=int(input('수1: '));b=int(input('수2: '))
dif = a - b
print('dif:',dif)
for dif in range(dif + 1):
    if dif % 2 == 0  :
        print(dif,end=' ')
    else:
        continue
#과제8
a=int(input('\n학번 입력: '));b=input('이름 입력: ');c=int(input('나이 입력: '))

print('학번: ',a);print('이름: ',b);print('나이: ',c)    

#과제11
a=int(input('금액 입력(원화): '))
b= a/1366
print(a,'원 = ',b,'유로')

#과제12
a=int(input('넓이 입력(제곱미터): '))
b=a/3.3
print(a,'제곱미터 =',b,'평')
