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

# 宿題２

## 工夫した点

### 小さいテストケースから網羅するようにした

とにかく単純なものからテストするようにすることで、実装のミスをした際にどこでミスしたのかわかりやすくした。

### エラーもテストした

エラーが出るようなフォーマットをあえて用意して、エラーになったら PASS ということにした。
`exit`だと処理自体を抜けてしまうので、`try except`を使うために`raise Exception`を使った。

例：

```py
    test("*1", expect_error=True)
    test("/2", expect_error=True)
    test("3+1/0", expect_error=True)
    test("3+1/", expect_error=True)
    test("3+1*", expect_error=True)
    test("3+1/*2", expect_error=True)

```

```
Do not start with * or /
PASS! (Invalid syntax)
Do not start with * or /
PASS! (Invalid syntax)
PASS! (ZeroDivisionError)
Do not end with * or /
PASS! (Invalid syntax)
Do not end with * or /
PASS! (Invalid syntax)
Please use numbers before and after symbols
PASS! (Invalid syntax)
```

となる。

### 気になっているところ

- これでも網羅できていない
  - もっと大きい数のときは？
  - 小数ちゃんと.0~.9 まで大丈夫？
- エラーになるときのテストケースが print が入ってきて少し見づらい状態。
