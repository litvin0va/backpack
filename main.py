import pandas as pd
import os
import dynamic_alg
import greedy_alg
import genetic_alg
import linear_programming_alg
import time

file_time = open('time.txt', 'w')
file_info = open('info.txt', 'w')

method_to_run = 2

def get_ans(answer):
    ans = []
    for i in range(0, len(answer)):
        if answer[i] == 1:
            ans.append(i)
    return ans

def get_n_from_file(filepath):
    head = pd.read_csv(filepath, nrows = 1, header = None, skiprows = 1)
    x = str(head[0]).split(" ")
    for_read = x[5].split("\n")
    return int(for_read[0])

def get_capacity(fPath, offset):
    head = pd.read_csv(fPath, nrows = 1, header = None, skiprows = 2 + offset)
    x = str(head[0]).split(" ")
    f = x[5].split("\n")
    return int(f[0])

def get_final_price_ans(fPath, offset):
    head = pd.read_csv(fPath, nrows = 1, header = None, skiprows = 3 + offset)
    x = str(head[0]).split(" ")
    f = x[5].split("\n")
    return int(f[0])

def get_columns(fPath, offset, size):
    df = pd.read_csv(fPath, skiprows = 5 + offset, sep=',', header = None).head(size).drop(0, axis = 1)
    prices = [int(item) for item in df[1].to_list()]
    weights = [int(item) for item in df[2].to_list()]
    answer = [int(item) for item in df[3].to_list()]
    return prices, weights, answer

def get_final_price(prices, ans):
    sum_pr = 0
    for id in ans:
        sum_pr += prices[id]
    return sum_pr

def switch_method(max_сapacity, prices, weights, size):
    start = time.time()
    if method_to_run == 1:
        ans = greedy_alg.greedy_alg(prices, weights, max_сapacity, size)
    if method_to_run == 2:
        ans = dynamic_alg.run_algorithm(prices, weights, max_сapacity, size)
    if method_to_run == 3:
        ans = linear_programming_alg.run_algorithm(prices, weights, max_сapacity, size)
    if method_to_run == 4:
        genetic_alg.run_algorithm(prices, weights, max_сapacity, size, price_ans_true)
        return
    end = time.time()
    time_res = end - start
    file_info.write(str(size))
    file_info.write('\n')
    file_time.write(str(time_res))
    file_time.write('\n')
    #print("Time:", time_res)
    return ans


def run_calculation(offset, size, fPath):
    try:
        max_сapacity = get_capacity(fPath, offset)
        price_ans_true = get_final_price_ans(fPath, offset)
        prices, weights, answer = get_columns(fPath, offset, size)
    except:
        return False

    ans = switch_method(max_сapacity, prices, weights, size)

    if ans != price_ans_true:
        # print(ans, price_ans_true)
        print(":(((((((((((((((")
    #   else:
    #      print(":))))))))))))))")
    return True

def run_for_file(filepath):
    size = get_n_from_file(filepath)
    i = 0
    while 1:
        if run_calculation(i * (size + 7), size, filepath) == False:
            return
        i += 1
        print("Step:", i)


if __name__ == "__main__":
    dir = "/home/elizaveta/smallcoeff_pisinger/500"
    files = [os.path.join(dir, file) for file in os.listdir(dir) if file.endswith(".csv")]
    count = 0
    for file in files:
        file_info.write(file)
        file_info.write('\n')
        file_time.write('\n')
        print(file)
        run_for_file(file)
        count += 1
      #  if count == 2:
      #  break

file_time.close()
file_info.close()