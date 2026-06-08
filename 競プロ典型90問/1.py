# https://atcoder.jp/contests/typical90/tasks/typical90_a

# 入力を受けとる
n, l = map(int, input().split()) # 切れ目の数，羊羹の長さ
k = int(input()) # 選ぶ切れ目の数
a = list(map(int, input().split())) # 切れ目の位置

a.append(l) # 羊羹の右端も切れ目の位置に追加する

# 切り込み間の長さをdifferenceに保持
difference = [a[0]]
for i in range(n):
    difference.append(a[i+1]-a[i])

# 二分探索によりスコアが最大となるものを探索
def binary_search(left, right): # 範囲の最小値，最大値を受け取り，スコアを返す
    mid = (left + right) //2
    if (mid == left):
        return left
    if is_ok(mid):
        return binary_search(mid, right)
    else:
        return binary_search(left, mid)

def is_ok(mid): # そのスコアが条件を満たすかチェックする
    count = 0
    current_length = 0
    for length in difference:
        current_length = current_length + length
        if current_length >= mid: # 合計が現在テストしている長さ以上になった時点でcountを上げて今までの長さの合計をリセットする
            count = count + 1
            current_length = 0
    return (count >= k + 1)


print(binary_search(0,l))