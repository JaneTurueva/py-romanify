from romanify import arabic2roman


def test_arabic2roman():
    assert arabic2roman(1) == 'I'
    assert arabic2roman(2) == 'II'
    assert arabic2roman(3) == 'III'
    assert arabic2roman(4) == 'IV'
    assert arabic2roman(9) == 'IX'
    assert arabic2roman(10) == 'X'
    assert arabic2roman(11) == 'XI'
    assert arabic2roman(40) == 'XL'
    assert arabic2roman(90) == 'XC'
    assert arabic2roman(110) == 'CX'
    assert arabic2roman(400) == 'CD'
    assert arabic2roman(900) == 'CM'
    assert arabic2roman(1000) == 'M'
