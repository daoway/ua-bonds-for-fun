import matplotlib.pyplot as plt
import numpy as np

from bond import BondSpecBuilder


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


def visualize_profits(investment_usd, start_exchange_rate, end_exchange_rate_range, bond_spec,
                      filename='profits_vs_exchange_rate.png'):
    """
    Visualize how profit changes with varying end exchange rates and save the plot as a PNG file.

    Parameters:
    investment_usd (float): The amount of investment in USD.
    start_exchange_rate (float): The exchange rate from USD to UAH at the start.
    end_exchange_rate_range (tuple): The range of end exchange rates (start, end, step).
    bond_spec (BondSpec): The specifications of the bond.
    filename (str): The name of the PNG file to save the plot.
    """
    end_rates = np.arange(end_exchange_rate_range[0], end_exchange_rate_range[1] + end_exchange_rate_range[2],
                          end_exchange_rate_range[2])
    profits = []

    for end_rate in end_rates:
        _, profit_usd = calculate_bond_yield(investment_usd, start_exchange_rate, end_rate, bond_spec)
        profits.append(profit_usd)

    plt.figure(figsize=(10, 6))
    plt.plot(end_rates, profits, marker='o')
    plt.xlabel('End Exchange Rate (UAH/USD)')
    plt.ylabel('Profit in USD')
    plt.title('Profit vs. End Exchange Rate')
    plt.grid(True)
    #plt.show()
    plt.savefig(filename)  # Save the plot as a PNG file
    plt.close()  # Close the plot to free up memory


def main():
    # Example usage
    investment_usd = 1000  # Investment amount in USD
    start_exchange_rate = 37  # Exchange rate UAH/USD at the start
    end_exchange_rate_range = (37, 150, 1)  # Range of end exchange rates (start, end, step)

    # Create BondSpec object using Builder
    bond_spec = (BondSpecBuilder()
                 .set_coupon_rate(9.85)
                 .set_nominal_yield_rate(19.70)
                 .set_duration_years(2.5)
                 .build())

    # Visualize profits and save the plot as a PNG file
    visualize_profits(investment_usd, start_exchange_rate, end_exchange_rate_range, bond_spec,
                      'profits_vs_exchange_rate.png')


if __name__ == "__main__":
    main()
