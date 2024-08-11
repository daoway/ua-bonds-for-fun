from bond import BondSpecBuilder
from bond_calc import calculate_bond_yield
from visualization import visualize_profits
import numpy as np


def main():
    investment_usd = 1000  # Investment amount in USD
    start_exchange_rate = 37  # Initial exchange rate (UAH/USD)
    end_exchange_rate_range = (
        start_exchange_rate, 150, 1)  # Range of final exchange rates to simulate (start, stop, step)
    coupon_rate = 9.85  # Coupon rate in percentage
    nominal_yield_rate = 19.70  # Nominal yield rate in percentage
    duration_years = 2.5  # Duration of the bond in years

    bond_spec = (BondSpecBuilder()
                 .set_coupon_rate(coupon_rate)
                 .set_nominal_yield_rate(nominal_yield_rate)
                 .set_duration_years(duration_years)
                 .build())

    end_rates = np.arange(end_exchange_rate_range[0], end_exchange_rate_range[1] + end_exchange_rate_range[2],
                          end_exchange_rate_range[2])

    profits_usd = []

    for end_exchange_rate in end_rates:
        result = calculate_bond_yield(investment_usd, start_exchange_rate, end_exchange_rate, bond_spec)
        profits_usd.append(result.profit_usd)

    # Visualize the profits
    visualize_profits(end_rates, profits_usd, 'profits_vs_exchange_rate.png')


if __name__ == "__main__":
    main()
