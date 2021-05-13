import numpy as np
points = np.array([1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4])


def hash_word(word):
    a = [0] * 26
    for i in word:
        # ord('a')=97, ord('z')=122
        a[ord(i)-97] += 1
    return a


def hash_dictionary(dictionary):
    new_dictionary = []
    for word in dictionary:
        new_dictionary.append((hash_word(word), word))
    return new_dictionary


def find_word(random_word, new_dictionary):
    hashed_word = hash_word(random_word)
    max_point = 0
    anagram = ""
    for i in new_dictionary:
        if i[1] == random_word:
            continue
        a = np.array(hashed_word)-np.array(i[0])
        if all([aa >= 0 for aa in a]):
            point = sum(np.array(i[0]) * points)
            if point > max_point:
                max_point = point
                anagram = i[1]

    return anagram


def main():
    f = open('myfile.txt', 'r')
    data = f.read()
    f.close()
    dictionary = data.splitlines()
    new_dictionary = hash_dictionary(dictionary)

    f = open('small.txt', 'r')
    data = f.read()
    f.close()
    inputs = data.splitlines()

    for i in inputs:
        anagram = find_word(i, new_dictionary)
        if anagram:
            print(anagram)
        else:
            print("anagramは見つけられませんでした\n")


main()
