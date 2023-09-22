    def encode(self, strs):
        result = ''
        for word in strs:
            result += len(word) + '#' + word
        return result

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
            