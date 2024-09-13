import numpy as np

def compute():
    matrix = np.random.rand(1000, 1000)
    result = np.dot(matrix, matrix)
    row_sums = np.sum(result, axis=1)
    return row_sums

if __name__ == '__main__':
    result = compute()
    print("Computation completed. Result sum:", np.sum(result))
