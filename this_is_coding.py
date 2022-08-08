# 그리디 예제 3-1 거스름돈
# n = int(input())
# count = 0
#
# coin_types = [500,100,50,10]
#
# for coin in coin_types:
#     count += n // coin
#     n %= coin
# print(count)

# 큰 수의 법칙 - 내 풀이
# import sys
# n,m,k = map(int,sys.stdin.readline().split())      # n,k,m 입력
# data = list(map(int,sys.stdin.readline().split())) # data배열 입력
# data.sort()   # 배열 정렬
# sum = 0       # 합
# count = 0     # k횟수 카운터
# for i in range(m):        # m만큼 반복
#     if count < k:         # court가 k보다 작을 때 최대값 더하기
#         sum += data[n-1]  # 최대값 더하기
#         count +=1         # k가 넘지 않도록 더해주기
#     elif count == k:      # count의 값이 k와 같아질 경우
#         sum += data[n-2]  # 최대값 다음으로 높은값 더하기
#         count = 0         # count 0으로 초기화
# print(sum)                # 결과출력

# 큰 수의 법칙 - 단순하게 푸는 답안 예시
# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int,input().split())
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int,input().split()))
#
# data.sort() # 입력받은 수들 정렬하기
# first = data[n-1] # 가장 큰 수
# second = data[n-2] # 두 번째로 큰 수
#
# result = 0
#
# while True:
#     for i in range(k): # 가장 큰 수를 K번 더하기
#         if m == 0: # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1 # 더할 떄마다 1씩 빼기
#     if m == 0: # m이 0이라면 반복문 탈출
#         break
#     result +=second # 두 번째로 큰 수를 한 번 더하기
#     m -= 1 # 더할 때마다 1씩 뺴기
#
# print(result) # 최종 답안 출력
