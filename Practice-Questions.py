'''
    *
  * * *
* * * * *
  * * *
    *
'''
for i in range(1,6,2):
    for sp in range(6,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('')
for i in range(3,0,-2):
    for sp in range(6,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('')
'''
1010101
 10101
  101
   1
'''
for i in range(7,0,-2):
    for sp in range(i,6,1):
        print(' ', end='')
    for j in range(1,i+1):
        if j%2==0:
            print("0",end='')
        else:
            print("1",end='')
    print('')
'''
*
**
***
****
*****
****
***
**
*
'''
for i in range(1,6):
    print("*"*i)
for i in range(4):
    for j in range(4-i):
        print("*",end="")
    print('')
'''
1
3 2
6 5 4
10 9 8 7
'''
start,stop=1,2
current_num=stop
for r in range(2,6):
    for c in range(start,stop):
        current_num-=1
        print(current_num,end=' ')
    print("")
    start=stop
    stop+=r
    current_num=stop
'''
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''
for i in range(0,5):
    n=i+1
    inc=4
    for j in range(0,i+1):
        print(n,end=' ')
        n+=inc
        inc-=1
    print('')
'''
* * * * * * *
* * * * *
* * *
*
* * *
* * * * *
* * * * * * *
'''
for i in range(7,1,-2):
    for j in range(0,i):
        print('* ',end='')
    print('')
for i in range(1,8,2):
    for j in range(0,i):
        print('* ',end='')
    print('')
'''
1 2 3 4 5 6
2 3 4 5 6
3 4 5 6
4 5 6
5 6
6
'''

'''
        0
      1 0 1
    2 1 0 1 2
  3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4
'''
for i in range(0,5):
    for sp in range(6,i,-1):
        print(' ',end=' ')
    for d in range(i,-1,-1):
        print(d,end=' ')
    for a in range(1,i+1):
        print(a,end=' ')
    print('')
'''
ABCDEFGFEDCBA
ABCDEFFEDCBA
ABCDEEDCBA
ABCDDCBA
ABCCBA
ABBA
AA
'''
for i in range(71,64,-1):
    for j in range(65,i+1):
        print(chr(j),end='')
    for k in range(i,64,-1):
        print(chr(k),end='')
    print('')
'''
#*#*#*#*#
*#*#*#*#
#*#*#*
*#*#*
#*#
*#
#
'''
for i in range(6,-3,-1):
    for j in range(1,i+4):
        if i%2==0:
            if j%2==0:
                print("*",end='')
            else:
                print("#",end='')
        else:
            if j%2!=0:
                print("*",end='')
            else:
                print("#",end='')
    print('')
'''
 ***
*   *
*   *
*****
*   *
*   *
*   *
'''
for r in range(0,7):
    for c in range(0,7):
        if (((c==1 or c==5) and r!=0) or ((r==0 or r==3) and (c>1 and c<5))):
            print('*',end='')
        else:      
            print(' ',end='')
    print('')
# Highest Common Factor of two given numbers:
n1=int(input("Enter smaller number: "))
n2=int(input("Enter larger number: "))
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print("Highest Common Factor:",hcf)
