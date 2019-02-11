from collections import OrderedDict

import sys

mapping = OrderedDict()
mapping['M'] = 1000
mapping['CM'] = 900
mapping['D'] = 500
mapping['CD'] = 400
mapping['C'] = 100
mapping['XC'] = 90
mapping['L'] = 50
mapping['XL'] = 40
mapping['X'] = 10
mapping['IX'] = 9
mapping['V'] = 5
mapping['IV'] = 4
mapping['I'] = 1


def arabic2roman(number) -> str:
    result = ''
    for i,k in mapping.items():
        result += (i * (number // k))
        number %= k

    return result

def main():
    if len(sys.argv) < 2:
        print('Please provide arabic number', file=sys.stderr)
        exit(1)

    arabic = int(sys.argv[1])
    print(arabic2roman(arabic))
