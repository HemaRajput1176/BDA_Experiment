# Sales by Category - Bar Chart Visualization

import pandas as pd
import matplotlib.pyplot as plt


def create_sales_bar_chart():
    # Create DataFrame
    data = pd.DataFrame({
        'Category': ['Electronics', 'Clothing', 'Food'],
        'Sales': [40000, 30000, 20000]
    })

    # Create figure
    plt.figure(figsize=(8, 5))

    # Plot bar chart
    bars = plt.bar(data['Category'], data['Sales'])

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height}',
            ha='center',
            va='bottom',
            fontsize=10
        )

    # Add labels and title
    plt.xlabel("Product Category")
    plt.ylabel("Total Sales")
    plt.title("Sales by Category")

    # Add grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Adjust layout and show plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    create_sales_bar_chart()