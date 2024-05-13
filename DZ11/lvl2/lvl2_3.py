from collections import Counter
import matplotlib.pyplot as plt

from lvl2_2 import main


def most_common(data: list, n: int) -> list[tuple[str, int]]:
    words = dict(Counter([i[0] for i in data]))
    sorted_words = sorted(list(words.keys()), key=lambda x: words[x], reverse=True)
    words = [(word, words[word]) for word in sorted_words if len(word) > 3]

    return words[:n]


def graphic():
    words_and_frequency = most_common(list(main()), 30)
    words = [i[0] for i in words_and_frequency]
    frequency = [i[1] for i in words_and_frequency]

    plt.ylabel("Frequency")
    plt.xlabel('Words')
    plt.plot(words, frequency)
    plt.xticks(rotation=90)

    plt.show()


if __name__ == '__main__':
    graphic()
