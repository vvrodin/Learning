def permutations(list_):
    n = len(list_)
    list_ = [str(i) for i in list_]
    numbers = list_.copy()
    while len(numbers[0]) < n:
        t = sorted(numbers * n)
        numbers = [''.join(z) for z in list(zip(t, list_ * len(t)))]
        numbers = [i for i in numbers if len(set(i)) == len(i)]
    return numbers


def combination(list_, k):
    n = len(list_)
    if k > n:
        return 0
    list_ = [str(i) for i in list_]
    numbers = [i for i in list_]
    output = []
    while len(numbers[0]) < k:
        t = sorted(numbers * n)
        numbers = [''.join(z) for z in list(zip(t, list_ * len(t)))]
        numbers = [i for i in numbers if len(set(i)) == len(i)]
    numbers = [set(i) for i in numbers]
    for i in numbers:
        if i not in output:
            output.append(i)
    output = [''.join(list(i)) for i in output]
    return output


def combinations_with_repetitions(list_, k):
    n = len(list_)
    if k > n:
        return 0
    list_ = [str(i) for i in list_]
    numbers = [i for i in list_]
    while len(numbers[0]) < k:
        t = sorted(numbers * n)
        numbers = [''.join(z) for z in list(zip(t, list_ * len(t)))]
    numbers = [''.join(sorted(list(i))) for i in set(numbers)]
    numbers = list(set(numbers))
    return numbers