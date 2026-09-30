# The total cost of a Coke is 50 cents
amount_due = 50

# Loop until the user has paid at least 50 cents
while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    # Prompt user to insert a coin
    coin = int(input("Insert Coin: "))

    # Only accept valid denominations
    if coin in [25, 10, 5]:
        amount_due -= coin

# Calculate change owed
change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")
