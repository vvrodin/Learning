class string_search:

    def direct_search(self, string, sub):
        for i in range(len(string)):
            if string[i] == sub[0]:
                flag = True
                for j in range(len(sub)):
                    if string[i + j] != sub[j]:
                        flag = False
                        break
                if flag:
                    return i
        return -1

    def __prefix_function(self, string):
        arr = [0 for _ in range(len(string))]
        j, i = 0, 1
        while i < len(string):
            if string[i] == string[j]:
                arr[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = arr[j - 1]
        return arr

    def Knuth_Morris_Pratt_algorithm(self, string, sub):
        pi = self.__prefix_function(sub)
        i, j = 0, 1
        while i < len(string) and j < len(sub):
            if string[i] == sub[j]:
                if j >= len(sub) - 1:
                    return i - j
                else:
                    i += 1
                    j += 1
            else:
                if i >= len(string) - 1:
                    return -1
                elif j == 0:
                    i += 1
                else:
                    j = pi[j - 1]
        return None

    def Boyer_Moore_Horspool_algorithm(self, string, sub):
        n = len(sub) - 1
        chars_table = {i: n - sub[:-1].rindex(i) for i in set(sub[:-1])}
        chars_table['*'] = len(sub)
        if sub[:-1] not in chars_table.keys():
            chars_table[sub[-1]] = len(sub)
        i, j = n, n
        while i < len(string) and j > 0:
            if i == len(string):
                return -1
            if string[i] == sub[j]:
                i -= 1
                j -= 1
            else:
                if j == n:
                    i += chars_table.get(string[i], chars_table['*'])
                else:
                    i += n - j
                    i += chars_table.get(sub[j])
                    j = n
        return i
