def is_plusone_dictionary(d):
  check = True
  last_v = 0
  for k, v in d.items() :
    if k == (v - 1) and last_v + 1 is k:
      check = True
      last_v = v
    else :
      check = False
      break
  return check