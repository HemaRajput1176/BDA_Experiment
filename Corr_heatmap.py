# Correlation Heatmap Visualization

import pandas as pd
import matplotlib.pyplot as plt


def plot_correlation_heatmap():
    # Sample dataset with multiple features
    data = pd.DataFrame({
        'Math': [85, 90, 78, 92, 88],
        'Science': [80, 85, 75, 95, 89],
        'English': [78, 82, 74, 88, 86],
        'History': [72, 76, 70, 85, 80]
    })

    # Calculate correlation matrix
    corr_matrix = data.corr()

    # Create figure
    plt.figure(figsize=(6, 5))

    # Plot heatmap using matplotlib
    plt.imshow(corr_matrix, interpolation='nearest')
    plt.colorbar()

    # Add ticks and labels
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

    # Add title
    plt.title("Correlation Heatmap")

    # Annotate correlation values
    for i in range(len(corr_matrix.columns)):
        for j in range(len(corr_matrix.columns)):
            plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                     ha='center', va='center')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_correlation_heatmap()