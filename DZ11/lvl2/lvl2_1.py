import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

from pymorphy2 import MorphAnalyzer

from hash_table import HashTable


def get_tokens() -> list[str]:
    nltk.download('punkt')
    nltk.download('stopwords')

    with open('2.txt', 'r') as file:
        txt = file.read()

    tokens = word_tokenize(txt)
    return [word for word in tokens if (word not in stopwords.words('russian')) and word.isalpha()]


def lemma(words: list[str]) -> list[str]:
    morph = MorphAnalyzer()
    cache = HashTable()

    lemmas = []
    for word in words:
        if not cache.contains(word):
            lemmas.append(morph.parse(word)[0].normal_form)
            cache.set_value(word, lemmas[-1])
        else:
            lemmas.append(cache.get_value(word))

    return lemmas


def main():
    tokens = get_tokens()
    return lemma(tokens)


if __name__ == '__main__':
    print(main())
