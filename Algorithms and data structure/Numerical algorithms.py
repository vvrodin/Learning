class Numerical:
    def determinant_row_expansion(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        output = 0
        for i in range(n):
            new_matrix = [matrix[j][:i] + matrix[j][i + 1:] for j in range(1, n)]
            output += ((-1) ** (i % 2)) * matrix[0][i] * self.determinant_row_expansion(new_matrix)
        return output

    def evaluate(self, coefs, x):
        result = 0
        power_x = 1
        for i in range(len(coefs)):
            result += coefs[i] * power_x
            power_x *= x
        return result

    def horner_method(self, coefs, x):
        result = coefs[-1]
        for i in range(len(coefs) - 2, -1, -1):
            result *= x
            result += coefs[i]
        return result

    def matrix_multiplication(self, matrix_A, matrix_B):
        a_r, a_c = len(matrix_A), len(matrix_A[0])
        b_r, b_c = len(matrix_B), len(matrix_B[0])
        matrix = [[0 for _ in range(a_r)] for _ in range(b_c)]
        for i in range(a_r):
            for j in range(b_c):
                for k in range(a_c):
                    matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]
        return matrix

    def matrix_multiplication_vinograd(self, matrix_A, matrix_B):
        row_factor_A, column_factor_B = [], []
        a_r, a_c = len(matrix_A), len(matrix_A[0])
        b_r, b_c = len(matrix_B), len(matrix_B[0])
        flag = False
        if a_c % 2 == 1:
            a_c -= 1
            flag = True
        for i in range(a_r):
            factor = matrix_A[i][0] * matrix_A[i][1]
            for j in range(2, a_c - 1, 2):
                factor += matrix_A[i][j] * matrix_A[i][j + 1]
            row_factor_A.append(factor)
        for i in range(b_c):
            factor = matrix_B[0][i] * matrix_B[1][i]
            for j in range(2, b_r - 1, 2):
                factor += matrix_B[j][i] * matrix_B[j + 1][i]
            column_factor_B.append(factor)
        matrix = [[0 for _ in range(a_r)] for _ in range(b_c)]
        for i in range(a_r):
            for j in range(b_c):
                matrix[i][j] = -row_factor_A[i] - column_factor_B[j]
                for k in range(0, a_c - 1, 2):
                    matrix[i][j] += (matrix_A[i][k] + matrix_B[k + 1][j]) * (matrix_A[i][k + 1] + matrix_B[k][j])
        if flag:
            for i in range(a_r):
                for j in range(b_c):
                    matrix[i][j] += matrix_A[i][a_c] * matrix_B[a_c][j]
        return matrix

    def matrix_multiplication_strassen(self, matrix_A, matrix_B): # НЕРАБОТАЕТ
        x1 = (matrix_A[0][0] + matrix_A[1][1]) * (matrix_B[0][0] + matrix_B[1][1])
        x2 = (matrix_A[1][0] + matrix_A[1][1]) * matrix_B[0][0]
        x3 = matrix_A[0][0] * (matrix_B[0][1] - matrix_B[1][1])
        x4 = matrix_A[1][1] * (matrix_B[1][0] - matrix_B[0][0])
        x5 = (matrix_A[0][0] + matrix_A[1][1]) * matrix_B[1][1]
        x6 = (matrix_A[1][0] - matrix_A[0][0]) * (matrix_B[0][0] + matrix_B[0][1])
        x7 = (matrix_A[1][0] - matrix_A[1][1]) * (matrix_B[1][0] + matrix_B[1][1])
        matrix = [[0, 0], [0, 0]]
        matrix[0][0] = x1 + x4 - x5 + x7
        matrix[1][0] = x2 + x4
        matrix[0][1] = x3 + x5
        matrix[1][1] = x1 + x3 - x2 + x6
        return matrix

    def gaussian_elimination(self, matrix, vector, accuracy=1):
        matrix = sorted(matrix)
        for i in range(len(matrix)):
            matrix[i].append(vector[i])
        i = 0
        while i < len(matrix):
            try:
                matrix[i] = list(map(lambda x: round(x / matrix[i][i], accuracy), matrix[i]))
            except ZeroDivisionError:
                return 'System has at least one free variable'
            for j in range(len(matrix)):
                if i == j:
                    continue
                t = matrix[j][i]
                for s in range(i, len(matrix[j])):
                    matrix[j][s] -= matrix[i][s] * t
                    matrix[j][s] = round(matrix[j][s], accuracy)
            i += 1
        answer = [i[-1] for i in matrix]
        return answer

    def fast_matrix_exponentiation(self, matrix, n):
        if n == 1:
            return matrix
        if n % 2 == 1:
            y = self.fast_matrix_exponentiation(matrix, n - 1)
            return self.matrix_multiplication(y, matrix)
        elif n % 2 == 0:
            y = self.fast_matrix_exponentiation(matrix, n // 2)
            return self.matrix_multiplication(y, y)
