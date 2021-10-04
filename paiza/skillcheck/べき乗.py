# inputで256までの数字が渡される
# それが2のほにゃ乗の数字であればOKでなければNG
# a = int(input())
# count = []

# for i in range(8):
#     count.append(2**(i+1)) #この2**(3)という書き方
# print(count)
# if a in count:
#     print("OK")
# else:
#     print("NG")

# 複数回かけようとして失敗した記録
a = int(input())
count = []
summ = []

for i in range(8):
    count.append(i+1)

for j in count:
    total = 1
    while j >0:
        total *= 2
        j -= 1
    summ.append(total)
print(summ)

