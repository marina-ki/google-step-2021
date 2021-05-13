
def sort_dictionary(dictionary):
    new_dictionary = []
    for word in dictionary:
        new_dictionary.append((''.join(sorted(word)), word))
    new_dictionary.sort(key=lambda x: x[0])
    return new_dictionary


def find_word(random_word, new_dictionary):
    sorted_random_word = ''.join(sorted(random_word))

    left = 0
    right = len(new_dictionary)

    # 二分探索
    while right > left:  # 上限と下限が反転するまで探索
        pivot = (right + left)//2
        if new_dictionary[pivot][0] < sorted_random_word:  # 小さければ下限を変更
            left = pivot + 1
        else:  # その他はここ
            right = pivot - 1

    if new_dictionary[pivot][0] != sorted_random_word:
        return []
    else:
        # 一致する回答すべて探す
        res = []
        i = pivot
        while i < len(new_dictionary) and new_dictionary[i][0] == sorted_random_word:
            a = new_dictionary[i][1]
            if a != random_word:
                res.append(a)
            i += 1
        return res


def main():
    f = open('words.txt', 'r')
    data = f.read()
    f.close()

    print("文字を入力してください\n")
    random_word = input()

    dictionary = data.splitlines()
    new_dictionary = sort_dictionary(dictionary)
    anagram = find_word(random_word, new_dictionary)
    if len(anagram) > 0:
        print(anagram)
    else:
        print("nothing found.")


main()
