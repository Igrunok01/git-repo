def safe_div(a, b):
    if b == 0:
        return float('inf')
    return a / b

def load_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    a, b = map(float, lines[:2])
    return a, b
