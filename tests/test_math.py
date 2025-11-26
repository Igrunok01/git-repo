def safe_div(a, b):
    if b == 0:
        return float("inf")
    return a / b


def test_safe_div_normal():
    assert safe_div(10, 2) == 5


def test_safe_div_by_zero():
    result = safe_div(10, 0)
    assert result == float("inf")

def test_safe_div_negative():
    assert safe_div(-10, 2) == -5
