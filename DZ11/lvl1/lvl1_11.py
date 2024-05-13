from nltk.probability import FreqDist

from lvl1_9 import lemma


def build():
    fd = FreqDist(lemma())
    fd.plot(30, cumulative=False)


if __name__ == '__main__':
    build()
