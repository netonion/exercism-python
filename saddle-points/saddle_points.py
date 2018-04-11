def saddle_points(matrix):
    if len({len(row) for row in matrix}) > 1:
        raise ValueError("Matrix is irregular.")

    row_max = [max(row) for row in matrix]
    col_min = [min(col) for col in zip(*matrix)]

    return {(i, j) for i, row in enumerate(matrix) for j, _ in enumerate(row) if row_max[i] == col_min[j]}
