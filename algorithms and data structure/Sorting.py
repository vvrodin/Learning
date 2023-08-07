def binary_search(list_, target):
    counter = 0
    while len(list_) > 0:
        if list_[len(list_) // 2] >= target:
            list_ = list_[: len(list_) // 2]
        elif list_[len(list_) // 2] < target:
            counter += len(list_) // 2 + 1
            list_ = list_[len(list_) // 2 + 1:]
    return counter


def insertionSort_orig(list_):
    for i in range(1, len(list_)):
        newElement = list_[i]
        location = i - 1
        while (location >= 0) and (newElement < list_[location]):
            list_[location + 1], list_[location] = list_[location], list_[location + 1]
            location -= 1
    return list_


def insertionSort_ver1(list_):
    for i in range(1, len(list_)):
        newElement = list_[i]
        location = i - 1
        if (location >= 0) and (newElement < list_[location]):
            del list_[i]
            list_.insert(binary_search(list_[:i], newElement), newElement)
    return list_


def BubbleSort_orig(list):
    flag = True
    while flag:
        flag = False
        for i in range(1, len(list)):
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
                flag = True
    return list


def BubbleSort_ver1(list):
    flag = True
    last_swap = len(list)
    while flag:
        flag = False
        for i in range(1, last_swap):
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
                last_swap = i
                flag = True
    return list


def BubbleSort_ver2(list):
    flag = True
    num = 0
    last_swap = len(list)
    while flag:
        flag = False
        num += 1
        if num % 2 == 1:
            for i in range(1, last_swap):
                if list[i] < list[i - 1]:
                    list[i], list[i - 1] = list[i - 1], list[i]
                    flag = True
        else:
            for i in range(last_swap - 1, 0, -1):
                if list[i - 1] > list[i]:
                    list[i], list[i - 1] = list[i - 1], list[i]
                    flag = True
    return list


def BubbleSort_ver3(list_):
    flag = True
    num = 0
    last_swap = len(list_)
    while flag:
        flag = False
        num += 1
        if num % 2 == 1:
            for i in range(1, last_swap):
                if list_[i] < list_[i - 1]:
                    list_[i], list_[i - 1] = list_[i - 1], list_[i]
                    last_swap = i
                    flag = True
        else:
            counter_rev = 0
            for i in range(last_swap - 1, 0, -1):
                if list_[i - 1] > list_[i]:
                    counter_rev += 1
                    if counter_rev == 1:
                        last_swap = i
                    list_[i], list_[i - 1] = list_[i - 1], list_[i]
                    flag = True
    return list_


def Shellsort_orig(list_):
    increment = len(list_) // 2
    while increment > 0:
        for i in range(increment):
            output = []
            for j in range(i, len(list_), increment):
                output.append(list_[j])
            output = insertionSort_orig(output)
            t = -1
            for j in range(i, len(list_), increment):
                t += 1
                list_[j] = output[t]
        increment //= 2
    return list_


def Shellsort_ver1(list_):
    increment = len(list_) // 2
    while increment > 0:
        for i in range(increment):
            output = []
            for j in range(i, len(list_), increment):
                output.append(list_[j])
            output = insertionSort_ver1(output)
            t = -1
            for j in range(i, len(list_), increment):
                t += 1
                list_[j] = output[t]
        increment //= 2
    return list_

def RadixSort(list_):
    t = 1
    mx_len = 1
    while t <= mx_len:
        bucket = [[] for _ in range(10)]
        for i in list_:
            if len(str(i)) > mx_len:
                mx_len = len(str(i))
            num = str(i)
            if len(num) < t:
                bucket[0].append(i)
            else:
                bucket[int(num[-t])].append(i)
        list_.clear()
        for i in bucket:
            list_.extend(i)
        t += 1
    return list_