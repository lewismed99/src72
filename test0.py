from prime import is_prime



def test_prime(n,expected):
    if is_prime(n)!=expected:
        print(f"error on is_prime({n}),expected {expected}")