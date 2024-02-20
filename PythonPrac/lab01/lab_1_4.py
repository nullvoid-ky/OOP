def func(num):
  print(1234 * num)
def main(number):
  check1 = number >= 0
  check2 = number < 10
  if check1 and check2:
    func(number)
  else:
    print("Error")
main(int(input()))