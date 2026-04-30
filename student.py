# Student Marks Distribution - Histogram Visualization

import matplotlib.pyplot as plt


def plot_marks_histogram():
    # Sample marks data
    marks = [35, 42, 55, 60, 65, 70, 72, 75, 80, 82, 85, 88, 90, 92, 95]

    # Create figure
    plt.figure(figsize=(8, 5))

    # Plot histogram
    plt.hist(marks, bins=6)

    # Labels and title
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.title("Student Marks Distribution")

    # Grid for readability
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_marks_histogram()