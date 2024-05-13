from lvl1_2 import main


def length(txt: list[str]) -> dict[str, int]:
    words = {}
    for word in txt:
        if not words.get(word):
            words[word] = 1
        else:
            words[word] += 1

    return words


if __name__ == '__main__':
    text = main()

    print(length(text))
    print(len(text))
