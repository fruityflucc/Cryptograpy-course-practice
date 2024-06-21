def fastexponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result


def main():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    modulus = int(input("Enter the modulus: "))
    result = fastexponentiation(base, exponent, modulus)
    print(f"{base}^{exponent} mod {modulus} =", result)


if __name__ == "__main__":
    main()