def count_case(str):
    upper_count = sum(1 for char in str if char.isupper())
    lower_count = sum(1 for char in str if char.islower())
    return upper_count, lower_count

upper, lower = count_case(input())
print(lower, upper, sep = "\n")