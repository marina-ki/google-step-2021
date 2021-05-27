# 宿題１

## evaluate_times_and_divided について

例えば `3 + 4 * 2 + 1` の計算のときの挙動について
(type などは省略)

1. index = 0
   `new_tokens = [3]`
2. index = 1
   `new_tokens = [3,+]`
3. index = 2
   `new_tokens = [3,+,4]`
4. index = 3
   `new_tokens`の最後の値->4
   `tokens[index+1]`を見る->3
   -> `new_tokens`の最後の値を `4*3` に更新
   `new_tokens = [3,+,12]`
   ※index+1 の値を計算済みなので、index は２つすすめる
5. index = 5
   `new_tokens = [3,+,12,+]`
6. index = 6
   `new_tokens = [3,+,12,+,6]`

## 工夫した点

エラーを全部`Invalid syntax`にするのではなく、詳細も書くようにして、デバッグしやすいようにした。
