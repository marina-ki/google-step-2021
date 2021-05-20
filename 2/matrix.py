import numpy as np
import sys
import time
import matplotlib.pyplot as plt


def init_matrix(n):  # 行列a,b,cを作成
    a = np.zeros((n, n))  # Matrix A
    b = np.zeros((n, n))  # Matrix B
    c = np.zeros((n, n))  # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0
    return a, b, c


def calc_matrix_product(a, b, c, n):  # a,bの行列積をcに入れる
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i, j] += a[i, k] * b[k, j]
    return c


def get_time(n):  # n*nの行列のとき, 行列積にかかる時間
    a, b, c = init_matrix(n)
    begin = time.time()
    calc_matrix_product(a, b, c, n)
    end = time.time()
    return end - begin


def save_graph(x_max, y_list):  # グラフをplotして保存
    x_list = list(range(x_max))
    plt.scatter(x_list, y_list)
    plt.xlabel("size of matrix")
    plt.ylabel("time[s]")
    plt.savefig("matrix_py.png")


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage: python %s N" % sys.argv[0])
        quit()

    n_max = int(sys.argv[1])
    times = [get_time(i) for i in range(n_max)]
    save_graph(n_max, times)
