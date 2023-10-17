def least_initial_balance(transactions):
    runing_balance = 0 
    min_balance = 0
    for transaction in transactions :
        runing_balance += transaction

        if runing_balance<min_balance:
            min_balance = runing_balance
    return abs(min_balance)
def main ():
    transactions = []
    while True:
        line = input().strip()
        if line =="$":
            break
        transactions.append(int(line))

    print(least_initial_balance(transactions))
if __name__ == "__main__":
    main()
