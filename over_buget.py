def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    sum_four_parameters = food_bill + electricity_bill + internet_bill + rent
    if sum_four_parameters > budget:
        return True
    return False


