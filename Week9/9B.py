
list_price = [float(i) for i in input().split()]


list_qry = [int(i) for i in input().split()]


total = sum(price * qry for price, qry in zip(list_price, list_qry))

print((total))  

