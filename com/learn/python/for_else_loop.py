# a try statement’s else clause runs when no exception occurs,
# and a loop’s else clause runs when no break occurs.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion
# of the iterable (with for) or when the condition becomes false (with while),
# but not when the loop is terminated by a break statement.
