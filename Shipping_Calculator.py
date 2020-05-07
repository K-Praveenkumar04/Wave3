#Shipping_Calculator
items = int(input("Enter the number of items: "))
def total_cost(items):
    if items == 1:
        return 10.95
    elif items > 1:
        items = items -1
        return items * 2.95 + 10.95
print ("The total cost for shipping is: $" + str(total_cost(items)))