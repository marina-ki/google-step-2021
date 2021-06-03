# week4 の Haruka Kobayashi さんのコードレビュー

## 対象のコード

https://github.com/haruponponpopon/STEP/tree/week4

## 全体のレビュー

- 私の環境でも動きました！
- 機能ごとに関数を分離していて、すっきりしていてよかったです。
- 変数名がわかりやすく、「これから何をするか」のコメントも適宜あって読みやすかったです。

## task1.cpp のレビュー

C++がわからないので当たり障りない感想になってしまいますが…！

- 良かった点
  - task1.md に懸念点なども書いてあり、レビューする側がアドバイスしやすい形になっていてよかったです。
- 改善できるかもしれない点
  - search_ID 関数は、start_page と goal_page を渡すようにしてしまうと汎用性が低いので、探したい page を配列で渡すようにしたらより良さそうです！

### task1.py のレビュー

- 良かった点
  - `raise ValueError("error!")`を使って関数内でエラーを発生させている。
- 改善できるかもしれない点
  - serach_ID 関数内の`for ID, page in pages.items():`の箇所ですが、`id`のように小文字始まりにしたほうが良さそうです。
    - 参考：https://qiita.com/naomi7325/items/4eb1d2a40277361e898b

---

本質的でない話ですが、気付きがあったのでメモ程度に書いておきます！
普段自分は無限ループのときに`while True`を使っているのですが、Haruka さんが`while 1`を使っていて、何が違うんだろう？と気になり調べてみました。

https://stackoverflow.com/questions/3815359/while-1-vs-whiletrue-why-is-there-a-difference-in-python-2-bytecode

python2 のときは True というのはただの定数だったので、

- もし`True = 0`とするようなコードがあったらバグが発生してしまう
- True という定数を呼び出すのに時間がかかる
  などの懸念点から`while 1`を使うことが一般的だったみたいです。

ですが、python3 では True が組み込み定数になり、python2 の懸念点がなくなり、`while True`のほうが一般的になったみたいです。(可読性のため？)
