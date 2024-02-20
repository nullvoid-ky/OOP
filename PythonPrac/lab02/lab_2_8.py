day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0): 
        return True
    else: return False

def day_of_year(day, month, year):
    if day < 1 or day > 31:
      return -1
    day_in_month_local = day_in_month.copy()
    if day > day_in_month_local[month-1]:
      return -1
    if is_leap(year):
        day_in_month_local[1] = 29
    for i in range(0, month - 1): day += day_in_month_local[i]
    return day

def day_in_year(year):
    if is_leap(year): return 366
    else : return 365

def date_diff(date_1, date_2):
    date_1 = list(map(int, date_1.split("-"))) 
    date_2 = list(map(int, date_2.split("-")))
    date_first = day_of_year(date_1[0], date_1[1], date_1[2])
    date_second = day_of_year(date_2[0], date_2[1], date_2[2])
    if date_first == -1 or date_second == -1: return -1

    date = 0
    date += date_second - date_first + \
        sum([day_in_year(y) for y in range(date_1[2], date_2[2])]) + 1
    return date