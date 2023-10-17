import math
def day_to_week(days):
    return math.ceil(days/7)

days = int(input())
print(day_to_week(days))
