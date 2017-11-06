class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [[int(ch) for ch in line.split()] for line in matrix_string.splitlines()]
        self.columns = map(list, zip(*self.rows))
