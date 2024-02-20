def is_palindrome(num):
    return str(num) == str(num)[::-1]

largest_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome)