# 入力された文字を＋で囲う
a = input()
length = len(a)

def line(length):
    for i in range(length + 2):
        print("+", end="")
        
line(5)
print()
print("+" + a + "+")
line(5)