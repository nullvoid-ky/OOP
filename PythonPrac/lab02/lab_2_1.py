from itertools import permutations

num = list(map(int, input().split()))[:10]
number_sort = min((p for p in permutations(num, len(num)) if p[0] != 0))

result = "".join(map(str, number_sort))
print(result)