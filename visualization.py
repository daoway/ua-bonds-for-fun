import matplotlib.pyplot as plt


def visualize_profits(end_exchange_rates, profits_usd, filename):
    """
    Visualizes the profits in USD against different end exchange rates.

    Parameters:
    - end_exchange_rates: List of exchange rates at the end of the investment period.
    - profits_usd: List of profits corresponding to the exchange rates.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(end_exchange_rates, profits_usd, marker='o')
    plt.title("Bond Investment Profit vs. End Exchange Rate")
    plt.xlabel("End Exchange Rate (UAH/USD)")
    plt.ylabel("Profit (USD)")
    plt.grid(True)
    #plt.show()
    plt.savefig(filename)  # Save the plot as a PNG file
    plt.close()  # Close the plot to free up memory

