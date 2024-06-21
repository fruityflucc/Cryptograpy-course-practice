irreducible_polynomial = 0b10011
order_of_field = 2 ** 4


def gf_add(a, b):
    return a ^ b


def gf_multiply(a, b):
    result = 0
    for _ in range(order_of_field):
        if b & 1:
            result ^= a
        a <<= 1
        if a & (1 << 4):
            a ^= irreducible_polynomial
        b >>= 1
    return result


def gf_inverse(a):
    t = 0
    newt = 1
    r = 0x11B
    newr = a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t ^ (quotient * newt)
        r, newr = newr, r ^ (quotient * newr)
    if r > 1:
        raise ValueError("Element is not invertible")
    if t < 0:
        t += order_of_field
    return t


def main():
    a = int(input("Enter the first element: "), 2)
    b = int(input("Enter the second element: "), 2)
    print("Addition:", bin(gf_add(a, b)))
    print("Multiplication:", bin(gf_multiply(a, b)))
    try:
        inverse_a = gf_inverse(a)
        inverse_b = gf_inverse(b)
        print("Inverse of", bin(a), "is", bin(inverse_a))
        print("Inverse of", bin(b), "is", bin(inverse_b))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()