import numpy as np
import sys

points = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]


def calculate_score(word):
    score = 0
    for character in list(word):
        score += points[ord(character) - 97]
    return score


def hash_word(word):
    a = [0] * 26
    sum = 0
    for i in word:
        # ord('a')=97, ord('z')=122
        a[ord(i)-97] += 1
        sum += points[ord(i) - 97]
    return a, sum


def hash_dictionary(dictionary):
    new_dictionary = []
    for word in dictionary:
        a, sum = hash_word(word)
        new_dictionary.append((a, word, sum))
    # 合計点数の小さい順に並べる
    new_dictionary.sort(key=lambda x: x[2])
    return new_dictionary


def find_word(random_word, new_dictionary):
    hashed_word, hash_sum = hash_word(random_word)
    max_point = 0
    anagram = ""

    # random_wordすべてを使った時の合計点より小さいところから探す
    # 二分探索
    left = 0
    right = len(new_dictionary)
    while right > left:  # 上限と下限が反転するまで探索
        pivot = (right + left)//2
        if new_dictionary[pivot][2] > hash_sum:  # 大きければ上限を変更
            right = pivot - 1
        else:  # その他はここ
            left = pivot + 1

    while pivot >= 0:
        i = new_dictionary[pivot]

        # 辞書は合計点でsortしてあるので、max_pointよりも小さくなったらもう探さない
        if max_point > i[2]:
            break

        # random_wordと一致する時はanagramではないので飛ばす
        if i[1] == random_word:
            pivot -= 1
            continue

        # anagramかどうかチェック
        is_anagram = True
        for j in range(26):
            if hashed_word[j] < i[0][j]:
                is_anagram = False
                break
        if is_anagram == False:
            pivot -= 1
            continue

        point = calculate_score(i[1])
        if point > max_point:
            max_point = point
            anagram = i[1]
        pivot -= 1

    return anagram


def main():

    input_f = sys.argv[1]
    output_f = sys.argv[2]
    f = open('words.txt', 'r')
    data = f.read()
    f.close()
    dictionary = data.splitlines()
    new_dictionary = hash_dictionary(dictionary)

    f = open(input_f, 'r')
    data = f.read()
    f.close()
    inputs = data.splitlines()

    f = open(output_f, 'w')
    res = []

    for i in inputs:
        res.append(find_word(i, new_dictionary))
    f.writelines('\n'.join(res))
    f.close()


main()
