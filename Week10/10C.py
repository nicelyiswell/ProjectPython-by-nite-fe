class Matrix:
    def __init__(self, m, n):
        self.rowCount = m
        self.colCount = n
        self.matrix = [[0 for j in range(n)] for i in range(m)]

    def set(self, i, j, x):
        if 0 <= i < self.rowCount and 0 <= j < self.colCount:
            self.matrix[i][j] = x
        else:
            raise ValueError("Row or column index out of bounds")

    def get(self, i, j):
        if 0 <= i < self.rowCount and 0 <= j < self.colCount:
            return self.matrix[i][j]
        else:
            raise ValueError("Row or column index out of bounds")

    def transpose(self):
        m, n = self.colCount, self.rowCount
        transposed = Matrix(m, n)
        for i in range(m):
            for j in range(n):
                transposed.set(i, j, self.get(j, i))
        return transposed

    def __add__(self, q):
        if self.rowCount != q.rowCount or self.colCount != q.colCount:
            return None
        result = Matrix(self.rowCount, self.colCount)
        for i in range(self.rowCount):
            for j in range(self.colCount):
                sum_value = self.get(i, j) + q.get(i, j)
                result.set(i, j, sum_value)
        return result

    def __mul__(self, q):
        if self.colCount != q.rowCount:
            return None
        result = Matrix(self.rowCount, q.colCount)
        for i in range(self.rowCount):
            for j in range(q.colCount):
                sum_value = 0
                for k in range(self.colCount):
                    sum_value += self.get(i, k) * q.get(k, j)
                result.set(i, j, sum_value)
        return result

def read_matrix(m,n):
    mat = Matrix(m,n)
    for i in range(0,m):
        row = input().split()
        for j in range(0,n):
            mat.set(i,j,int(row[j]))
    return mat

def print_matrix(mat):
    for i in range(0,mat.rowCount):
        for j in range(0,mat.colCount):
            print(mat.get(i,j),end='')
            if j!=mat.colCount-1:
                print(' ',end='')
        print()

mat1 = read_matrix(int(input()),int(input()))
mat2 = read_matrix(int(input()),int(input()))
mat3 = mat1.transpose()*(mat1+mat2)
print_matrix(mat3)
