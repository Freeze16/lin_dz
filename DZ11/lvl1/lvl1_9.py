from pymorphy2 import MorphAnalyzer

from lvl1_7 import delete_stop_words


def lemma():
    morph = MorphAnalyzer()
    return [morph.parse(word)[0].normal_form for word in delete_stop_words()]


if __name__ == '__main__':
    # 4.536506175994873
    print(lemma())
