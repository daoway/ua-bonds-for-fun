import unittest
from bond_calc import calculate_bond_yield, BondYieldResult
from bond import BondSpec


class TestCalculateBondYield(unittest.TestCase):

    def setUp(self):
        """Set up test cases with default values."""
        self.investment_usd = 1000
        self.start_exchange_rate = 37
        self.end_exchange_rate = 37
        self.bond_spec = BondSpec(coupon_rate=9.85, nominal_yield_rate=19.70, duration_years=2.5)

    def test_bond_yield_with_same_exchange_rate(self):
        """Test when the start and end exchange rates are the same."""
        result = calculate_bond_yield(self.investment_usd, self.start_exchange_rate, self.end_exchange_rate, self.bond_spec)
        self.assertIsInstance(result, BondYieldResult)
        self.assertAlmostEqual(result.total_return_usd, 1738.75, places=2)
        self.assertAlmostEqual(result.profit_usd, 738.75, places=2)
        self.assertAlmostEqual(result.profit_percentage, 73.875, places=2)

    def test_bond_yield_with_increased_exchange_rate(self):
        """Test when the end exchange rate is higher than the start exchange rate."""
        result = calculate_bond_yield(self.investment_usd, self.start_exchange_rate, 50, self.bond_spec)
        self.assertIsInstance(result, BondYieldResult)
        self.assertAlmostEqual(result.total_return_usd, 1286.675, places=2)
        self.assertAlmostEqual(result.profit_usd, 286.675, places=2)
        self.assertAlmostEqual(result.profit_percentage, 28.67, places=2)

    def test_bond_yield_with_zero_investment(self):
        """Test with zero investment amount. Expect ValueError."""
        with self.assertRaises(ValueError):
            calculate_bond_yield(0, self.start_exchange_rate, self.end_exchange_rate, self.bond_spec)

    def test_bond_yield_with_negative_investment(self):
        """Test with negative investment amount. Expect ValueError."""
        with self.assertRaises(ValueError):
            calculate_bond_yield(-1000, self.start_exchange_rate, self.end_exchange_rate, self.bond_spec)


if __name__ == '__main__':
    unittest.main()
