from collections import Counter

from lvl1_2 import main


if __name__ == '__main__':
    words = Counter(main())

    print(words)
    print(sum(list(words.values())))
