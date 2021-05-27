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

# 宿題３

## solve_without_brackets について

()のない箇所の計算

## solve_brackets について

### `1+((3+4)/5+2)`のとき

1. index = 0,1

   特に何もせず

2. index = 2

   `(`なので、
   `open_index = [2]`
   になる。

3. index = 3

   `(`なので、
   `open_index = [2,3]`
   になる。

4. index = 4,5

   特に何もせず

5. index = 6

- `)`なので、open_index の最後の値を取り出す->3
- index=3 より大きく index=6 より小さい箇所、つまり`3+4`を solve_without_brackets を用いて計算する->7
- `1+((3+4)/5+2)`を`1+(7/5+2)`に置き換える
- index の位置を`(`の位置、つまり 3 に戻す

#### `1+(7/5+2)`を見て考える。

6. index = 4,5,6,7

   特に何もせず

7. index = 8

- `)`なので、open_index の最後の値を取り出す->2
- index=2 より大きく index=8 より小さい箇所、つまり`7/5+2`を solve_without_brackets を用いて計算する->3.4
- `1+((3+4)/5+2)`を`1+3.4`に置き換える
- index の位置を`(`の位置、つまり 2 に戻す

#### `1+3.4`を見て考える。

8. index = 3

`index < len(tokens)`となり終了。

#### 最後に

solve_without_brackets を用いて計算する->4.4

## テストケースについて

- 四則演算で小数の計算ができていることを確認してあるので、ここでは()の中が小数になるパターンを１つだけ用意した。
