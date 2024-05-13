from spacy import load


def main():
    nlp = load('ru_core_news_md')
    text = 'Привет, привет-привет а и он почему'

    doc = nlp.tokenizer(text)
    lemma_and_morph = {i.norm_: i.morph for i in doc}
    return lemma_and_morph.keys()


if __name__ == '__main__':
    print(main())