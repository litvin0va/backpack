def greedy_alg (prices, weights, max_сapacity, size):
    A = list(map(lambda x, y, t, z: (x/y, t, z), prices, weights, prices, weights))
    A.sort(reverse=True, key=lambda elem: elem[0])
    ans = 0
    weight_sum = 0
    for i in range(size):
        if weight_sum + A[i][2] < max_сapacity:
            weight_sum += A[i][2]
            ans += A[i][1]
    return ans