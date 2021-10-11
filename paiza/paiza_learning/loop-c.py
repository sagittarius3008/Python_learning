# map:全ての要素に対して一括して処理を行う
# ただし、多くの場合list内包表記やlambda式で代用可能。
# コードが簡潔で見やすい場合が多い。
# N, M, K = map(int, input().split())
N, M, K = [int(s) for s in input().split()]
print(type(N))
print(M)
print(K)
for i in range(N):
    a = [int(j) for j in input().split()]
    ans = 0
    for j in range(M):
        if a[j] == K:
            ans += 1
    print(ans)



[count, num, point] = input().split()

for i in range(int(count)):
    ans = input().split()
    a = 0
    for j in ans:
        if j == point:
            a += 1
    print(a)