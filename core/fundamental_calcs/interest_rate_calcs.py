
def future_value_basic_interest(principal_amount:float,rate_of_interest:float) -> float:
    """
        principal_amount: Amount borrowed
        rate_of_interest: Annual rate of interest

        returns: total amount due post interest at first year
    """
    return round((1.00000+(rate_of_interest*0.010000))*principal_amount,16)


def future_value_compound_interest(principal_amount:float,rate_of_interest:float,duration:int) -> float:
    """
        principal_amount: Amount borrowed
        rate_of_interest: Annual rate of interest
        duration: time until maturity (years)

        returns: total amount due post compound interest
    """
    return round(((1.00000+(0.01*rate_of_interest))**duration)*principal_amount,6)

def future_value_periodic_compound_interest(principal_amount:float,rate_of_interest:float,duration:int,frequency:int) -> float:
    """
        principal_amount: Amount borrowed
        rate_of_interest: Annual rate of interest
        duration: time until maturity (years)
        frequency: interest periodicity (number of times in an year)

        returns: total amount due post interest from first year
    """
    return round(((1.00000+(0.01*rate_of_interest/frequency))**(duration*frequency))*principal_amount,6)


def gross_return(principal_amount:float,future_value:float):
    return round(future_value/principal_amount,6)

def net_return(principal_amount:float,future_value:float):
    
    return round((future_value-principal_amount)/principal_amount,6)*100

def equivalent_rate(current_rate:float,current_periodicity:int,prospect_periodicity:int):
    current_rate = current_rate*0.01
    eq_rate = (((1.0000+(current_rate/current_periodicity))**(current_periodicity/prospect_periodicity)) - 1.00000)*prospect_periodicity
    return eq_rate*100.00

def present_value(rate:float,duration:int,future_amount:float,periodicity:int=1):
    rate=0.01*rate
    return round(future_amount/((1+(rate/periodicity))**(periodicity*duration)),6)

