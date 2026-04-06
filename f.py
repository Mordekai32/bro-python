for num in range(2, 101):  # start from 2, because 1 is not prime
    is_prime = True        # assume num is prime
    for i in range(2, int(num**0.5) + 1):  # check divisors up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")