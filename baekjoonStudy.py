# # 3046번
# r1, s = map(int,input().split()) # 한줄로 입력받기
# r2 = s*2-r1
# print(r2)

# 2163번
# x, y = map(int, input().split())
# print(x*y-1)

# 11022번
# t = int(input())
# case = []
# for i in range(t):
#     a,b = map(int, input().split())
#     case.append((a,b))
# i = 1
# for j in case:
#     print("Case #"+str(i)+":",j[0],"+",j[1],"=",j[0]+j[1])
#     i += 1

# 10699번
# from datetime import datetime # 현재 시간을 이용하기 위한 참조
# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))
# print(now)
# print(now.date())

# 7287번
# print("31")
# print("dbdudann")

# 2525번 - 오류 / 8.1(해결)
# h, m = map(int,input().split())
# cook = int(input())
# a = cook//60
# b = cook%60
# if m+b <=59:
#     m = m+b
#     if h + a < 24:
#         h = h + a
#     elif 24 <= h + a:
#         h = (h + a)%24
# else:
#     m = m+b
#     c = m//60
#     d = m%60
#     if h+a+c <24 and h+c < 24:
#         h = h+a+c
#     elif 24<= h+a+c:
#         h = (h + a + c) % 24
#     m = d
# print(h,m)

# 2525번 - 정답
# h, m = map(int, input().split())
# c = int(input())
# if c%60+m <60:
#     m = (c%60+m)%60
#     if c//60+h <24:
#         h = c//60+h
#     else:
#         h = (c//60+h)-24
# elif c%60+m >= 60:
#     m = (c%60+m)%60
#     if c//60+h+1 <24:
#         h = c//60+h +1
#     else:
#         h = (c//60+h)-23
# print(h,m)

# 2525번 - 다른 방향
# h, m = map(int, input().split())
# c = int(input())
#
# a = ((c+m)//60+h)%24
# b = (c+m)%60
# print(a, b)

# 2530번 - 포기(뭔가 잘못됨)
# h, m, s = map(int, input().split())
# c = int(input())
# if c%60+s <60:
#     s = (c%60+s)%60
#     if c > 60:
#         c = c - (c%60)
#     if (c//60)%60+m < 60:
#         m = ((c//60)%60+m)%60
#         if (c//60)//60+h < 24:
#             h = ((c//60)//60+h)%24
#         else:
#             h = ((c//60)//60+h-24)%24
#     elif (c//60)%60+m >= 60:
#         m = ((c//60)%60+m)%60
#         if (c//60)//60+h+1 < 24:
#             h = ((c//60)//60+h + 1)%24
#         else:
#             h = ((c//60)//60+h-23)%24
# elif c%60+s >=60:
#     s = (c%60+s)%60
#     if c > 60:
#         c = c - (c % 60)
#     if (c // 60) % 60 + m < 60:
#         m = ((c // 60) % 60 + m + 1) % 60
#         if (c//60)//60+h <23:
#             h = ((c // 60) // 60 + h + 1) % 24
#         elif (c // 60) // 60 + h < 24 and (c // 60) // 60 + h >22:
#             h = ((c // 60) // 60 + h + 1)%24
#         else:
#             h = ((c // 60) // 60 + h - 24)%24
#     elif (c // 60) % 60 + m >= 60:
#         m = ((c // 60) % 60 + m+1) % 60
#         if (c//60)//60+h  <23:
#             h = ((c // 60) // 60 + h + 1) % 24
#         elif (c // 60) // 60 + h< 24 and (c // 60) // 60 + h >22:
#             h = ((c // 60) // 60 + h + 1)%24
#         else:
#             h = ((c // 60) // 60 + h - 24)%24
# print(h,m,s)

# 2530번 - 방법1
# A,B,C = map(int,input().split())
# D = int(input())
#
# A = (A + (B + (C + D)//60) // 60) % 24
# B = (B + (C + D) // 60 ) % 60
# C = (C + D) % 60
# print(A, B, C)

# 2914번 - 방법1
# a, i = map(int, input().split())
# x = a * i
# for j in range(x, 0, -1):
#     if j // a < i-1:
#         x = j
#         print(j+2)
#         break

# 2914번 - 방법2
# a, i = map(int,input().split())
# print(a*(i-1)+1)

# 5355번 - 망한 방법
# t = int(input())
# s = []
# for i in range(t):
#     s.append((input().split()))
#
# for j in s:
#     x = float(j[0])
#     print(j[2])
#     if j[1] == "@":
#         x = x*3
#         if j[2] == "%":
#             x = x + 5
#             if j[3] == "#":
#                 x = x-7
#         elif j[2] == "#":
#             x = x -7
#             if j[3] == "%":
#                 x = x +5
#     elif j[1] == "%":
#         x = x+5
#         if j[2] == "@":
#             x = x*3
#             if j[3] == "#":
#                 x = x-7
#         elif j[2] == "#":
#             x = x -7
#             if j[3] == "@":
#                 x = x *3
#     else:
#         x= x-7
#         if j[2] == "%":
#             x = x+5
#             if j[3] == "@":
#                 x = x*3
#         elif j[2] == "@":
#             x = x *3
#             if j[3] == "%":
#                 x = x +5
#     print("%.2f"%(x))

# 5355번 - 복습1
# t = int(input())
# s = []
# for i in range(t):
#     s.append(input().split())
#
# for i in range(len(s)):
#     x = float(s[i][0])
#     for j in range(1,len(s[i])):
#         if s[i][j] == '@':
#             x *= 3
#         elif s[i][j] == '%':
#             x += 5
#         elif s[i][j] == '#':
#             x -= 7
#         else:
#             print("잘못된 수식")
#     print("%.2f"%x)

# 5355번 - 방법1
# t = int(input())
# s = []
# for i in range(t):
#     s.append(input().split())
#
# for i in range(len(s)):
#     x = float(s[i][0])
#     for j in range(1, len(s[i])):
#         if s[i][j] == "@":
#             x *=3
#         elif s[i][j] == "%":
#             x +=5
#         elif s[i][j] == "#":
#             x -=7
#     print("%.2f"%x)

# 2675번 - 해결
# t = int(input())
# r = []
# s = []
# for i in range(t):
#     rr, ss = map(str, input().split())
#     r.append(rr)
#     s.append(ss)
# for i in range(t):
#     for j in range(len(s[i])):
#         print(s[i][j]*int(r[i]), end='')
#     print()

# 2935번 - 해결
# a = int(input())
# pm = input()
# b = int(input())
#
# if pm == "*":
#     print(a * b)
# else:
#     print(a+b)

# 10817번 - 해결
# a, b, c = map(int, input().split())
# if a >= b:
#     if a >= c:
#         if b >= c:
#             print(b)
#         else:
#             print(c)
#     elif c >= a:
#         print(a)
# else:
#     if b >= c:
#         if a >= c:
#             print(a)
#         else:
#             print(c)
#     elif c >= b:
#         print(b)

# 10817번 - 방법2(sort 이용)
# a = list(map(int,input().split()))
# aa = sorted(a)
# print(aa[1])

# 11653번 - 해결
# n = int(input())
# if n > 1:
#     for i in range(2, n+1):
#         for j in range(n):
#             if n % i == 0:
#                 n = int(n/i)
#                 print(i)
#             elif n % i != 0:
#                 break
#         if 1 == n:
#             break
# else:
#     print()

# 1789번 - 인터넷 정보획득
# s = int(input())
# x = 0
# for i in range(1,s+1):
#     x = x + i
#     if x == s:
#         print(i)
#         break
#     elif x > s:
#         print(i-1)
#         break

# 1789번 - 방법2
# s = int(input())
# for i in range(1,s+2):
#     if i*(i+1)/2 > s:
#         print(i-1)
#         break

# 10039번 - 해결
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# l = [a,b,c,d,e]
# sum = 0
# for i in range(len(l)):
#     if 40>l[i]:
#         l[i] = 40
#     sum += l[i]
# print(int(sum/5))

# 10039번 - 방법2
# import sys
# std = []
# sum = 0
# for i in range(5):
#     std.append(list(map(int,sys.stdin.readline().split())))
#     if std[i][0] > 40:
#         sum += std[i][0]
#     elif std[i][0] < 40:
#         sum += 40
# print(sum//5)

# 1934번 - x
# t = int(input())
# a = []
# b = []
# for i in range(t):
#     o, s = map(int, input().split())
#     a.append(o)
#     b.append(s)
#
# for i in range(t):
#     a1 = []
#     b1 = []
#     if a[i] > 1:
#         for j in range(2, a[i] + 1):
#             for k in range(a[i]):
#                 if a[i] % j == 0:
#                     a[i] = int(a[i] / j)
#                     a1.append(j)
#                 if a[i] % j != 0:
#                     break
#             if 1 == a[i]:
#                 break
#     if b[i] > 1:
#         for j in range(2, b[i] + 1):
#             for k in range(b[i]):
#                 if b[i] % j == 0:
#                     b[i] = int(b[i] / j)
#                     b1.append(j)
#                 if b[i] % j != 0:
#                     break
#             if 1 == b[i]:
#                 break
#     union1 = list(set(a1) & set(b1))
#     union2 = list(set(a1) ^ set(b1))
#     union = union1 + union2
#     print(union1, union2)
#     k = 1
#     for i in range(len(union)):
#         k *= union[i]
#
#     print(k)

# 1934번 - 유클리드 호제법 사용(인터넷)
# def gcd(a,b):
#     while b>0:
#         a,b = b, a%b
#     return a
# def lcm(a,b):
#     return a*b / gcd(a,b)
#
# import sys
# t = int(input())
# a = []
# b = []
# for i in range(t):
#     o, s = map(int, sys.stdin.readline().split())
#     a.append(o)
#     b.append(s)
# for i in range(t):
#     print(int(lcm(a[i],b[i])))

# 2480번 - 해결
# a, b, c = map(int, input().split())
# if a == b and b == c:
#     print(10000+a*1000)
# elif (a == b and b !=c)or(a==c and c !=b)or(c==b and b !=a):
#     if a==b:
#         print(1000+a*100)
#     else:
#         print(1000+c*100)
# else:
#     d = max(a,b,c)
#     print(d*100)

# 4101번 - 해결
# a = []
# b = []
# while True:
#     c, d = map(int, input().split())
#     if c ==0 and d == 0:
#         break
#     a.append(c)
#     b.append(d)
# for i in range(len(a)):
#     if a[i]>b[i]:
#         print("Yes")
#     else:
#         print("No")

# 10156번 - 해결
# k, n, m = map(int, input().split())
# if k*n > m:
#     print(k*n-m)
# elif m >= k*n:
#     print(0)

# 3009번 - 해결
# x = []
# y = []
# for i in range(3):
#     a,b = map(int, input().split())
#     x.append(a)
#     y.append(b)
# if x[0] == x[1] :
#     print(x[2], end=" ")
# elif x[0] == x[2]:
#     print(x[1], end=" ")
# else:
#     print(x[0], end=" ")
# if y[0] == y[1] :
#     print(y[2], end="")
# elif y[0] == y[2]:
#     print(y[1], end="")
# else:
#     print(y[0], end="")

# 3009번 - list.count() 사용시
x = []
y = []
for i in range(3):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(3):
    if x.count(x[i]) == 1:
        print(x[i], end=" ")
    if y.count(y[i]) == 1:
        print(y[i], end=" ")