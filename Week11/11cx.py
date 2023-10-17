import math

def mean(data):
    return sum(data) / len(data)

def standard_deviation(data):
    avg = mean(data)
    variance = sum([((x - avg) ** 2) for x in data]) / len(data)
    return math.sqrt(variance)

def remove_outliers(data):
    avg = mean(data)
    sd = standard_deviation(data)
    return [x for x in data if (avg - sd) <= x <= (avg + sd)]

def main():
    n = int(input())

    data = [float(input()) for _ in range(n)]

    revised_data = remove_outliers(data)
    revised_avg = mean(revised_data)

    print(round(revised_avg, 2))

if __name__ == "__main__":
    main()
