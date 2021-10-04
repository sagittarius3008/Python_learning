# <///+///+<<<///とかを入力
# < = 10, / = 1の足し算

a = input().split("+")
count = 0
length = len(a)
while length > 0:
    for i in list(a[length - 1]):
        if i == "/":
            count += 1
        else:
            count += 10
    length -= 1
print(count)