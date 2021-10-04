# 母音を抜け問題
N = list(input())
list = ["a","i","u","e","o","A","I","U","E","O"]
ans = []
for i in N:
    if i not in list:
        ans.append(i)

print("".join(ans))