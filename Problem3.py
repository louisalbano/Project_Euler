# What is the largest prime factor of the number 600851475143 ?

# Brute force solution I came up with
# It's really slow, so not really much of a solution in this case
def primeFactor(num):
    result = 0
    for x in range(1, num):
        isPrime = True
        if num % x == 0:  # Find the factors of num
            for y in range(2, x):  # Check if those factors are prime
                if x % y == 0:
                    isPrime = False
                    break
            if isPrime:
                result = x
    return result

# Trying to utilize the Fundamental Theorem of Arithmetic for a faster solution
# Lots of comments below. Mostly for my understanding of
def betterPrimeFactor(num):
    counter = 2
    temp = num
    while counter ** 2 <= temp:  # Only check numbers up to sqrt(num)
        if temp % counter == 0:  # Is it a factor?
            temp /= counter
            result = counter
        else:
            counter = 3 if counter == 2 else counter + 2  # Only check odd numbers since evens aren't prime
    if temp > result:  # The remainder is a prime number
        result = temp
    return result


if __name__ == "__main__":
    print(primeFactor(13195))
    print(betterPrimeFactor(600851475143))
