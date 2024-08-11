class BondSpec:
    """
    Represents the specifications of a bond.
    """

    def __init__(self, coupon_rate, nominal_yield_rate, duration_years):
        self.coupon_rate = coupon_rate
        self.nominal_yield_rate = nominal_yield_rate
        self.duration_years = duration_years

    def __repr__(self):
        return (f"BondSpec(coupon_rate={self.coupon_rate}, "
                f"nominal_yield_rate={self.nominal_yield_rate}, "
                f"duration_years={self.duration_years})")


class BondSpecBuilder:
    """
    A builder class for creating BondSpec objects.
    """

    def __init__(self):
        # Default values can be set here if desired
        self._coupon_rate = None
        self._nominal_yield_rate = None
        self._duration_years = None

    def set_coupon_rate(self, coupon_rate):
        self._coupon_rate = coupon_rate
        return self

    def set_nominal_yield_rate(self, nominal_yield_rate):
        self._nominal_yield_rate = nominal_yield_rate
        return self

    def set_duration_years(self, duration_years):
        self._duration_years = duration_years
        return self

    def build(self):
        if self._coupon_rate is None or self._nominal_yield_rate is None or self._duration_years is None:
            raise ValueError("All bond specification fields must be set before building")
        return BondSpec(self._coupon_rate, self._nominal_yield_rate, self._duration_years)


def calculate_bond_yield(investment_usd, start_exchange_rate, end_exchange_rate, bond_spec):
    """
    Calculate the total return and profit from investing in a bond with varying exchange rates.

    Parameters:
    investment_usd (float): The amount of investment in USD.
    start_exchange_rate (float): The exchange rate from USD to UAH at the start.
    end_exchange_rate (float): The exchange rate from USD to UAH at the end.
    bond_spec (BondSpec): The specifications of the bond.

    Returns:
    tuple: Total return and profit in USD.
    """
    # Convert investment to UAH at the start exchange rate
    investment_uah = investment_usd * start_exchange_rate

    # Calculate annual coupon payment
    annual_coupon_payment = investment_uah * bond_spec.coupon_rate / 100

    # Total coupon payments over the bond's duration
    total_coupon_payments = annual_coupon_payment * bond_spec.duration_years

    # Calculate total nominal yield over the bond's duration
    total_nominal_yield = investment_uah * bond_spec.nominal_yield_rate / 100 * bond_spec.duration_years

    # Total return in UAH
    total_return_uah = investment_uah + total_coupon_payments + total_nominal_yield

    # Convert total return back to USD using the end exchange rate
    total_return_usd = total_return_uah / end_exchange_rate

    # Calculate profit in USD
    profit_usd = total_return_usd - investment_usd

    return total_return_usd, profit_usd
