# Word Frequency Bar Chart from Text

import matplotlib.pyplot as plt
from collections import Counter
import re


def plot_word_frequency(text, top_n=8):
    # Convert to lowercase and remove punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

    # Split into words
    words = cleaned_text.split()

    # Count word frequencies
    word_counts = Counter(words)

    # Get top N most common words
    common_words = word_counts.most_common(top_n)
    labels = [word for word, count in common_words]
    counts = [count for word, count in common_words]

    # Create bar chart
    plt.figure(figsize=(9, 5))
    bars = plt.bar(labels, counts)

    # Add values on top of bars
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
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top Word Frequencies in Text")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sample_text = """
    Data science is an interdisciplinary field that uses scientific methods,
    processes, algorithms and systems to extract knowledge and insights from data.
    Data science is widely used in machine learning, statistics, and analytics.
    """

    plot_word_frequency(sample_text)