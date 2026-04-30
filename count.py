# Word Cloud Visualization from Text

from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_wordcloud(text):
    # Create WordCloud object
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sample_text = """
    data science machine learning python data analysis visualization
    statistics data mining machine learning python data science
    """

    generate_wordcloud(sample_text)