from romanify import romanify


def test_arabic2roman():
    assert romanify(1) == 'I'
    assert romanify(2) == 'II'
    assert romanify(3) == 'III'
    assert romanify(4) == 'IV'
    assert romanify(9) == 'IX'
    assert romanify(10) == 'X'
    assert romanify(11) == 'XI'
    assert romanify(40) == 'XL'
    assert romanify(90) == 'XC'
    assert romanify(110) == 'CX'
    assert romanify(400) == 'CD'
    assert romanify(900) == 'CM'
    assert romanify(1000) == 'M'
