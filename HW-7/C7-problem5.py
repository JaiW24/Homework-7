def gcd(m, n):
    while m != 0:
        n, m = m, n % m

    return n


def phi(n):
    numbers = []

    for i in range(1, n):
        if gcd(i, n) == 1:
            numbers.append(i)

    return numbers


def main():
    n = int(input("Enter a number: "))

    answer = phi(n)

    print("Numbers relatively prime to", n)
    print(answer)

    print("Phi(", n, ") =", len(answer))


main()