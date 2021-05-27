#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_times(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1


def read_divided(line, index):
    token = {'type': 'DIVIDED'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_times(line, index)
        elif line[index] == '/':
            (token, index) = read_divided(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate_times_and_divided(tokens):  # *と/のみ計算
    new_tokens = []
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'TIMES' or tokens[index]['type'] == 'DIVIDED':
            if index + 1 >= len(tokens):  # index+1が配列の長さ以上になると、以下の条件分岐がうまく行かない
                print('Invalid syntax')
                print('Do not end with * or /')
                exit(1)
            elif tokens[index - 1]['type'] != 'NUMBER' or tokens[index + 1]['type'] != 'NUMBER':  # 前後が数字でないときはエラー
                print('Invalid syntax')
                print('Please use numbers before and after symbols')
                exit(1)
            elif tokens[index]['type'] == 'DIVIDED' and tokens[index + 1]['number'] == 0:  # 0で割り算しようとしたらエラー
                print("ZeroDivisionError")
                exit(1)

            # new_tokensの最後の文字を、掛け算または割り算したあとの値に修正する
            if tokens[index]['type'] == 'TIMES':
                new_tokens[-1]['number'] *= tokens[index+1]['number']
            else:
                new_tokens[-1]['number'] /= tokens[index+1]['number']
            index += 2
        else:
            new_tokens.append(tokens[index])
            index += 1
    return new_tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                print('You can only use number,+,-,* or /')
                exit(1)
        index += 1
    return answer


def test(line):
    tokens = tokenize(line)
    solved_times_and_divided = evaluate_times_and_divided(tokens)
    actual_answer = evaluate(solved_times_and_divided)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    print("==== Test finished! ====\n")


run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    solved_times_and_divided = evaluate_times_and_divided(tokens)
    answer = evaluate(solved_times_and_divided)
    print("answer = %f\n" % answer)
