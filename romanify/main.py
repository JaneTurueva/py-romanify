import sys


MAPPING = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
)


def romanify(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError('Please provide positive integer')

    if number < 0:
        raise ValueError('Please provide positive integer')

    result = ''
    for char, value in MAPPING:
        result += (char * (number // value))
        number %= value

    return result


def main():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print('Please provide arabic number', file=sys.stderr)
        exit(1)

    arabic = int(sys.argv[1])
    print(romanify(arabic))
