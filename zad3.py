def cesar_cypher(data, move,
                 alphabet=list(
                     {"a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z'})):
    data = list(str.lower(data))
    ret = ""
    alphabet.sort()
    for letter in data:
        if letter in alphabet:
            i = list(alphabet).index(letter)
            if i + move < len(alphabet) - 1:
                letter = list(alphabet)[i + move]
                ret += letter

            else:
                letter = list(alphabet)[i + move - len(alphabet)]
                # print(letter)
                ret += letter
        else:
            ret += letter
    return ret




