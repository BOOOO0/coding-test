import sys

# 부분수열은 주어진 수열의 원소들을 나열해서 만드는 새로운 수열이다 

# !! 순서를 유지하며 !!

# 즉 6개의 숫자가 주어진다면 그 중 오름차순으로 가장 길게 만들 수 있는 수열의 원소들을 뽑는 것이다
# set으로 중복 없애고 길이출력 해보기 --- 틀림

# 이전까지의 DP문제풀이 형식으로 한다면
# 인덱스별로 


N = int(sys.stdin.readline().rstrip())

dp = [0 for i in range(N)]

nums = list(map(int , sys.stdin.readline().split()))

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] :
            dp[i] = dp[j]
    dp[i]+=1

print(max(dp))