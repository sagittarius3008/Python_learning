# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_for_step2
# 解答例
# n = int(input())

# flag = False

# for i in range(n):
#     a = int(input())
#     if a == 7:
#         flag = True

# if flag:
#     print("YES")
# else:
#     print("NO")
    
# # 書いたコード(一度目)
# count = int(input())

# for (a, i) in enumerate(range(count)):
#     b = input().split()
#     if str(7) in b:
#         print("YES")
#         break
#     else:
#         if (a+1) == count:
#             print("NO")
            
# 書いたコード(二度目)            
count = int(input())
box = []
for i in range(count):
    box.append(input())
    
if str(7) in box:
    print("YES")
else:
    print("NO")