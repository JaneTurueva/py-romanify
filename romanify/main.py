from collections import OrderedDict

mapping = OrderedDict()
mapping['M'] = 1000
mapping['D'] = 500
mapping['C'] = 100
mapping['L'] = 50
mapping['X'] = 10
mapping['V'] = 5
mapping['I'] = 1


def arabic2roman(number) -> str:
    result = ''
    for i,k in mapping.items():
        result += (i * (number // k))
        number %= k

    return result
