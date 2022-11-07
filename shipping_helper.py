def calculate_shipping(quantity):
    """Calculate the total weight of the package,
    and returns the shipping fee"""
    quantity = int(quantity)
    count = 0
    if quantity <= 4:
        if quantity <= 2:
            total_cost = 4000
        else:
            total_cost = 6000
    else:
        count = int(quantity / 4)
        extra_sets = quantity - count*4
        if extra_sets <= 2:
            extra_cost = 4000
        else:
            extra_cost = 6000
        total_cost = float(count*6000 + extra_cost)
    
    return total_cost

def total_amount(quantity):
    quantity = int(quantity)
    price = 54000
    total_deposit = calculate_shipping(quantity) + quantity * price
    return total_deposit
        
def main():
    """
    You can test all the functions here
    """
    # calculate_shipping(20)


if __name__ == '__main__':
    main()