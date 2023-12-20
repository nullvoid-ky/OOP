def delete_minus(x):
  result = [[num for num in sublist if num >= 0] for sublist in x]
  return result