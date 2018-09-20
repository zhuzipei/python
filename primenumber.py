def odd_gen():
    n = 1
    while True:
        n += 2
    yield n
def is_prime(n):
    g = odd_gen()
    while b <= n/2:
        b = next(g)
        if n%b == 0:
            return False
    return True
def primes():
    yield 2
    while True:
        lst = filter(is_prime(n),odd_gen())


def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def _not_divisible(n):
#     return lambda x: x % n > 0

# def prime():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
