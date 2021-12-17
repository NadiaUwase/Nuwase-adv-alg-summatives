# this will calculate the sum of the digits individually
def sum_of_digits(n):
    s = 0
    # checking if it is not already a digit, to divide the number into digits, it is dividing it by 10 and deriving it
    # from the remainder and the quotient which are then returned
    while n > 9:
        s += n % 10
        n //= 10
    s += n
    return s

# the sum above is then passed to the check super_digit function which checks to see if the sum has already added up to
# a digit
def check_super_digit(n):
    d = sum_of_digits(n)
    if d < 10:
        return d
    return check_super_digit(d)

# if it still is a number and not a digit, this function below then passes it to the first function to calculate the sum
def super_digit_iter(n):
    d = sum_of_digits(n)
    while d > 9:
        d = sum_of_digits(d)
    return d


def main():
    n = int(input("please enter the number for which you want to know the super digit: ").strip())
    k = int(input("what is the number of iterations of the number: ").strip())
    print("the super digit of", n,"repeated", k, "times is: ", super_digit_iter(sum_of_digits(n) * k))


if __name__ == "__main__":
    main()
