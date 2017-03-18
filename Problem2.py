# Find the sum of all even numbers in the Fibonacci sequence under 4 million

def fibSum(limit):
    current = 1
    next = 2
    temp = 0
    sum = 0
    while current < limit:
        if current % 2 == 0:
            sum += current
        temp = next + current
        current = next
        next = temp
    return sum

if __name__ == "__main__":
    print(fibSum(4000000))
