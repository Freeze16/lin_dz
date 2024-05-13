from pymorphy2 import MorphAnalyzer
from pymorphy2.tagset import OpencorporaTag

from lvl1_7 import delete_stop_words


def morph_analyze() -> dict[str, OpencorporaTag]:
    morph = MorphAnalyzer()
    return {word: morph.parse(word)[0].tag for word in delete_stop_words()}


if __name__ == '__main__':
    print(morph_analyze())
