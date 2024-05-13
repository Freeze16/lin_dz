from nltk.probability import FreqDist
import matplotlib.pyplot as plt

from lvl1_9 import lemma


def build(data=lemma()):
    words = dict(FreqDist(data).most_common(30))
    plt.ylabel("Frequency")
    plt.xlabel('Words')
    plt.plot(list(words.keys()), list(words.values()))
    plt.xticks(rotation=90)

    plt.show()


if __name__ == '__main__':
    build()
