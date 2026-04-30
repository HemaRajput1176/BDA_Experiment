# Market Share - Pie Chart Visualization

import matplotlib.pyplot as plt


def plot_market_share_pie():
    # Sample market share data
    companies = ['Company A', 'Company B', 'Company C', 'Company D']
    market_share = [35, 25, 20, 20]

    # Create figure
    plt.figure(figsize=(7, 7))

    # Plot pie chart
    plt.pie(
        market_share,
        labels=companies,
        autopct='%1.1f%%',
        startangle=90
    )

    # Title
    plt.title("Company Market Share")

    # Equal aspect ratio ensures pie is a circle
    plt.axis('equal')

    # Display
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_market_share_pie()