# Sentiment Count Visualization

import matplotlib.pyplot as plt


def plot_sentiment_counts():
    # Sample sentiment data
    sentiments = ['Positive', 'Negative', 'Neutral']
    counts = [50, 30, 20]

    # Create figure
    plt.figure(figsize=(8, 5))

    # Plot bar chart
    bars = plt.bar(sentiments, counts)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height}',
            ha='center',
            va='bottom'
        )

    # Labels and title
    plt.xlabel("Sentiment Type")
    plt.ylabel("Number of Reviews")
    plt.title("Sentiment Analysis Review Count")

    # Grid for readability
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Show plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_sentiment_counts()