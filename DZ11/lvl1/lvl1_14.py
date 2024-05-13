import nltk
from nltk import collocations


def col(txt: str):
    colocation = collocations.BigramCollocationFinder(nltk.corpus.genesis.words('russian-web.txt'), 2)
    print(colocation)


def main():
    with open('2.txt', 'r') as file:
        text = file.read()

    col(text)


if __name__ == '__main__':
    main()
