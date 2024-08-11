import matplotlib.pyplot as plt
import numpy as np

from bond import BondSpecBuilder, calculate_bond_yield

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
