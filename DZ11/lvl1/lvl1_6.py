from lvl1_3 import main


def delete_punctuation() -> list[str]:
    return [word for word in main() if word.isalpha()]


if __name__ == '__main__':
    print(delete_punctuation())
