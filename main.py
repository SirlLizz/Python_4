# минимальное число выздоровевших среди всех стран

import pandas as pd
from multiprocessing import Pool
import time
from matplotlib import pyplot as plt

def min(*args):
    min = 0
    for i in range(len(args)):
        if(args[i] < min):
            min=args[i]
    return min


def multiproc(num_of_proc):
    if __name__ == '__main__':
        start_time = time.time()
        with Pool(num_of_proc) as p:
            df = global_df.copy()
            print(p.apply(min, df['Вылечились'].tolist()[0:217]))
        end_time = time.time()
        return end_time - start_time

if __name__ == '__main__':
    global_df = pd.read_csv("data.csv", sep=',', encoding="cp1251")
    # print(global_df.info)
    a = []
    for i in range(1, 24):
        a.append(multiproc(i))
    plt.plot(a)
    plt.show()