import unittest

from bond import BondSpecBuilder, BondSpec


class TestBondSpecBuilder(unittest.TestCase):

    def test_build_valid_bond_spec(self):
        """Test that BondSpecBuilder correctly builds a BondSpec object."""
        builder = BondSpecBuilder()
        bond_spec = (
            builder.set_coupon_rate(9.85)
            .set_nominal_yield_rate(19.70)
            .set_duration_years(2.5)
            .build()
        )

        self.assertIsInstance(bond_spec, BondSpec)
        self.assertEqual(bond_spec.coupon_rate, 9.85)
        self.assertEqual(bond_spec.nominal_yield_rate, 19.70)
        self.assertEqual(bond_spec.duration_years, 2.5)

    def test_missing_parameters(self):
        """Test that BondSpecBuilder raises a ValueError when parameters are missing."""

        with self.assertRaises(ValueError):
            builder = BondSpecBuilder()
            builder.set_coupon_rate(9.85).build()  # Missing nominal_yield_rate and duration_years

        with self.assertRaises(ValueError):
            builder = BondSpecBuilder()
            builder.set_nominal_yield_rate(19.70).build()  # Missing coupon_rate and duration_years

        with self.assertRaises(ValueError):
            builder = BondSpecBuilder()
            builder.set_duration_years(2.5).build()  # Missing coupon_rate and nominal_yield_rate

    def test_invalid_values(self):
        """Test that BondSpecBuilder handles invalid input correctly."""
        builder = BondSpecBuilder()

        with self.assertRaises(ValueError):
            builder.set_coupon_rate(-5).build()


if __name__ == '__main__':
    unittest.main()
