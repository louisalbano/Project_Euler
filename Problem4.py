# Find the largest palindrome made from the product of two 3-digit numbers

def largestPalindrome(num):
    result = 0
    for x in range(1, num):
        for y in range(x, num):
            product = x * y
            strProduct = str(product)
            if strProduct == strProduct[::-1] and product > result:
                result = product
    return result


if __name__ == "__main__":
    print(largestPalindrome(1000))