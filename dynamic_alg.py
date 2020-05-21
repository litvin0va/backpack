def build_A(prices, weights, size, capacity):
    A = [[0] * (capacity + 1) for i in range(size + 1)]
    for i in range(1, size + 1):
        for k in range(1, capacity + 1):
            if k >= weights[i - 1]:
                A[i][k] = max(A[i - 1][k], A[i - 1][k - weights[i - 1]] + prices[i - 1])
            else:
                A[i][k] = A[i - 1][k]
    return A

def findAns(A, weights, size, max_сapacity, prices):
    k = max_сapacity
    ans = 0
    for i in range(size, 0, -1):
        if A[i][k] != A[i - 1][k]:
            ans += prices[i - 1]
            k -= weights[i - 1]
    return ans


def run_algorithm(prices, weights, max_сapacity, size):
    A = build_A(prices, weights, size, max_сapacity)
    ans = findAns(A, weights, size, max_сapacity, prices)
    return ans

