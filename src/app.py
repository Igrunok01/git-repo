from utils import safe_div, load_numbers

if __name__ == "__main__":
    a, b = load_numbers("data.txt")
    result = safe_div(a, b)
    print(f"{a} / {b} = {result}")
    print("dev3 patch 2")