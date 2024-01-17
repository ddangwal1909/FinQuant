from typing import List


def cashflow_present_value(maturity_amounts:List[float],rate_of_interests:List[float]):

    interests = [0.01*r for r in rate_of_interests]
    discount_factors = [(1/(1+interests[r]))**(r+1) for r in range(len(interests))]
    present_value = [r*am for r,am in zip(discount_factors,maturity_amounts)]
    return present_value,round(sum(present_value),6)


def bond_cashflow_present_value(bond_value:float, maturity_years:int, coupon_interest_rate:float,yield_to_maturity:float,periodicity:int=1):
    """
    returns the dirty_price of a bond, That is it doesn't account for accrued intrests from initial coupon payments
    """
    
    print(f"Bond Value: ${bond_value}")
    present_value = 0.00000
    total_cycles = maturity_years*periodicity
    coupon_payment = (bond_value*(0.01*coupon_interest_rate))/periodicity
    for cyc in range(1,total_cycles):
        pv_curr = coupon_payment/(((1+((0.01*yield_to_maturity)/periodicity)))**cyc)
        print(f"Cycle {cyc} -> Coupon payment (FV) of ${coupon_payment} with PV : ${pv_curr}")
        present_value+=pv_curr
    ### maturity year
    pv_maturity = (bond_value+coupon_payment)/(((1+((0.01*yield_to_maturity)/periodicity)))**total_cycles)
    present_value+=pv_maturity
    print(f"Maturity Cycle {total_cycles} -> total PAR + Coupon payment (FV) of ${bond_value+coupon_payment} with PV : ${pv_maturity}")
    print(f"Bond of Future Value: ${bond_value} has a present value priced at : ${present_value}")
    return present_value



