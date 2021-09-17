balance = 1000
max_withdraw = 1000000
withdraw = int(input("いくら引き出しますか？"))
if withdraw > max_withdraw:
    print("引き出し額の上限は{}です".format(max_withdraw))
elif balance > withdraw:
    balance -= withdraw
    print(f"{withdraw}円ですね。")
    print(f"今の残高は{balance}円です")
else:
    print(f"残高は{balance}です。引き出しできません。")