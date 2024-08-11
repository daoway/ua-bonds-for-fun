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
