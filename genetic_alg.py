import random

sample_size = 10
genes_in_a_population = pow(sample_size, 2)
num_of_generations = 100

def calculate_price(gen, prices):
    F = 0
    for i in range(len(prices)):
        F += gen[i] * prices[i]
    return F


def fitness_func(gen, prices, weights, max_сapacity, size):
    W = 0
    for i in range(size):
        W += gen[i] * weights[i]
    if W > max_сapacity:
        return 0
    return calculate_price(gen, prices)


def calculate_target(gens, prices, weights, max_сapacity, size):
    target = []
    for gen in gens:
        target.append(fitness_func(gen, prices, weights, max_сapacity, size))
    return target

def sort_by_target(gens, target):
    to_sort = list(map(lambda x, y: (x,y), gens, target))
    to_sort.sort(reverse = True, key=lambda a: a[1])
    return list(map(lambda x: x[0], to_sort)), to_sort[0][1]

def sex_ver_3(gens):
    childrens = []
    size = len(gens[0])
    for i in range(len(gens)):
        for j in range(len(i + 1, gens)):
            chid = list(map(lambda x, y: int(x == 1 or y == 1), gens[i], gens[j]))
            childrens.append(chid)
    return childrens

def sex_ver_2(gens):
    childrens = []
    size = len(gens[0])
    for i in range(len(gens)):
        for j in range(len(gens)):
            chid = list(map(lambda x, y: x * (j % 2) + y * (j % 2 + 1), gens[i], gens[j]))
            childrens.append(chid)
    return childrens

def sex_ver_1 (gend):
    childrens = []
    size = len(gens[0])
    for i in range(len(gens)):
        for j in range(len(gens)):
            childrens.append(gens[i][0:int(size / 2)] + gens[j][int(size / 2):size])
    return childrens

def check_progress(best_candidat, prices, price_answer):
    diff = price_answer - calculate_price(best_candidat, prices)
    print("Diff:", diff)
    return diff

def get_random_generation(size):
    variants = [0, 1]
    return [[random.choice(variants)**4 for j in range(size)] for i in range(genes_in_a_population)]


def run_algorithm(prices, weights, max_сapacity, size, price_answer):
    #generation = [list(map(lambda j: int((i & pow(2, j)) > 0), range (size))) for i in range(genes_in_a_population)]
    generation = [list(map(lambda j: int(i * int (size / genes_in_a_population) == j), range (size))) for i in range(genes_in_a_population)]
    #generation = get_random_generation(size)

    prev = 0
    prev_prev = 0
    prev_prev_prev = 0
    for step in range(num_of_generations):
        target = calculate_target(generation, prices, weights, max_сapacity, size)

        generation, best_of_target = sort_by_target(generation, target)
        if best_of_target == 0:
            print ("Vymeranie! :(((")
            break
        best_sample = generation[0:sample_size]


        print("Step:", step)
        prev_prev_prev = prev_prev
        prev_prev = prev
        prev = check_progress(best_sample[0], prices, price_answer)
        if prev == prev_prev and prev == prev_prev_prev:
            print ("No pogress! :(((")
            break
        generation = sex_ver_3(best_sample)
        print(len(generation))

        break


