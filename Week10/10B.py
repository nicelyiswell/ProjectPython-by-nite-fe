n = int(input().strip())

food_counts = {}

for _ in range(n):
    food_item = input().strip()
    if food_item not in food_counts:
        food_counts[food_item] = 0
    food_counts[food_item] += 1

sorted_items = sorted(food_counts.items(), key=lambda x: (x[1], x[0]))


for item in sorted_items:
    print(item[0], item[1])
