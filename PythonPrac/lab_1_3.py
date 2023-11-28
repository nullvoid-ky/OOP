import math
def func(ent, ext):
    total = float(ext - ent)
    if total <= 15:
        return 0
    if total < 180:
        return math.ceil(total / 60) * 10
    if total < 360:
        return (math.ceil((total / 60) - 3) * 20) + 30
    return 200
def main():
    ent_hour, ent_min, ext_hour, ext_min = map(int, input().split())
    ent_time = ent_hour * 60 + ent_min
    ext_time = ext_hour * 60 + ext_min
    check1 = ent_time >= 420 and ent_time <= 1380
    check2 = ext_time >= 420 and ent_time <= 1380
    check3 = ext_time - ent_time >= 0
    if check1 and check2 and check3:
        print(func(ent_time, ext_time))
main()