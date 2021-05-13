
def sort_dictionary(dictionary):
    new_dictionary = []
    for word in dictionary:
        new_dictionary.append((''.join(sorted(word)), word))
    new_dictionary.sort(key=lambda x: x[0])
    return new_dictionary


def find_word(random_word, dictionary):
    sorted_random_word = ''.join(sorted(random_word))
    new_dictionary = sort_dictionary(dictionary)

    left = 0
    right = len(new_dictionary)
    find = False

    # 二分探索
    while right >= left:
        pivot = (right + left)//2
        if new_dictionary[pivot][0] == sorted_random_word:
            find = True
            break
        elif new_dictionary[pivot][0] < sorted_random_word:
            left = pivot + 1
        else:
            right = pivot - 1

    # もし見つけた単語がrandom_wordと一致していたら、その前後を見る
    if new_dictionary[pivot][1] == random_word:
        if pivot+1 < len(new_dictionary) and new_dictionary[pivot+1][1] == random_word:
            pivot += 1
        elif pivot - 1 >= 0 and new_dictionary[pivot-1][1] == random_word:
            pivot -= 1
        else:
            find = False

    anagram = ""
    if find:
        anagram = new_dictionary[pivot][1]

    return anagram


def main():
    f = open('myfile.txt', 'r')
    data = f.read()
    f.close()

    print("文字を入力してください\n")
    random_word = input()

    dictionary = data.splitlines()
    anagram = find_word(random_word, dictionary)
    if anagram:
        print(anagram)
    else:
        print("anagramは見つけられませんでした\n")


main()
