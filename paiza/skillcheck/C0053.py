member = int(input())
card = input().split()

def summ(list):
    sum = 0
    for i in list:
        sum += int(i)
    return sum

def intlist(list):
    for i in range(len(list)):
            list[i] = int(list[i])
    
if "x10" in card:
    card.remove("x10")
    intlist(card)
    if 0 in card:
        card.remove(0)
        card.remove(max(card))
        print(summ(card * 10))
    else:
        print(summ(card * 10))
else:
    intlist(card)
    if 0 in card:
        card.remove(max(card))
        print(summ(card))
    else:
        print(summ(card))