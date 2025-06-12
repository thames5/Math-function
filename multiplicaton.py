def multiply_matrices(A, B):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
    print("Matrix A:")
    for row in A:
        print(row)
    print("Matrix B:")
    for row in B:
        print(row)
    print("Result of Matrix Multiplication:")
    for row in result:
        print(row)

A = [[2, 3], [4, 5]]
B = [[3, 1], [2, 3]]

multiply_matrices(A, B)

