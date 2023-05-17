#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        shallow = []
        for i in matrix:
            shallow.append(list(map(lambda x: x**2, i)))
        return (shallow)
    return None
