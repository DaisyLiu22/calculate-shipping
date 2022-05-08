def calculate_shipping(quantity):
    """Calculate the total weight of the package,
    and returns the shipping fee"""
    quantity = int(quantity)
    weight = 0.8
    total_weight = float(quantity * weight)
    count = 0
    if total_weight < 15:
        if total_weight < 3:
            total_cost = 3000
        elif total_weight >= 3 and total_weight < 5:
            total_cost = 4000
        elif total_weight >= 5 and total_weight < 7:
            total_cost = 5000
        elif total_weight >= 7 and total_weight < 10:
            total_cost = 6000
        else:
            total_cost = 7000
    else:
        count = int(total_weight / 15)
        extra_weight = total_weight - count*15
        if extra_weight < 3:
            extra_cost = 3000
        elif extra_weight >= 3 and extra_weight < 5:
            extra_cost = 4000
        elif extra_weight >= 5 and extra_weight < 7:
            extra_cost = 5000
        elif extra_weight >= 7 and extra_weight < 10:
            extra_cost = 6000
        else:
            extra_cost = count*7000
        total_cost = float(count*7000 + extra_cost)
    
    return total_cost

def total_amount(quantity):
    quantity = int(quantity)
    price = 23000
    total_deposit = calculate_shipping(quantity) + quantity * price
    return total_deposit
        
def main():
    """
    You can test all the functions here
    """
    # calculate_shipping(20)


if __name__ == '__main__':
    main()