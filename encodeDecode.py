    def encode(self, strs):
        res = ''
        for word in strs:
            res += len(word) + '#' + word
        return res

    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(str[i:j])
            i = j
        return res
            