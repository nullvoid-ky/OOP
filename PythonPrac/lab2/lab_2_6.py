def add2list(lst1, lst2):
  if len(lst1) != len(lst2):
    return -1
  sum = [num1 + num2 for num1,num2 in zip(lst1, lst2)]
  return sum