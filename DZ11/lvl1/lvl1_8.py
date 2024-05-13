from nltk.stem import PorterStemmer

from lvl1_7 import delete_stop_words


def stemming() -> list[str]:
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in delete_stop_words()]


if __name__ == '__main__':
    print(stemming())
