
def calc_sum(n):
    total = 0
    i = 0
    while i <= n:
        total = total + i
        i = i+1
    return total


# testing the function for n= 10
print("the sum of the first elements is", calc_sum(10))
# n= 10000
print("the sum of the first elements is", calc_sum(10000))

# n= 1000000
print("the sum of the first elements is", calc_sum(1000000))

# n= 1000000000
print("the sum of the first elements is", calc_sum(1000000000))

