# listのメソッド
# .append:listの一番後ろに追加
# .insert:listの指定した位置に追加。第一引数の前に追加する。第二引数が追加するオブジェクト
# .remove:マッチした最初のオブジェクトを除く
# .sort:昇順に並び替える。引数にreverse=Trueとすると降順に。
# len:リストの要素数を取得する(length)ビルトインメソッド

# if.pyをlistを使って無理やりリファクタ。わかりにくい。
balance_list = [1000,1000000]
balance_list.append(int(input("いくら引き出しますか？")))
if balance_list[0] > balance_list[1]:
    print("引き出し額の上限は{}です".format(balance_list[1]))
elif balance_list[0] > balance_list[2]:
    balance_list[0] -= balance_list[2]
    print(f"{balance_list[2]}円ですね。")
    print(f"今の残高は{balance_list[0]}円です")
else:
    print(f"残高は{balance_list[0]}です。引き出しできません。")

print(len(balance_list))