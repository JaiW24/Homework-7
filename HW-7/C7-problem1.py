def simpleDiv(dividend, divisor):
    count = 0

    while dividend >= divisor:
        dividend = dividend - divisor
        count = count + 1

    return count


def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    answer = simpleDiv(dividend, divisor)

    print("Result:", answer)


main()