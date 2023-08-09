class Numerical:
    def evaluate(self, a, x):
        result = a[0] + a[1] * x
        for i in range(2, len(a)):
            result += a[i] * (x ** i)
        return result

    def horner_method(self, a, x):
        result = 1
        for i in range(len(a) - 1, -1, -1):
            result *= x
            result += a[i]
        return result