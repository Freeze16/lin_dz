from spacy import load
from spacy.lang.ru import Russian


def main():
    nlp = load('ru_core_news_md')
    with open('2.txt', 'r') as file:
        text = file.read()

    doc = nlp(text)
    lemma_and_morph = [(i.lemma_, i.morph) for i in doc if i.is_alpha and not nlp.vocab[i.lemma_].is_stop]

    return lemma_and_morph


if __name__ == '__main__':
    print(main())
