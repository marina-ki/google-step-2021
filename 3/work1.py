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
                print('Do not end with * or /')
                raise Exception('Invalid syntax')
            if index - 1 < 0:  # 最初に*または/が来ると、以下の条件分岐がうまく行かない
                print('Do not start with * or /')
                raise Exception('Invalid syntax')
            elif tokens[index - 1]['type'] != 'NUMBER' or tokens[index + 1]['type'] != 'NUMBER':  # 前後が数字でないときはエラー
                print('Please use numbers before and after symbols')
                raise Exception('Invalid syntax')
            elif tokens[index]['type'] == 'DIVIDED' and tokens[index + 1]['number'] == 0:  # 0で割り算しようとしたらエラー
                raise Exception("ZeroDivisionError")
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


def evaluate_plus_and_minus(tokens):
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
                print('You can only use number,+,-,* or /')
                raise Exception('Invalid syntax')
        index += 1
    return answer


def evaluate(tokens):
    solved_times_and_divided = evaluate_times_and_divided(tokens)
    actual_answer = evaluate_plus_and_minus(solved_times_and_divided)
    return actual_answer


def test(line, expect_error=False):
    try:
        tokens = tokenize(line)
        actual_answer = evaluate(tokens)
        expected_answer = eval(line)
        if expect_error == False:
            if abs(actual_answer - expected_answer) < 1e-8:
                print("PASS! (%s = %f)" % (line, expected_answer))
            else:
                print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))
        else:
            print("FAIL! (%s should be ERROR)" % line)
    except Exception as e:
        if expect_error == True:
            print("PASS! (%s)" % e)


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")

    # 足し算
    # 整数
    test("1")
    test("1+2")
    test("1+2+3")
    test("1+2+3+10000000")
    # 小数
    test("1.0")
    test("1.2+2.3+3.4")
    test("1.2+2.3+3.4+10000000.5")
    # 整数と小数
    test("1.2+2+3.4+4+5+6.5+7+8+9+10000000")

    # 引き算
    # 整数
    test("-1")
    test("-1-2")
    test("-1-2-3")
    test("-1-2-3-10000000")
    # 小数
    test("-1.0")
    test("-1.1-2.0-3.0")
    test("-1.2-2.0-3.0-10000000.0")
    # 整数と小数
    test("-1.0-2-3.0-4-5-6.5-7-8-9-10000000")

    # 足し算と引き算(整数、小数混ぜる)
    # 最初がプラス
    test("1-3")
    test("3-1")
    test("3-1.0")
    test("3.0-1")
    test("1.0+2-3.0+4+5+6.5-7+8+9-10000000")
    # 最初がマイナス
    test("-1+3")
    test("-3+1")
    test("-3+1.0")
    test("-3.0+1")
    test("-1.0+2-3.0+4+5+6.5-7+8+9-10000000")

    # 掛け算
    # 整数
    test("2*3")
    test("0*5")  # 0がある
    test("2*5*6")  # 3つ以上
    test("2*5*6*9*10000000")  # 複数個・大きい数
    test("10000000*6*2*4")  # 大きい数字からかけると桁落ちするかもしれないので一応試す
    # 小数
    test("2.0*3.5")
    test("0.0*5.2")  # 0.0がある
    test("2.0*5.0*6.0")  # 3つ以上
    test("2.3*5.5*6.2*9.0*10000000.0")  # 複数個・大きい数
    test("10000000.0*6.4*2.6*4.3")  # 大きい数字からかけると桁落ちするかもしれないので一応試す
    # 整数、小数
    test("10000000*6.0*2*4.0")
    test("10000000.0*6*2.0*4")
    test("10000000.0*0*2.0*4")  # 0を含む
    test("10000000.0*0.0*2.0*4")  # 0.0を含む

    # 割り算
    # 整数同士
    test("4/2")  # 答えが整数
    test("2/3")  # 答えが小数(かつ、答えが0.1以下")
    test("8/4/2")  # ３つ以上、割り切れる
    test("8/3/2")  # ３つ以上、割り切れない
    test("8/10000000")  # 大きい数で割る
    test("0/100")  # 0を割る
    # 小数同士
    test("4.0/2.0")
    test("8.0/3.0/2.0")
    test("8.0/10000000.0")
    test("0.0/100.0")
    # 整数・小数
    # 整数を小数で割る
    test("4/2.0")  # 答えが整数
    test("2/3.0")  # 答えが小数(かつ、答えが0.1以下")
    test("8/4.0/2.0")  # ３つ以上、割り切れる
    test("8/3.0/2.0")  # ３つ以上、割り切れない
    test("8/10000000.0")  # 大きい数で割る
    test("0/100.0")  # 0を割る
    # 小数を整数で割る
    test("4.0/2")  # 答えが整数
    test("2.0/3")  # 答えが小数(かつ、答えが0.1以下")
    test("8.0/4.0/2")  # ３つ以上、割り切れる
    test("8.0/3/2")  # ３つ以上、割り切れない
    test("8.0/10000000")  # 大きい数で割る
    test("0/100")  # 0を割る

    # 四則演算
    test("1+2-3*4/5")
    test("1.5*3*0.3+2*3.5/5")
    test("1.5*3*0.3+20000*3.5/5")

    # エラーが出ることを確認する
    test("*1", expect_error=True)
    test("/2", expect_error=True)
    test("3+1/0", expect_error=True)
    test("3+1/", expect_error=True)
    test("3+1*", expect_error=True)
    test("3+1/*2", expect_error=True)
    print("==== Test finished! ====\n")


run_test()

while True:
    print('> ', end="")
    try:
        line = input()
        tokens = tokenize(line)
        answer = evaluate(evaluate)
        print("answer = %f\n" % answer)
    except Exception as e:
        print("ERROR!" + e)
