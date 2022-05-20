import math
import random
import multiprocessing as mp
import time


def f(x):
    return 1/(math.sqrt(x+3) + math.sqrt((x+3)*(x+3))) #приблизительное значение на отрезке от -2 до 1: 0.8109302162163288

def monte_carlo(n):
    right = 1
    left = -2
    square = 100 * (right - left)
    x = []
    y = []
    for i in range(n):
        x.append(random.uniform(left, right))
        y.append(random.uniform(0, 100))
    count = 0 #точки попавшие в промежуток под графиком
    for i in range(n):# вычисляем их
        if y[i] <= f(x[i]):
            count += 1
    return square*(count/n)

def main(pool):
    n = 1000
    a = []
    start_p = time.time()
    a = pool.map(monte_carlo, [n]*n)
    end_p = time.time()
    print('примерное значение интеграла', sum(a) / n, 'потребовалось времени c мультипроцессингом', end_p - start_p)
    a = []
    start = time.time()
    for i in range(n):
        a.append(monte_carlo(n))
    end = time.time()
    print('примерное значение интеграла', sum(a)/n, 'потребовалось времени без мультипроцессинга', end - start)

if __name__ == "__main__":
    pool = mp.Pool(processes=4)
    main(pool)
