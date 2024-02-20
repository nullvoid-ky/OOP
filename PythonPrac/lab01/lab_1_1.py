for i in range(2000, 3200):
  check1 = i % 7
  check2 = i % 5
  if not check1 and check2:
    print(i, end=",")