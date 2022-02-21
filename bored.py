# 오늘은 GST를 계산해 볼 거에요~
GST = 0.15
item = float(input("Enter item price: "))
item_GST = item * GST
total_cost = item + item_GST
print(f"Total cost ${total_cost}")
